# NOBLESS Homepage Visual Redesign Implementation Plan

> **For agentic workers:** Use the host's available task-by-task implementation workflow. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the NOBLESS homepage into a premium, monochrome, frontier-technology experience across English, French, and Arabic while keeping LYMI as the only featured public product.

**Architecture:** The repository currently contains a static exported site with localized HTML and hashed Astro assets, but no visible Astro source tree or package manifest. Implement this phase as a tightly scoped static-site change on `nobless-redesign`: add a reusable monochrome terrain SVG, add page-scoped styles and hero composition to each localized homepage, preserve existing shared CSS and scripts, and verify links, RTL, reduced motion, and deployment. If the original source project is later found, migrate these changes back into source before future redesign work.

**Tech Stack:** Static HTML, CSS, inline SVG, lightweight vanilla JavaScript already present, GitHub branch workflow, Vercel Preview deployments.

## Global Constraints

- Use a distinct NOBLESS identity; inspiration from xAI is limited to visual restraint, confidence, typography, and whitespace. Do not copy logos, copy, or proprietary assets.
- Keep the palette monochrome: near-black, white, and restrained greys.
- Use monochrome terrain as the main signature; use topographic lines, grain, paper/felt texture, and subtle glass as accents. Avoid visual clutter and excessive glow.
- LYMI remains the only publicly featured product on the homepage.
- Do not invent customers, metrics, awards, funding, team size, or product capabilities.
- Maintain equivalent EN / FR / AR messaging and correct Arabic RTL.
- Respect `prefers-reduced-motion`, keyboard access, responsive layouts, semantic structure, and contrast.
- All changes remain on `nobless-redesign`; do not merge into `main` without explicit approval.

---

### Task 1: Create the NOBLESS monochrome terrain artwork

**Files:**
- Create: `media/nobless-monochrome-terrain.svg`

**Interfaces:**
- Consumes: none.
- Produces: a responsive, monochrome terrain image usable as a decorative hero background via `background-image`.

- [ ] **Step 1: Add the asset**
  Create a scalable SVG with layered grayscale terrain, topographic contour lines, and restrained procedural grain. Keep all artwork self-contained; no external fonts, images, or scripts.

- [ ] **Step 2: Verify the asset source**
  Confirm the SVG includes a viewBox, no external references, no embedded scripts, and only grayscale fills/strokes.

- [ ] **Step 3: Commit the asset**
  The asset is committed independently on the feature branch.

### Task 2: Redesign the English homepage hero and visual rhythm

**Files:**
- Modify: `en/index.html`
- Modify: `media/nobless-monochrome-terrain.svg` only if the visual verification finds a concrete defect.

**Interfaces:**
- Consumes: `/media/nobless-monochrome-terrain.svg`, existing `.wrap`, `.hero`, `.btn`, `.reveal` classes and the existing NOBLESS navigation.
- Produces: a hero with clear NOBLESS positioning, a prominent LYMI path, terrain artwork, and page-scoped responsive styles.

- [ ] **Step 1: Add focused static checks**
  Check the homepage for the new headline, a single LYMI product link, valid hero artwork path, no unsupported numerical claims, and the reduced-motion CSS rule.

- [ ] **Step 2: Verify the checks fail before implementation**
  Run the static checks against the current page and confirm the new headline/artwork checks fail.

- [ ] **Step 3: Implement the hero**
  Replace the generic particle-logo hero emphasis with a layered monochrome terrain composition, editorial headline, short factual description, and a direct LYMI action. Retain a restrained secondary company/contact action. Add subtle grain/topographic detailing through CSS; do not add heavyweight libraries.

- [ ] **Step 4: Verify focused checks**
  Run static checks and confirm the headline, CTA, asset path, single product presence, semantic headings, and reduced-motion rules pass.

- [ ] **Step 5: Verify the page integration**
  Confirm navigation targets remain valid, existing product film/page links still work, and no unrelated sections or footer links were removed.

- [ ] **Step 6: Commit the passing English homepage**
  Commit only `en/index.html` with a focused message.

### Task 3: Localize and implement French and Arabic homepages

**Files:**
- Modify: `fr/index.html`
- Modify: `ar/index.html`

**Interfaces:**
- Consumes: the English hero structure and `/media/nobless-monochrome-terrain.svg`.
- Produces: equivalent localized homepage experience with correct RTL direction and language-specific copy.

- [ ] **Step 1: Add focused localization checks**
  Assert French and Arabic localized headline, product CTA, image path, exactly one LYMI product feature, and correct document direction (`ltr` for French; `rtl` for Arabic).

- [ ] **Step 2: Verify the relevant checks fail**
  Run the checks against existing pages and confirm the new localized headline/artwork checks fail.

- [ ] **Step 3: Implement localized pages**
  Match the English composition and responsive rules. Localize every new visible label and action. Ensure the hero artwork does not overlap Arabic text and navigation remains RTL.

- [ ] **Step 4: Verify focused checks**
  Run the localization assertions and inspect RTL-sensitive selectors and button order.

- [ ] **Step 5: Verify integration**
  Confirm all three language switchers link to their matching homepage paths and all product links point to the LYMI detail page.

- [ ] **Step 6: Commit the localized homepages**
  Commit `fr/index.html` and `ar/index.html` together.

### Task 4: Run release checks and verify Vercel Preview

**Files:**
- Test: `en/index.html`, `fr/index.html`, `ar/index.html`, `media/nobless-monochrome-terrain.svg`

**Interfaces:**
- Consumes: all three localized homepages and the shared SVG.
- Produces: verified feature-branch changes and a Vercel Preview URL/status for founder review.

- [ ] **Step 1: Run static validation**
  Parse each HTML file, verify all referenced local hero assets exist, check language/direction attributes, ensure each homepage has exactly one public product feature (LYMI), and confirm the reduced-motion CSS rule is present.

- [ ] **Step 2: Run link and accessibility checks**
  Verify all homepage internal hrefs resolve to files or valid external URLs; check heading hierarchy, descriptive link labels, keyboard-visible focus inherited from the site styles, and adequate text contrast.

- [ ] **Step 3: Push/commit only on the feature branch**
  Confirm the working branch is `nobless-redesign` and `main` is unchanged.

- [ ] **Step 4: Verify Vercel Preview**
  Inspect the GitHub commit/deployment status. Confirm the preview deployment is ready and test EN, FR, AR routes at desktop and mobile widths.

- [ ] **Step 5: Report evidence**
  Provide the preview URL, exact commits, verification outcomes, and any remaining limitations. Do not claim production is updated.

## Unresolved implementation seam

The original Astro source project is not present in the inspected repository tree. This plan therefore targets the committed static export and keeps changes narrowly scoped. If the canonical source repository becomes available, the same hero design should be ported into the source components before the next broad site-wide redesign.
