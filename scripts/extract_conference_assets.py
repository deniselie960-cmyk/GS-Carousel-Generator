from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image
from psd_tools import PSDImage


ARTBOARD_SIZE = (1080, 1350)


def paste_on_artboard(layer, artboard, destination: Path) -> None:
    rendered = layer.composite()
    if rendered is None:
        raise RuntimeError(f"Layer {layer.name!r} did not render")

    canvas = Image.new("RGBA", ARTBOARD_SIZE, (0, 0, 0, 0))
    x = layer.left - artboard.left
    y = layer.top - artboard.top
    if rendered.mode != "RGBA":
        rendered = rendered.convert("RGBA")
    canvas.alpha_composite(rendered, (x, y))
    canvas.save(destination, optimize=True)
    print(f"Saved {destination.name}: {layer.name!r} at ({x}, {y})")


def save_cropped(layer, destination: Path) -> None:
    rendered = layer.composite()
    if rendered is None:
        raise RuntimeError(f"Layer {layer.name!r} did not render")
    if rendered.mode != "RGBA":
        rendered = rendered.convert("RGBA")
    rendered.save(destination, optimize=True)
    print(f"Saved {destination.name}: {layer.name!r} {rendered.size}")


def main() -> None:
    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    output.mkdir(parents=True, exist_ok=True)

    psd = PSDImage.open(source)
    artboard = next(layer for layer in psd if layer.name == "slide 2")

    paste_on_artboard(artboard[0], artboard, output / "paper-background.png")
    paste_on_artboard(artboard[1], artboard, output / "decor-bottom-left.png")
    paste_on_artboard(artboard[2], artboard, output / "decor-top-left.png")
    paste_on_artboard(artboard[13], artboard, output / "decor-globe.png")
    paste_on_artboard(artboard[14], artboard, output / "event-logos.png")

    date_group = artboard[12][5]
    save_cropped(date_group[0], output / "icon-calendar.png")
    save_cropped(date_group[2], output / "icon-clock.png")
    save_cropped(date_group[4], output / "icon-location.png")


if __name__ == "__main__":
    main()
