# Global Sources Icon Carousel System

An HTML/CSS design system that renders fixed-size Instagram carousel slides using Playwright.

## Prototype

- Canvas: 1080 × 1350 px
- Typeface: locally installed Gotham family
- Theme: white paper texture with blue primary, yellow secondary, and dark editorial text
- Graphics: inline SVG icons and CSS-based diagrams
- Sample: four-slide NICE SO brand story

`assets/gs-logo-colour.png`, `assets/niceso-logo.png`, and `assets/paper-texture.jpg` are the supplied brand and texture assets. The full-colour Global Sources strip is used consistently on every slide.

## Render

Install Playwright in this folder, then run:

```powershell
npm install
npx playwright install chromium
npm run render:png
```

The renderer automatically uses Google Chrome or Microsoft Edge when available, so downloading Playwright's bundled Chromium is optional on Windows. Set `CAROUSEL_BROWSER` to override the browser executable.

Exports are written to `rendered/` at 2160 × 2700 physical pixels (2× scale).

To render JPG files instead:

```powershell
npm run render:jpg
```

## Editing

- Shared design tokens and components: `styles/system.css`
- Editable slide markup: `slides/slide-01.html` through `slide-04.html`
- Reusable copy source: `content/niceso-story.json`
- Renderer: `scripts/render.mjs`

The HTML slides can also be opened directly in a browser for quick previewing.
