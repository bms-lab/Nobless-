# NOBLESS design system: Deep Field v2 "Instrument"

The site should feel like a precise instrument: dark, calm, exact, with one living element (the Lattice). Every page follows this file; the same values live in `src/styles/global.css` as CSS variables. Pages use the names, never raw values.

Direction chosen from the project's own brief (`docs/15-master-strategy.json`: futuristic, premium, scientific, minimal; hairline grids, monospace-style labels, restrained blue, rare gold). It was not compared with a design-reference library in this pass.

## Color (dark only)

| Token | Value | Role |
|---|---|---|
| `--color-bg` | `#07080b` | Page background |
| `--color-bg-raised` | `#0d0f14` | Panels you can open: product, featured article, closing panel |
| `--color-bg-elevated` | `#14171f` | Rare: menus, overlays |
| `--color-line` | `#1d212c` | Hairlines between rows and cells |
| `--color-line-strong` | `#2f3545` | Outlines of buttons, chips, card hover |
| `--color-text` | `#eef0f4` | Headings and main text (17.5:1) |
| `--color-text-muted` | `#a3a9b8` | Body copy, leads (8.5:1) |
| `--color-text-faint` | `#7d8496` | Labels, meta (5.3:1, never under 4.5:1) |
| `--color-ion` | `#8cc8ff` | The one accent: links, focus ring, section numbers, the "now" marker |
| `--color-ion-strong` | `#b8ddff` | Hover of ion and of the primary button |
| `--color-aurum` | `#d6be8a` | Rare: the eyebrow at the top of a page, "in exploration" dot |
| `--color-success` / `--color-danger` | `#7bd9a6` / `#ff8a8a` | Live status, published fact / form errors |

No gradients as decoration, no purple, no glass. Gradients only fade lines and dot grids.

## Typography

One family for all three languages: **Readex Pro** (variable weight + HEXP width axis, Latin and Arabic). Headings are light (300; 400 in Arabic) and widen slightly with HEXP; Arabic never uses letter-spacing or uppercase.

| Token | Size | Use |
|---|---|---|
| `--text-display` | 48 → 120px | Home hero only |
| `--text-h1` | 40 → 80px | Page titles, big statements |
| `--text-h2` | 30 → 52px | Section titles, principle names |
| `--text-h3` | 20 → 28px | Steps, article subheads, list titles |
| `--text-body-lg` | 18 → 20px | Leads and article text |
| `--text-body` | 16 → 17px | Body |
| `--text-small` | 14px | Meta, table of contents |
| `--text-label` | 11.5 → 12.5px | Tracked uppercase labels (Latin), 14px plain in Arabic |

Line length: prose capped at `--measure` (66ch).

## Spacing

8-based scale `--space-1` (4px) to `--space-10` (128px). Sections use `--section-y` (72 → 136px). Content width `--maxw` 1280px with `--gutter` 16 → 64px.

## Shape and depth

Radius: `--radius-sm` 6px, `--radius-md` 14px (cards), `--radius-lg` 22px (feature panels), `--radius-pill` (buttons, chips, status). No shadows: depth comes from surface color and hairlines.

## Components

- **Section index**: `01  The house` in labels, number in ion, hairline to the edge. Every home section starts with one.
- **Buttons**: primary (white, one per view), secondary (outline), quiet (ion text with arrow). Hover: ion-tinted; focus: 2px ion ring; disabled: 45% opacity.
- **Ledger**: numbered rows with large titles and a hairline that fills with ion on hover (principles).
- **Product card**: wide panel, symbol tile, status pill, name in wide light caps, plus the **Stage track** (Now / Next / Later), where only the current stage and the one committed next step are named.
- **Process**: four numbered steps on one line (vertical on phones), the first marker filled.
- **Journal**: featured latest article panel, then rows (date, title, category, reading time); status tags: fact (green), work in progress (ion), plan (gold ring).
- **Article**: category eyebrow, title, excerpt, meta row (date, reading time, status, other languages), sticky table of contents on desktop, reading progress line.
- **Footer**: links, then the NOBLESS wordmark as a hairline outline across the full width.

## Imagery and motion

No photos, no stock, no illustrations of people (faceless brand). The only images are the logo symbol and the Lattice (points that settle into the symbol). Motion is slow and purposeful: headline settle, reveal on scroll, pointer dot field, the "now" marker breathing. Everything is static with reduced motion.

## Rules that do not bend

The logo is fixed (Soft Cut N) and never mirrored in Arabic. Three principles only: Honesty, Innovation, Accessibility. No invented numbers, customers, dates or people.
