# Local Icons Carousel Design — Draft

> Status: working draft for social carousel production. This guide translates the current Local Icons introduction carousel and the supplied `LI - KV 1x1-01.jpg` key visual into a repeatable visual system. It supplements the repository-level `design.md`; where the two differ on campaign styling, this Local Icons guide takes precedence.

## 1. Creative direction

Local Icons should feel like a contemporary Indonesian discovery platform: bold, optimistic, social-first, and easy to scan. The design combines a clean editorial base with playful color and large, confident typography.

The intended impression is:

- **Local pride without heritage clichés** — celebrate modern Indonesian brands, creators, and products.
- **Youthful, not childish** — use bright colors and friendly shapes with disciplined spacing and typography.
- **Premium-accessible** — generous white space, sharp brand assets, and selective visual effects keep the work polished.
- **Digital and event-ready** — layouts should work for introductions, brand stories, product showcases, offers, schedules, and calls to action.

Avoid a conventional corporate-event look, crowded trade-show graphics, or decorative elements that do not support the message.

## 2. Reference hierarchy

Use references in this order:

1. Approved Local Icons logo assets in the relevant carousel `assets/` folder.
2. The supplied Local Icons key visual for brand mood, color, shape language, and event lockup behavior.
3. `introduction-2026` for the core carousel layout system.
4. `brand-spotlight` for photo-led brand stories, offers, and closing slides.
5. The repository-level `design.md` for production, file structure, and general export QA.

Rendered PNGs are visual references only. Edit the HTML, CSS, JSON, SVG, and source images instead of editing rendered output.

### Campaign development notes

Before creating, editing, or rendering any slide, inspect the campaign's `thoughts.md` file first. Read it completely to understand the established design steps, approved direction, copy constraints, asset selection, layout decisions, revision history, and outstanding QA items.

- Treat `thoughts.md` as the campaign-specific development log and use it together with this design guide.
- The user's latest explicit instruction always takes precedence over older notes in `thoughts.md`.
- Confirm that the planned change is consistent with the recorded spacing, branding, copy, and output requirements before modifying slide files.
- Update `thoughts.md` after a material design or content change so the next development pass starts from accurate information.
- If a campaign does not yet contain `thoughts.md`, create it before substantial slide development begins.

## 3. Format and safe area

- Design at `1080 × 1350px` in a `4:5` portrait ratio.
- Export at `2160 × 2700px` unless another delivery size is requested.
- Use `72px` left and right as the default text-safe margin.
- Use approximately `62–72px` top padding and `68–76px` bottom padding.
- Keep the Local Icons lockup, headline, copy, and main visual on a shared alignment axis.
- Decorative shapes may bleed beyond the canvas; important text, logos, faces, products, dates, and CTAs may not.
- Leave deliberate breathing room around the logo. Do not let a headline, card, or photograph appear attached to it.
- Do not overlap primary text or logos with photographs, cards, or other primary content blocks. Maintain at least `32px` of clearly visible separation at the `1080px` working size; prefer `48–72px` between major elements when space permits. If the gap is unclear, add a line break, reduce the type or image size, or reposition the elements before rendering.

The design should remain legible in an Instagram feed without zooming. If a slide needs more than one reading pass, reduce the copy or split the information across slides.

## 4. Core color system

The key visual and current carousel establish five main colors. Use white as the dominant field, black for hierarchy, and the four bright colors as modular accents.

| Role | Token | Working value | Use |
| --- | --- | --- | --- |
| Canvas | `--paper` | `#FFFFFF` | Primary background and negative space |
| Primary text | `--ink` | `#22211D` | Headlines, body copy, dark pills |
| Local Icons teal | `--teal` | `#00C5B2` to `#00CBB7` | Lead brand accent, cards, corner forms |
| Teal shadow | `--teal-deep` | `#009F8C` | Subtle depth in gradients only |
| Purple | `--purple` | `#7952F5` to `#8057F4` | Secondary brand accent, cards, corner forms |
| Blue | `--blue` | `#268CFF` | Supporting accent, gradient transitions |
| Yellow | `--yellow` | `#FFCA22` | Warm accent, highlights, small graphic moments |
| Warm cream | `--cream` | `#FFF9ED` | Optional photo-led or offer background |

### Color rules

- Keep roughly `65–80%` of a standard information slide white or near-white.
- Use black for the strongest typographic message; use color to organize rather than recolor every word.
- A slide may feature one dominant accent plus one supporting accent. All four bright colors do not need equal weight on every slide.
- Teal and purple are the primary brand pair. Blue and yellow create rhythm and contrast.
- The approved teal → blue → purple gradient may be used for short rules, hashtags, or small emphasis elements.
- Do not use red as a Local Icons accent. Red may appear only inside the supplied Global Sources show marks or an approved featured-brand asset.
- Check white text on colored cards at phone size. When contrast is uncertain, use `--ink` on yellow and white on teal, blue, or purple.

## 5. Shape language

The key visual uses large, soft, inflated organic forms that enter from the edges of the frame. The carousel may simplify these to circles or broad cropped ellipses while preserving the same visual behavior.

### Primary forms

- Place large teal and purple forms near the top corners.
- Place yellow and blue forms near the bottom corners or lower edge.
- Crop at least `35%` of a large edge form outside the canvas so it reads as atmosphere, not a sticker.
- Use subtle gradient shading when recreating the dimensional key-visual look. Flat color is acceptable for dense information slides.
- Keep the center of the canvas calm and bright so the message remains dominant.

### Secondary forms

- Small dots, rounded squares, rings, and short gradient rules may guide the eye or label a list.
- Corners should be generous: approximately `25–40px` for cards and fully rounded for pills.
- Use a slight rotation on isolated product placeholders or accent tiles only when it adds energy.
- Avoid mixing hard polygons, thin technical line art, and unrelated illustration styles with the soft Local Icons geometry.

### Depth

- Use restrained shadows on white cards: soft, wide, and low-opacity.
- Use depth on edge shapes sparingly; the reference key visual feels dimensional but still clean.
- Do not apply heavy drop shadows to headlines or official logos.

## 6. Typography

Use Gotham where available, with `Arial` or a close geometric sans-serif only as a fallback. The system relies on weight and scale rather than multiple typefaces.

| Element | Recommended treatment |
| --- | --- |
| Main headline | Gotham Black / `900`, uppercase, `64–92px`, line-height `0.90–0.98`, tracking around `-0.055em` |
| Cover tagline | Gotham Black / `900`, sentence or title case, `40–54px` |
| Section intro | Gotham Bold / `700`, `27–34px`, line-height `1.25–1.35` |
| Card title | Gotham Black / `900`, `22–30px` |
| Body copy | Gotham Book / `400–500`, `19–27px`, line-height `1.32–1.45` |
| CTA or pill | Gotham Bold/Black, `22–34px` |

### Headline rules

- Keep headlines short and poster-like. Use intentional line breaks.
- Prefer one to three lines with no more than about four words per line.
- Use uppercase for section titles such as `WHAT IS LOCAL ICONS?`, `MEET THE ICONS`, and `SPECIAL OFFER`.
- The campaign statement `Where Local Becomes Iconic.` may use title case because it functions as a brand line.
- Do not stretch, outline, bevel, or add shadows to type.
- Do not shrink body copy below `19px` to make excess copy fit; edit the copy instead.

### Voice and language

- Use concise, conversational Indonesian with selective English phrases already natural to the audience.
- Sound confident and culturally current, not forced or overly slang-heavy.
- Keep capitalization and punctuation consistent across a carousel.
- Use bold emphasis for the key phrase, benefit, offer value, date, or location—not for every sentence.

## 7. Logo and co-branding

### Local Icons lockup

- Use an approved Local Icons SVG: horizontal for most headers and stacked/vertical for centered covers or closing slides.
- Keep the artwork intact. Do not redraw the icon, retype the wordmark, recolor individual letters, or separate the `LOCAL` and `ICONS` elements.
- Preserve the gold square detail inside the Local Icons symbol.
- Prefer the dark lockup on white or cream. Use a supplied light version only on a sufficiently dark background.
- Keep the logo optically level and give it clear space of at least the height of the gold square on all sides.

### Global Sources relationship

- Use the approved co-branded lockup containing `Presented by: Global Sources` and the three Indonesia pavilion show marks when the campaign requires event attribution.
- Preserve the show order: Electronics → Home Appliances → Gifts & Home.
- Never reconstruct or retype the Global Sources or show logos from the key visual.
- On a cover, the co-brand may be prominent. On interior slides, keep it in a consistent header position and let the content headline lead.
- Featured-brand logos should never appear larger than the Local Icons identity unless the slide is explicitly a product or brand showcase.

## 8. Key visual usage

The supplied square key visual is the source for event mood and campaign framing, not a universal background for every carousel slide.

### What to carry forward

- A bright white center with an event or crowd image washed back behind it.
- Large teal, purple, blue, and yellow soft forms entering from the edges.
- Oversized black statement typography.
- A black rounded date pill with white type.
- Clear hierarchy: Local Icons identity → proposition → date → venue.

### How to use it in carousels

- Rebuild the layout natively for `4:5`; do not simply crop the square artwork.
- If the crowd or venue image is used, apply a strong white veil so it supports rather than competes with type. A working target is `8–20%` apparent image contrast.
- Protect faces and recognizable product details from headline overlap when they are meant to be seen.
- Use event details as a compact block near the lower third, with the date in the strongest pill.
- Keep venue copy outside the date pill unless the composition is extremely simple.
- Do not repeat the full key-visual lockup on every slide. Use it for the launch cover, event reminder, or closing CTA.

## 9. Layout system

Use one of four layout modes per slide.

### A. Identity cover

- Center or optically balance the primary Local Icons lockup.
- Place the campaign line below it with ample space.
- Use a single black pill for the swipe cue, date, or main CTA.
- Keep decorative corner forms large and cropped.

### B. Editorial information

- Use a consistent header lockup at the top.
- Place the headline below the header, followed by a short gradient rule.
- Use one clear content device: list, two-by-two card grid, timeline, quote, or comparison.
- Align all text and cards to the `72px` safe margin.

### C. Photo or product showcase

- Let approved photography occupy most of the composition.
- Use one hero image or a deliberate two-to-three-image collage; avoid a gallery of many equally small images.
- Use rounded photo cards with thin light borders and soft shadows.
- Keep product color accurate and avoid gradients over the product itself.
- Add only a short label or statement when the image already carries the story.

### D. Closing or event CTA

- Center the statement, date, venue, and CTA.
- Use the vertical Local Icons lockup when it improves balance.
- Repeat the four-color edge framing from the cover to create closure.
- Give the date or hashtag one dominant pill treatment; do not stack multiple competing pills.

## 10. Components

### Accent rule

- Use a short `108–145px` rounded rule beneath section headlines.
- Preferred gradient: teal → blue → purple.
- Treat it as a navigation cue, not a divider spanning the full page.

### Cards

- Default: white fill, `1px` neutral border, `25–38px` radius, soft shadow.
- Colored cards: solid teal or purple with white text; blue may be used selectively.
- Yellow is best as a top border, label, small shape, or pale card field rather than a full dense text card.
- Keep internal padding between `24–44px` depending on card size.
- Maintain equal heights inside grids unless the asymmetry is deliberately photo-led.

### Pills

- Use `--ink` with white type for dates, swipe cues, and primary actions.
- Use the campaign gradient for hashtags or secondary digital CTAs.
- Keep pill copy to one line and center it vertically.
- Do not use more than two pills on one slide.

### Icons

- Prefer a consistent custom SVG or approved icon set.
- Emoji are acceptable only in an intentionally casual introduction draft; replace them for final polished event materials if suitable assets exist.
- Keep icon rendering consistent in size and visual weight across a grid.

### Lists

- Use white rounded rows with one colored marker per item.
- Keep each item to one or two short lines.
- Alternate marker colors with purpose; do not imply categories unless the colors are explained.

## 11. Photography and featured brands

- Use authentic product, creator, founder, booth, or event imagery with clear subject focus.
- Favor bright, clean photography that can coexist with the white canvas and color system.
- Crop around the story: face, product detail, interaction, or environment. Avoid arbitrary center crops.
- Do not distort logos, packaging, jewelry, clothing, or product proportions.
- A featured brand may introduce its own colors and visual texture, but retain at least two Local Icons anchors: the official lockup, campaign typography, corner forms, accent rule, or closing frame.
- For premium brands, reduce the number of bright forms and allow cream, material texture, and photography to lead.
- For offer slides, make the value and qualifying condition readable without relying on the image.

## 12. Carousel rhythm

A six-slide Local Icons introduction should generally follow this arc:

1. **Identity / hook** — introduce Local Icons and the campaign line.
2. **Audience recognition** — help the viewer see themselves in the event.
3. **Definition** — explain what Local Icons is and what happens there.
4. **Discovery** — show brands, products, or creators with real imagery.
5. **Reasons to attend** — translate features into concrete benefits.
6. **Event CTA** — restate the promise and surface date, venue, follow action, or registration path.

Use variation across the sequence: alternate between open typographic slides, structured cards, and photography. Do not repeat the same two-by-two grid on consecutive slides.

## 13. Draft-to-final priorities

Before treating the current introduction carousel as final:

- Replace product placeholders on `MEET THE ICONS` with approved product or brand imagery.
- Confirm whether the co-branded Local Icons lockup in the introduction assets is the final approved master.
- Confirm the final event date and exact venue spelling before adding them to a CTA slide.
- Replace mixed emoji with a consistent icon family if the carousel is used as a paid or official launch asset.
- Check long English headlines for optical fit; line breaks should feel intentional rather than squeezed.
- Add consistent slide numbering or progress cues if required by the publishing template.
- Confirm final Instagram CTA wording and destination before rendering QR codes or registration prompts.

## 14. Production tokens

Use these as a starting point for new Local Icons campaigns. Campaign CSS may refine them, but should not silently redefine the brand palette.

```css
:root {
  --li-paper: #ffffff;
  --li-cream: #fff9ed;
  --li-ink: #22211d;
  --li-teal: #00c5b2;
  --li-teal-deep: #009f8c;
  --li-purple: #7952f5;
  --li-blue: #268cff;
  --li-yellow: #ffca22;

  --li-canvas-w: 1080px;
  --li-canvas-h: 1350px;
  --li-safe-x: 72px;
  --li-radius-card: 30px;
  --li-shadow-card: 0 15px 38px rgba(34, 33, 29, 0.09);
  --li-accent-gradient: linear-gradient(90deg, var(--li-teal), var(--li-blue), var(--li-purple));
}
```

## 15. Final QA checklist

- [ ] The campaign's `thoughts.md` was inspected before development and updated after material changes.
- [ ] Canvas is `1080 × 1350px`; exported artwork is sharp.
- [ ] Important content stays inside the text-safe area.
- [ ] The approved Local Icons lockup is used without alteration.
- [ ] Global Sources and the three show marks are intact, in the approved order, and legible.
- [ ] The logo has clear space and aligns with the main composition.
- [ ] Primary text and logos do not overlap photographs or other primary content blocks, with at least `32px` of visible separation and preferably `48–72px` between major elements.
- [ ] White remains the dominant field on standard information slides.
- [ ] Teal and purple lead the accent system; blue and yellow support it.
- [ ] Edge shapes are intentionally cropped and do not obstruct content.
- [ ] Headline line breaks are deliberate and readable at phone size.
- [ ] Body copy is concise and no smaller than `19px`.
- [ ] Cards use consistent padding, radii, borders, and shadows.
- [ ] Colored cards meet contrast requirements.
- [ ] Product placeholders, draft copy, and temporary emoji have been resolved.
- [ ] Featured-brand assets are not distorted or recolored.
- [ ] Date, venue, offer conditions, CTA, and QR destination are verified.
- [ ] The six-slide sequence varies its layout while retaining a coherent visual rhythm.
- [ ] Every slide has been rendered and visually inspected before delivery.
