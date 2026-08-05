# Global Sources Carousel Library

An HTML/CSS carousel design library organized by brand and campaign. Each campaign owns its slide markup, content, local brand assets, and rendered output while reusing the shared Global Sources design system.

## Repository structure

```text
Carousel-Generator-2/
|-- carousels/
|   `-- niceso/
|       `-- brand-origin/
|           |-- assets/       # Campaign-specific images and logos
|           |-- content/      # Story copy and content data
|           |-- slides/       # Editable HTML slides
|           `-- rendered/     # Generated PNG/JPG files
|-- shared/
|   |-- assets/               # Global Sources logos and shared textures
|   `-- styles/               # Reusable design system
|-- scripts/
|   `-- render.mjs            # Campaign-aware Playwright renderer
|-- design.md                 # Design ground rules and QA checklist
|-- package.json
`-- README.md
```

## Included campaign

The current campaign is:

```text
carousels/niceso/brand-origin
```

It contains four 1080 x 1350 Instagram carousel slides and their verified PNG exports.

## First-time setup

Install Node.js, then run:

```powershell
npm install
```

The renderer uses Google Chrome or Microsoft Edge when available. Playwright Chromium can also be installed with:

```powershell
npx playwright install chromium
```

## Render the NICE SO campaign

```powershell
npm run render:png
```

For JPG output:

```powershell
npm run render:jpg
```

## Render another campaign

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
