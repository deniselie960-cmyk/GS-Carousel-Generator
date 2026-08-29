from __future__ import annotations

import re
import subprocess
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageStat


BANNER = Path(r"C:\Users\LENOVO\Downloads\Web banner main design\Web banner main design.jpg")
SOURCE_ROOT = Path(r"C:\Users\LENOVO\Downloads\FMO LI\Logo for LI FMO")
OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "output" / "web-banners"
PDFTOPPM = Path(
    r"C:\Users\LENOVO\.cache\codex-runtimes\codex-primary-runtime"
    r"\dependencies\native\poppler\Library\bin\pdftoppm.exe"
)

# The rounded white panel beneath "Visit Our Booth" is approximately
# x=155..648, y=282..573. This inner box keeps artwork clear of its corners.
SAFE_BOX = (185, 306, 618, 550)
RASTER_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}


def safe_name(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._ -]+", "", value).strip().rstrip(".")
    return re.sub(r"\s+", " ", value)


def render_pdf(path: Path, temp_dir: Path) -> Path:
    prefix = temp_dir / safe_name(path.stem)
    output = prefix.with_suffix(".png")
    subprocess.run(
        [str(PDFTOPPM), "-png", "-singlefile", "-r", "300", str(path), str(prefix)],
        check=True,
        capture_output=True,
    )
    return output


def corner_background(im: Image.Image) -> tuple[int, int, int]:
    rgb = im.convert("RGB")
    w, h = rgb.size
    side = max(1, min(w, h) // 18)
    samples = [
        rgb.crop((0, 0, side, side)),
        rgb.crop((w - side, 0, w, side)),
        rgb.crop((0, h - side, side, h)),
        rgb.crop((w - side, h - side, w, h)),
    ]
    joined = Image.new("RGB", (side * 4, side))
    for index, sample in enumerate(samples):
        joined.paste(sample, (index * side, 0))
    mean = ImageStat.Stat(joined).median
    return tuple(int(x) for x in mean[:3])


def trim_logo(path: Path) -> Image.Image:
    im = Image.open(path).convert("RGBA")
    alpha = im.getchannel("A")
    alpha_bbox = alpha.point(lambda value: 255 if value > 8 else 0).getbbox()

    # Transparent artwork: trim using alpha. Opaque scans/JPEGs: trim against
    # the color sampled from the page corners.
    if alpha.getextrema()[0] < 250 and alpha_bbox:
        bbox = alpha_bbox
    else:
        bg = corner_background(im)
        background = Image.new("RGB", im.size, bg)
        difference = ImageChops.difference(im.convert("RGB"), background).convert("L")
        mask = difference.point(lambda value: 255 if value > 18 else 0)
        bbox = mask.getbbox() or (0, 0, im.width, im.height)

        # When the sampled background is near-white, make only near-white page
        # pixels transparent so rectangular JPG/PDF edges disappear on the box.
        if min(bg) >= 232:
            rgba = im.load()
            for y in range(im.height):
                for x in range(im.width):
                    r, g, b, a = rgba[x, y]
                    whiteness = min(r, g, b)
                    if whiteness >= 248:
                        rgba[x, y] = (r, g, b, 0)
                    elif whiteness > 232:
                        rgba[x, y] = (r, g, b, int(a * (248 - whiteness) / 16))

    left, top, right, bottom = bbox
    pad_x = max(2, int((right - left) * 0.025))
    pad_y = max(2, int((bottom - top) * 0.025))
    crop_box = (
        max(0, left - pad_x),
        max(0, top - pad_y),
        min(im.width, right + pad_x),
        min(im.height, bottom + pad_y),
    )
    return im.crop(crop_box)


def place_logo(template: Image.Image, logo: Image.Image) -> Image.Image:
    result = template.copy().convert("RGBA")
    left, top, right, bottom = SAFE_BOX
    max_w, max_h = right - left, bottom - top
    scale = min(max_w / logo.width, max_h / logo.height)
    size = (max(1, round(logo.width * scale)), max(1, round(logo.height * scale)))
    logo = logo.resize(size, Image.Resampling.LANCZOS)
    x = left + (max_w - logo.width) // 2
    y = top + (max_h - logo.height) // 2
    result.alpha_composite(logo, (x, y))
    return result.convert("RGB")


def contact_sheet(items: list[tuple[str, Path]], output: Path) -> None:
    thumb_w, thumb_h = 640, 169
    label_h, margin, gap, columns = 38, 28, 22, 2
    rows = (len(items) + columns - 1) // columns
    width = margin * 2 + columns * thumb_w + (columns - 1) * gap
    height = margin * 2 + rows * (thumb_h + label_h) + (rows - 1) * gap
    sheet = Image.new("RGB", (width, height), "#e9edf3")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default(size=20)

    for index, (name, path) in enumerate(items):
        row, column = divmod(index, columns)
        x = margin + column * (thumb_w + gap)
        y = margin + row * (thumb_h + label_h + gap)
        thumb = Image.open(path).convert("RGB")
        thumb.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        sheet.paste(thumb, (x, y))
        draw.text((x, y + thumb_h + 8), name, fill="#111827", font=font)

    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output, quality=94, subsampling=0)


def main() -> None:
    template = Image.open(BANNER).convert("RGB")
    temp_dir = OUTPUT_ROOT / "_rendered-pdf-logos"
    temp_dir.mkdir(parents=True, exist_ok=True)

    for group in ("VIP", "Non VIP"):
        source_dir = SOURCE_ROOT / group
        output_dir = OUTPUT_ROOT / group
        output_dir.mkdir(parents=True, exist_ok=True)
        outputs: list[tuple[str, Path]] = []

        for source in sorted(source_dir.iterdir(), key=lambda item: item.name.lower()):
            extension = source.suffix.lower()
            if extension == ".pdf":
                logo_path = render_pdf(source, temp_dir)
            elif extension in RASTER_EXTENSIONS:
                logo_path = source
            else:
                continue

            display_name = safe_name(source.stem)
            output_path = output_dir / f"{display_name} - Web Banner.jpg"
            logo = trim_logo(logo_path)
            banner = place_logo(template, logo)
            banner.save(output_path, quality=95, subsampling=0, optimize=True)
            outputs.append((display_name, output_path))

        contact_sheet(outputs, OUTPUT_ROOT / f"Contact Sheet - {group}.jpg")

    print(f"Created banner sets in: {OUTPUT_ROOT}")


if __name__ == "__main__":
    main()
