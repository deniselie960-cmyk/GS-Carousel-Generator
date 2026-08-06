# Global Sources Carousel Design Ground Rules

Use this document as the source of truth when creating the next carousel in this system. The final NICE SO and Eiger carousels are the benchmark campaigns. New slides should feel like part of the same family even when the story, brand, statistics, photographs, and diagrams change.

## 1. Format and safe area

- Design each slide at `1080 × 1350px` (4:5 portrait).
- Export at 2× density: `2160 × 2700px`.
- Keep `72px` as the preferred text-safe margin from the left and right edges.
- Treat the logo, headline, supporting copy, and main visual as one composition stack.
- Optically center the composition stack vertically within the usable canvas, excluding the footer.
- Do not use a universal fixed `top` value for the logo or primary content.
- Large visual elements may use more horizontal width than the text-safe area when they remain balanced and unclipped.
- Keep the footer at `bottom: 48px`, aligned to both safe edges.
- Nothing important may touch or cross the safe-area boundary.

The canvas dimensions and shared page margin are controlled by:

```css
--canvas-w: 1080px;
--canvas-h: 1350px;
--page-x: 72px;
--visual-x: 32px;
--composition-footer-space: 96px;
--composition-gap: 34px;
```

## 2. Visual character

The design should feel editorial, bold, modern, and credible—not like a generic corporate presentation.

- Use the paper texture on every slide. Alternate between white paper and dark-blue paper when the story benefits from a stronger rhythm.
- Preserve the subtle blue dot field and soft blue/yellow edge glows.
- Use clean geometric forms, strong type, restrained shadows, and generous negative space.
- Use blue as the dominant emphasis color and amber only as a supporting accent.
- Avoid unnecessary decoration. Every graphic must explain, organize, or emphasize information.

## 3. Color system

Use the existing tokens in `shared/styles/system.css`:

| Role | Token | Value |
| --- | --- | --- |
| Primary emphasis | `--primary` | `#318ff0` |
| Darker blue | `--primary-dark` | `#176dc7` |
| Accent | `--amber` | `#f3b51b` |
| Main text | `--ink` | `#20232b` |
| Secondary text | `--muted` | `#687083` |
| White | `--white` | `#ffffff` |

Do not introduce a new dominant color unless it is essential to the featured brand. If a brand color is added, keep blue as the carousel system color.

## 4. Branding and hierarchy

- Show the full-color Global Sources logo strip on white slides and the white logo strip on blue slides.
- Keep its size, appearance, and opacity consistent across the carousel.
- Align the logo to the slide's primary content axis: left with left-aligned content and centered with centered content.
- Keep the logo inside the same composition stack as the headline, body, and main visual.
- Show the featured brand logo on slide 1 only, unless another slide specifically discusses brand identity.
- The order of attention should be: headline → key visual/data → supporting copy → navigation.
- Do not use category eyebrow labels such as “Asal-usul,” “Pertumbuhan,” or “Kesimpulan.” These were removed from the final design.

### Composition modes

Every standard slide must use one explicit composition mode:

- `.composition--left`: logo, headline, and body share the left content axis. The main visual may expand toward the right.
- `.composition--center`: logo, headline, body, and primary visual share the canvas center axis.

Canonical structure:

```html
<div class="composition composition--left">
  <header class="topbar">...</header>
  <section class="content">...</section>
</div>
```

Use `composition--center` for a centered slide. Do not center the logo independently from left-aligned content, or left-align it above a centered composition.

The standard `.composition` fills the canvas above the footer and uses flex centering to balance the entire stack vertically. Judge top and bottom space optically because a dense chart or large image carries more visual weight than text.

The `72px` margin is mandatory for important text. Decorative backgrounds, charts, orbit lines, images, and cards may approach the `32px` visual margin or bleed to an edge when the design requires it. Nothing essential may be clipped.

Full-bleed media slides may use local positioning overrides, but the logo must still follow the editorial content alignment and the full composition must remain visually balanced.

## 5. Headline system

Headlines are uppercase, Gotham Black (`900`), tightly tracked, and visually dominant.

```css
.headline {
  line-height: 0.98;
  letter-spacing: -0.045em;
  font-weight: 900;
  text-transform: uppercase;
}
```

### Line composition

- Write intentional line breaks in the HTML; do not rely on automatic wrapping.
- Prefer `2–3 words` per line for readable, poster-like rhythm.
- Use no more than three headline lines.
- Avoid four-word lines unless the wording cannot be separated; any exception must be verified in the rendered slide.
- If a required line is too long, reduce only that line’s font size. Do not compress the whole slide or allow the box to overflow.
- Keep `0.12em` vertical space between headline lines.

### Headline emphasis box

- Apply the emphasis box to the first headline line only.
- On white paper, use the blue box with white type.
- On blue paper, use the amber box with dark type.
- The box must hug the text, remain on one line, and stay inside the safe area.
- Do not extend the box to full canvas width.
- Do not use multiple headline boxes on one slide.

Canonical markup:

```html
<h1 class="headline">
  <span class="highlight">First emphasized line</span>
  <span class="line">Second headline line</span>
</h1>
```

Add another `<span class="line">` only when a third line is necessary.

For an unusually long emphasized line, use a local override:

```css
.headline .highlight { font-size: 0.84em; }
```

### Final NICE SO headline compositions

Use these as visual references for length and rhythm:

1. `DIKIRA BRAND` / `IMPOR KOREA,` / `TERNYATA MILIK LOKAL!`
2. `TERNYATA INI` / `RACIKAN ASLI` / `ANAK BANGSA`
3. `DIAM-DIAM NYALIP` / `TANPA NAMA BESAR` / `DARI LUAR`
4. `BUKAN SEKEDAR MIRIP.` / `INI BUKTI.`

### Final Eiger benchmark patterns

Use the Eiger carousel as the reference for these additional treatments:

1. **Editorial cover photography:** a wide photograph may replace a diagram when the featured storefront already supplies the brand identity.
2. **Alternating backgrounds:** use white paper on slides 1 and 3, then blue paper on slides 2 and 4, unless another sequence better supports the story.
3. **Blue-paper headline:** use an amber first-line box with dark type; keep remaining headline lines white.
4. **Photo collage:** combine two complementary images at restrained sizes instead of stretching a low-resolution image across the canvas.
5. **Meaningful chart selection:** a chart must visualize the claim accurately. Use an uninterrupted timeline for consistency, not a rising graph that would imply unsupported growth.
6. **Conclusion diagram:** center the logo, headline, explanatory visual, and takeaway when the final slide is a synthesis rather than a left-to-right narrative.

The Eiger headline references are:

1. `KENAPA EIGER` / `TETAP RELEVAN` / `SELAMA PULUHAN TAHUN?`
2. `KONSISTENSI YANG` / `BIKIN MEREKA KUAT`
3. `YANG DIJUAL` / `BUKAN SEKADAR PRODUK`
4. `PELAJARAN DARI EIGER`

## 6. Body copy

- Use sentence case and regular-weight Gotham for supporting text.
- Keep body copy between `25–29px`, with approximately `1.42–1.46` line height.
- Keep paragraphs short: ideally two to four lines.
- Bold only the proof point, date, number, or phrase the reader must remember.
- Do not repeat the headline in the body copy.
- Maintain at least `28–36px` between the headline and supporting copy or divider.

## 7. Data, cards, and diagrams

- Give each slide one dominant visual device: network, dial, chart, orbit, comparison, or another simple explanatory form.
- Use inline SVG for icons and charts when possible so exports remain sharp.
- Use editorial photo cards with fine white borders and restrained shadows when photography is the dominant visual.
- When source images are small, use a two-image collage at native-friendly sizes instead of a full-canvas enlargement.
- Use rounded cards with translucent white fills, fine borders, and soft shadows.
- Keep large metrics bold and unmistakable; supporting labels should be smaller and muted.
- Use amber for nodes, chart points, or secondary labels—not large background areas.
- Keep diagrams visually balanced within the 72px safe area.
- Avoid adding details that cannot be read comfortably on a phone.

## 8. Carousel story structure

A four-slide carousel should normally follow this sequence:

1. **Hook:** surprising claim, featured brand, and swipe cue.
2. **Context:** origin, mechanism, people, or background.
3. **Evidence:** growth, comparison, scale, or measurable proof.
4. **Conclusion:** synthesis, takeaway, and closing statement.

Each slide must make sense by itself while advancing the same story. Do not make every slide use the same diagram or layout.

## 9. Footer and navigation

- Show the slide number as `01 / 04`, `02 / 04`, and so on.
- Use the progress indicator on slides 2–4.
- Slide 1 may replace the progress indicator with a small “Swipe ke kiri” cue.
- Footer text is secondary and must never compete with the content.
- Update both the active progress marker and slide number when duplicating a slide.

## 10. File responsibilities

- `shared/styles/system.css`: shared tokens, canvas, typography, headline treatment, footer, icons, and reusable components.
- `shared/assets/`: Global Sources logos, shared textures, and system-wide assets.
- `carousels/<brand>/<campaign>/slides/slide-XX.html`: slide-specific content, layout, diagram, and local sizing exceptions.
- `carousels/<brand>/<campaign>/assets/`: campaign-specific logos and images.
- `carousels/<brand>/<campaign>/content/`: reusable copy source and story outline.
- `scripts/render.mjs`: automated PNG/JPG export.
- `carousels/<brand>/<campaign>/rendered/`: generated output only; do not treat rendered images as editable source files.

Put a rule in `shared/styles/system.css` only if it should apply to multiple slides or campaigns. Keep one-off adjustments inside the relevant slide’s `<style>` block.

## 11. Building a new slide

1. Duplicate the closest existing slide structure.
2. Choose `.composition--left` or `.composition--center` before positioning individual elements.
3. Change the title, content, slide number, and progress state.
4. Rewrite the headline using intentional `<span>` lines.
5. Keep only the first line inside `.highlight`.
6. Replace the central visual while preserving text safety and optical balance.
7. Open the HTML directly in a browser for a quick check.
8. Render the complete carousel and inspect the PNG files at full size.

## 12. Rendering

First-time setup:

```powershell
npm install
```

Render PNG files:

```powershell
npm run render:png -- carousels/eiger/brand-longevity
```

Render JPG files:

```powershell
npm run render:jpg -- carousels/eiger/brand-longevity
```

Exports are written to the selected campaign's `rendered/` directory.

## 13. Final QA checklist

Before approving a carousel, verify every item:

- [ ] Canvas is 1080 × 1350 and output is sharp.
- [ ] Global Sources logo strip is identical on every slide.
- [ ] The full-color logo is used on white paper and the white logo is used on blue paper.
- [ ] The logo follows the same left or center axis as the primary content.
- [ ] The logo, headline, body, and visual read as one composition stack.
- [ ] The complete stack is optically centered between the top of the canvas and the footer zone.
- [ ] Important text stays inside the 72px text-safe area.
- [ ] Wider visual elements remain balanced, intentional, and unclipped.
- [ ] Headline line breaks are intentional.
- [ ] Headline lines preferably contain 2–3 words.
- [ ] Only the first headline line has an emphasis box.
- [ ] The emphasis box uses blue/white on white paper or amber/dark on blue paper.
- [ ] The emphasis box is one line and does not clip or overflow.
- [ ] Supporting copy is readable and not overcrowded.
- [ ] Numbers and proof points are visually emphasized.
- [ ] The main visual has a clear purpose.
- [ ] Slide number and progress state are correct.
- [ ] No removed category eyebrow labels have been reintroduced.
- [ ] All slides have been rendered and visually inspected, not merely checked in code.
