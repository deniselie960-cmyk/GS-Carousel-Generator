# Global Sources Carousel Library

An HTML/CSS carousel design library organized by brand and campaign. Each campaign owns its slide markup, content, local brand assets, and rendered output while reusing the shared Global Sources design system.

## Repository structure

```text
GS-Carousel-Generator-main/
|-- carousels/
|   |-- eiger/
|   |   `-- brand-longevity/  # assets, content, slides, rendered
|   `-- niceso/
|       `-- brand-origin/     # assets, content, slides, rendered
|-- shared/
|   |-- assets/               # Global Sources logos and shared textures
|   `-- styles/               # Reusable design system
|-- scripts/
|   `-- render.mjs            # Campaign-aware Playwright renderer
|-- design.md                 # Design ground rules and QA checklist
|-- package.json
`-- README.md
```

## Included benchmark campaigns

Use these completed campaigns as references when building new carousels:

```text
carousels/niceso/brand-origin
carousels/eiger/brand-longevity
```

Both contain four 1080 x 1350 Instagram carousel slides and verified 2160 x 2700 PNG exports.

- **NICE SO** establishes the white-paper layouts, headline rhythm, charts, cards, and alignment modes.
- **Eiger** extends the system with alternating white/blue paper backgrounds, editorial photography, photo collages, yellow-on-blue headline emphasis, timelines, and centered conclusion diagrams.

## First-time setup

Install Node.js, then run:

```powershell
npm install
```

The renderer uses Google Chrome or Microsoft Edge when available. Playwright Chromium can also be installed with:

```powershell
npx playwright install chromium
```

## Render a campaign

Pass the campaign path after `--`:

```powershell
npm run render:png -- carousels/eiger/brand-longevity
```

Render NICE SO:

```powershell
npm run render:png -- carousels/niceso/brand-origin
```

For JPG output:

```powershell
npm run render:jpg -- carousels/eiger/brand-longevity
```

Running `npm run render:png` without a campaign path defaults to NICE SO.

## Direct renderer usage

Pass its path inside `carousels/`:

```powershell
node scripts/render.mjs --png carousels/brand-name/campaign-name
```

The renderer reads HTML files from that campaign's `slides/` directory and writes exports to its `rendered/` directory.

## Create another carousel

1. Copy the closest campaign folder.
2. Rename the brand and campaign directories.
3. Replace files in `assets/` and update `content/story.json`.
4. Edit the files in `slides/`.
5. Follow `design.md` for composition, spacing, typography, branding, and QA.
6. Render the complete campaign and inspect every exported image.

Shared rules belong in `shared/styles/system.css`. Campaign-only adjustments should stay inside the relevant slide HTML file.
