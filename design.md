# Global Sources Carousel Design Ground Rules

Use this document as the source of truth when creating the next carousel in this system. New slides should feel like part of the same family as the final NICE SO carousel, even when the story, brand, statistics, and diagrams change.

## 1. Format and safe area

- Design each slide at `1080 × 1350px` (4:5 portrait).
- Export at 2× density: `2160 × 2700px`.
- Keep the main horizontal safe area at `72px` from the left and right edges.
- Place the Global Sources logo strip at `top: 55px`, aligned to the left safe edge.
- Start primary content around `top: 220px`. Slide 1 may start at `225px` to accommodate its brand mark.
- Keep the footer at `bottom: 48px`, aligned to both safe edges.
- Nothing important may touch or cross the safe-area boundary.

The canvas dimensions and shared page margin are controlled by:

```css
--canvas-w: 1080px;
--canvas-h: 1350px;
--page-x: 72px;
```

## 2. Visual character

The design should feel editorial, bold, modern, and credible—not like a generic corporate presentation.

- Use the white paper texture as the base background.
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

- Show the full-color Global Sources logo strip on every slide.
- Keep its position, size, and opacity consistent across the carousel.
- Show the featured brand logo on slide 1 only, unless another slide specifically discusses brand identity.
- The order of attention should be: headline → key visual/data → supporting copy → navigation.
- Do not use category eyebrow labels such as “Asal-usul,” “Pertumbuhan,” or “Kesimpulan.” These were removed from the final design.

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
- A four-word line is allowed when the final wording must stay together, as on slide 1: “DIKIRA BRAND IMPOR KOREA,”.
- If a required line is too long, reduce only that line’s font size. Do not compress the whole slide or allow the box to overflow.
- Keep `0.12em` vertical space between headline lines.

### Blue emphasis box

- Apply the blue box to the first headline line only.
- Use white type inside the box.
- The box must hug the text, remain on one line, and stay inside the safe area.
- Do not extend the box to full canvas width.
- Do not use multiple blue headline boxes on one slide.

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

1. `DIKIRA BRAND IMPOR KOREA,` / `TERNYATA MILIK LOKAL!`
2. `TERNYATA INI` / `RACIKAN ASLI` / `ANAK BANGSA`
3. `DIAM-DIAM NYALIP` / `TANPA NAMA BESAR` / `DARI LUAR`
4. `BUKAN SEKEDAR MIRIP.` / `INI BUKTI.`

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
2. Change the title, content, slide number, and progress state.
3. Rewrite the headline using intentional `<span>` lines.
4. Keep only the first line inside `.highlight`.
5. Replace the central visual while preserving the safe area and overall hierarchy.
6. Open the HTML directly in a browser for a quick check.
7. Render the complete carousel and inspect the PNG files at full size.

## 12. Rendering

First-time setup:

```powershell
npm install
```

Render PNG files:

```powershell
npm run render:png
```

Render JPG files:

```powershell
npm run render:jpg
```

Exports are written to the selected campaign's `rendered/` directory.

## 13. Final QA checklist

Before approving a carousel, verify every item:

- [ ] Canvas is 1080 × 1350 and output is sharp.
- [ ] Global Sources logo strip is identical on every slide.
- [ ] All important content stays inside the 72px horizontal safe area.
- [ ] Headline line breaks are intentional.
- [ ] Headline lines preferably contain 2–3 words.
- [ ] Only the first headline line has a blue box.
- [ ] The blue box is one line and does not clip or overflow.
- [ ] Supporting copy is readable and not overcrowded.
- [ ] Numbers and proof points are visually emphasized.
- [ ] The main visual has a clear purpose.
- [ ] Slide number and progress state are correct.
- [ ] No removed category eyebrow labels have been reintroduced.
- [ ] All slides have been rendered and visually inspected, not merely checked in code.
