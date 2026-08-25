# Hers Batik Brand Spotlight — Development Notes

## Project objective

Create a six-slide Local Icons brand spotlight for Hers Batik at `1080 × 1350px`, exported as PNG at `2160 × 2700px`.

The carousel should feel editorial, contemporary, and fashion-led while remaining recognizably part of the Local Icons campaign system.

## Non-negotiable requirements

- Preserve the approved Local Icons lockup and show-mark order.
- Use only the copy supplied or explicitly revised by the user.
- Do not add invented headlines, captions, product names, or promotional claims.
- Do not use batik textures around the slide edges.
- Do not overlap primary text or logos with photography or other primary content blocks.
- Maintain at least `32px` of visible separation; prefer `48–72px` between major elements.
- Render PNG only.
- Reuse the Lily's Pearl QR code and `s.id/Localicons-2026` link on the closing slide.

## Visual direction

The selected direction combines the clean Local Icons framework with large editorial fashion photography. White and warm-cream backgrounds provide breathing room, while teal, purple, blue, and yellow remain restrained campaign accents.

Rounded photo cards and soft shadows connect the product imagery to the existing Local Icons visual language. The clothing remains the main focus; decorative circles stay outside critical content areas.

## Slide decisions

### Slide 1 — Cover

- Uses the Hers logo and blue batik fashion photograph.
- The logo is cropped non-destructively through CSS because its source image contains substantial white space.
- The logo was reduced to prevent contact with the photograph.
- The photograph was reduced from the previous source size to `410 × 830px`.
- The statement uses a forced line break before `ini` to prevent overlap and create a clear visual gap.
- The supplied `geser` cue and arrow icon sit at the bottom center, separated from the main composition.

### Slide 2 — Brand statement

- Uses the natural-light navy batik photograph.
- Copy remains exactly as approved, with only the requested capitalization:
  - `Comes with stamped batik concept and using eco friendly materials`
  - `Bring Indonesian heritage with modern & unique touch`
- The photo and copy use separate columns with visible spacing.

### Slide 3 — Sateen product showcase

- Contains product photography only, apart from the required Local Icons lockup.
- No `Produk Hers Batik` title or added showcase copy.
- Uses brown, green, and black sateen looks in an asymmetric three-photo composition.

### Slide 4 — Batik product showcase

- Contains product photography only, apart from the required Local Icons lockup.
- No `Produk Hers Batik` title or added showcase copy.
- Uses blue-white, red-black, and red batik looks.
- The photo composition was moved upward after removing the title.

### Slide 5 — Offers

- Uses two product-led offer cards.
- Current approved copy:
  - `-Discount All Dress Sateen Sale From 500k now only 250k`
  - `All Batik Discount 10%`
- The original price is struck through; the new price and percentage receive color emphasis without changing the wording.

### Slide 6 — Event CTA

- Uses the stacked Local Icons lockup.
- Current event copy:
  - `Where Local Becomes Iconic`
  - `17-19 September 2026`
  - `at Hall B, JICC Senayan`
- Reuses the same QR asset and `s.id/Localicons-2026` link as the Lily's Pearl campaign.
- No batik texture is used around the edges.

## Asset selection

- `batik-navy-sky.jpeg`: slide 1 cover.
- `batik-navy-sun.jpeg`: slide 2 statement.
- `sateen-brown.jpeg`, `sateen-green-close.jpeg`, `sateen-black.jpeg`: slide 3.
- `batik-blue-white.jpeg`, `batik-red-black.jpeg`, `batik-red.jpeg`: slide 4.
- `sateen-green-full.jpeg`, `batik-red-black.jpeg`: slide 5.
- `logo-hers.jpeg`: slide 1 brand mark.
- `swipe-left.png`: slide 1 swipe cue.
- `qr-localicons-2026.png`: slide 6 CTA.

## QA notes

- All six slides render successfully at `2160 × 2700px`.
- The current deliverables are PNG files.
- Slide 1 has been checked for separation between the logo, statement, and cover photo.
- Slides 3 and 4 have been checked after removing their titles and recomposing the photographs.
- Slide 2 and slide 5 have been checked after their latest copy revisions.

## Working files

- Slide source: `slides/slide-01.html` through `slides/slide-06.html`
- Campaign styling: `slides/campaign.css`
- Approved copy record: `content/story.json`
- Source media: `assets/`
- Final PNG output: `rendered/`
