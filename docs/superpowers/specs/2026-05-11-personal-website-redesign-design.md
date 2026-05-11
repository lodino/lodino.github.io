# Personal Website Redesign Design

## Goal

Rebuild the homepage of `lodino.github.io` into a clean, compact, professional AI researcher profile while preserving the existing information: bio, contact links, education background, selected publications, news, and service.

## Visual Direction

Use a restrained two-column academic layout:

- Left identity rail with portrait, name, role, affiliation, and contact links.
- Wide main column with concise bio, selected publications, recent news, and service.
- No oversized hero headline.
- Small, readable typography with generous line height.
- Warm off-white background, dark readable text, muted teal links, and subtle beige dividers.
- Beauty should come from spacing, alignment, and publication hierarchy rather than gradients, large type, animations, or decorative cards.

## Content Model

Homepage content should migrate all current top-level information from `_pages/about.md`:

- Ph.D. student in Data Science at UC San Diego.
- Advisor: Prof. Babak Salimi.
- Prior education: Xi'an Jiaotong University B.Eng. and UC San Diego M.S.
- Research interests: data-centric approaches for trustworthy ML, including robustness, fairness, explainability, and data quality.
- Recent news items from the current homepage.
- Service list from the current homepage.

Selected publications should be pulled from the existing `_publications` collection and shown prominently on the homepage. The full publications page remains available at `/publications/`.

## Architecture

Add a dedicated Jekyll layout for the homepage so the redesign does not disturb existing publication detail pages, archive pages, or the inherited Minimal Mistakes theme. Add a focused Sass partial for homepage styling and import it from `assets/css/main.scss`.

## Responsive Behavior

Desktop and tablet use two columns. Mobile collapses to a single column with the portrait and identity first, followed by bio, selected publications, news, and service. Text must remain readable without horizontal scrolling.

## Quality Requirements

- Preserve existing links to Google Scholar, GitHub, LinkedIn, email, publication pages, and external paper links where available.
- Use semantic HTML sections and accessible image alt text.
- Avoid over-fancy visual treatments.
- Build successfully with Jekyll.
- Provide a local preview URL after implementation.
