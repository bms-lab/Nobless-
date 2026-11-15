# NOBLESS Homepage Visual Redesign — Design Spec

Date: 2026-11-15
Status: Proposed for founder review
Target branch: `nobless-redesign`
Scope: Homepage first (EN / FR / AR); no production merge.

## 1. Objective

Reposition the NOBLESS homepage as a premium, globally credible technology group with the visual confidence and restraint associated with leading frontier-technology companies, while retaining a distinct NOBLESS identity. LYMI remains the only publicly featured product.

The page must communicate what NOBLESS is, what it builds, and where visitors should go next within the first screen.

## 2. Creative direction

Use an editorial monochrome system: near-black, warm white, restrained greys, precise typography, generous negative space, crisp grid alignment, and deliberate motion. Take inspiration from the clarity and restraint of xAI's visual language, without copying its logo, layouts, copy, or proprietary assets.

Visual ingredients are accents, not simultaneous decoration:
- Primary: monochrome landscapes / abstract terrain as the hero visual language.
- Secondary: subtle grain, noise, paper/felt texture, and topographic contour lines.
- Selective accents: frosted/liquid glass for a small number of interface surfaces; dithered or stippled gradients for depth; a restrained iridescent 3D object or lens-distortion moment only if it reinforces the hero concept.
- ASCII art may appear as a tiny technical detail, not as a dominant content treatment.
- Avoid colorful gradients, excessive glow, clutter, generic AI imagery, and effects that reduce legibility.

## 3. Homepage structure

1. Minimal global header: NOBLESS identity, concise navigation, language switcher, clear contact action.
2. Hero: one strong headline, one concise positioning statement, one primary action to LYMI, one secondary action for company/contact context, and one distinctive monochrome landscape/terrain composition.
3. Company thesis: explain NOBLESS as a technology group that designs, builds, and owns products and technology; avoid unsupported scale, traction, or research claims.
4. Featured product: LYMI only, with the existing product film and a clear path to the LYMI product page / lymi.io.
5. Principles: the five approved values — Honesty, Innovation, Accessibility, Excellence, Ownership — presented with strong editorial hierarchy rather than generic card clutter.
6. Closing contact statement and restrained footer.

Do not add invented products, customers, metrics, awards, funding, team size, or capabilities.

## 4. Localization and accessibility

- Maintain separate EN, FR, and AR homepages with equivalent meaning and localized copy.
- Preserve Arabic RTL layout and ensure the hero composition, navigation, buttons, and motion remain correct in RTL.
- Responsive layouts must work on mobile, tablet, and desktop.
- Respect `prefers-reduced-motion`; animation must not be required to understand the content.
- Maintain semantic headings, keyboard navigation, visible focus, sufficient contrast, and descriptive links.
- Keep visual effects lightweight and avoid large, unnecessary client-side dependencies.

## 5. Technical constraints and discovery

The current target branch appears to contain a static exported site: localized HTML pages, hashed `_astro` assets, and media, with no visible Astro source tree or package/build manifest at the repository root. Before implementation, identify whether the original source repository/build pipeline exists. Prefer editing the real source and regenerating the static output. If only the exported artifact is available, document that limitation and make the smallest maintainable change possible without pretending the source project is present.

The existing GitHub branch is connected to Vercel Preview deployments. All work for this phase stays on `nobless-redesign`; do not merge to `main` or alter production without explicit approval.

## 6. Acceptance criteria

- The first screen immediately communicates NOBLESS as a serious technology group and LYMI as its first public product.
- The visual result is recognizably NOBLESS, not a clone of xAI.
- The monochrome landscape / terrain visual is the central signature; textures and experimental effects remain restrained.
- EN / FR / AR content is consistent; Arabic RTL is verified.
- LYMI is the only product featured on the homepage.
- No unsupported business claims or fabricated statistics.
- Mobile and desktop layouts are usable; reduced-motion and keyboard accessibility are respected.
- Vercel Preview is generated successfully from the feature branch and checked before any production merge.

## 7. Out of scope for this phase

- Redesigning every internal page.
- Changing product functionality or LYMI itself.
- Adding new products or announcing unbuilt initiatives.
- Merging or deploying to production.
