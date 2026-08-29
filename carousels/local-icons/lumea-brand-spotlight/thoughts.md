# Lumea Brand Spotlight — Development Notes

## Objective

Create a four-slide Local Icons Brand Spotlight carousel for Lumea at `1080 × 1350px`, exported as sharp PNG files at `2160 × 2700px`.

## Pre-build audit

- The campaign follows the latest Local Icons Brand Spotlight structure: branded cover, one story slide, and two product-led showcase slides.
- The supplied copy is retained exactly; no headline, product claim, CTA, specification, or inferred product name is added.
- The Lumea logo source is a clean square asset with generous white space and is suitable for a contained logo window.
- `mug-lifestyle.png` and `pantry-containers.png` contain screenshot UI artifacts. They may only be used with crops that fully exclude the top-right close control and the bottom marketplace badge.
- `handled-bowls.jpg`, `olive-bin.jpg`, `egg-organizers.jpeg`, and `food-storage-trays.jpg` are clean enough to lead the product showcase slides.
- `food-storage-trays.jpg` is the lowest-resolution source at `720 × 713px`; it should remain a supporting image rather than a full-canvas hero.

## Visual direction

Warm lifestyle editorial: soft cream fields, Lumea brown and olive as the featured-brand palette, and restrained Local Icons teal, purple, blue, and yellow edge accents. Rounded photography cards, generous white space, and quiet shadows make ordinary household objects feel curated and lifestyle-oriented.

## Slide plan

### Slide 1 — Cover

- Local Icons horizontal lockup at the top.
- Exact `BRAND SPOTLIGHT` label, supplied Lumea logo, and exact hook.
- Mug lifestyle image cropped into a tall hero card with the screenshot close control excluded.

### Slide 2 — Brand story

- Exact supplied paragraph, unchanged.
- Key phrases receive typographic emphasis only.
- Pantry-container image forms a narrow lifestyle anchor; both screenshot overlays are cropped away.

### Slide 3 — Product showcase

- Product imagery only, apart from the required Local Icons lockup.
- Handled bowls form the main frame, balanced by the olive household bin.

### Slide 4 — Product showcase

- Product imagery only, apart from the required Local Icons lockup.
- Egg organizers lead the layout; food-storage trays and pantry containers support the finale.

## QA checklist

- [x] All four slides render successfully at `2160 × 2700px`.
- [x] Supplied copy matches `content/story.json` and the user brief exactly.
- [x] Screenshot controls and marketplace badges are absent from the visible crops.
- [x] Images preserve original proportions and color.
- [x] Important content stays inside the safe area.
- [x] Primary content blocks do not overlap.
- [x] Every rendered slide is visually inspected.

## Revision log

- Audited the current Local Icons system, the latest completed Brand Spotlight campaign, and all seven supplied Lumea assets before development.
- Established the warm cream, brown, and olive visual direction and mapped clean versus crop-restricted image usage.
- First render QA found clipped baked-in product labels on Slide 4. The layout was revised from a tall hero crop to a wide hero with two supporting cards, removing the distracting label fragments and keeping the low-resolution food-storage image appropriately sized.
- A second Slide 4 crop check still exposed a partial `Tingkat` label; the egg-organizer image was changed to an intentional uncropped presentation inside the wide hero card so its embedded labels remain complete.
- Final renders were checked at `2160 × 2700px`; all four slides pass copy, crop, spacing, proportion, and artifact QA.
- Replaced the original egg-organizer source with the user-supplied clean `egg-organizers.jpg`, which contains no logo or feature-label boxes. Restored a full-bleed wide hero crop on Slide 4.
- Audited the Slide 2 and Slide 3 image orientations after user feedback. The narrow portrait crops hid most of the pantry set, abstracted the olive bin, and clipped the handled bowls. Slide 2 was rebuilt as a full-width story card above a horizontal pantry image; Slide 3 was rebuilt as two stacked horizontal frames with contained, uncropped product photography.
- Revised Slide 3 again at the user's request: the two horizontal contained-image frames were replaced with staggered `520 × 520px` square cards. Both near-square sources now fill their boxes edge-to-edge without internal empty space, distortion, or product obstruction.
- Replaced the obstructed mug photograph on Slide 1 with `olive-bin.jpg`, selected because its centered vertical product silhouette is the strongest fit for the existing portrait hero frame. The crop was retuned to preserve the bin's shape without additional scaling.
- Reduced and widened the Slide 1 hero card from `405 × 900px` to `430 × 720px`, giving the square source more horizontal field so the bin's right side and base remain visible.
- Shifted the Slide 1 bin focal position left within the photo frame to add breathing room along the product's right edge.
- Replaced the former header artwork on all four slides with the user-supplied `LOGO LI Use Horizontal.svg`; the approved `Indonesia Pavilions by` wording and pavilion marks embedded in the supplied SVG remain intact.
