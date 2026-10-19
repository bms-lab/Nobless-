# nobless.world

The NOBLESS company website in English, French and Arabic (right-to-left). It is a static site built with Astro 5. There is no database and no admin panel.

Live preview: https://noblessworld.vercel.app

## Folder tree
```
nobless-site/
├── src/
│   ├── pages/            One file per page. [lang] = en, fr, ar
│   │   ├── index.astro         / → sends visitors to their language
│   │   ├── 404.astro           page not found
│   │   ├── sitemap.xml.ts      sitemap (generated)
│   │   ├── robots.txt.ts       robots.txt (generated)
│   │   └── [lang]/             home, company, principles, products, journal, contact, privacy, legal
│   ├── i18n/strings.ts   ALL visible text, in the three languages
│   ├── data/
│   │   ├── site.json         settings (contact form key, email, hosting…)
│   │   ├── products/         one JSON file per product (NOBEON)
│   │   └── journal/          articles, one folder per article, one .md per language
│   ├── components/       header, footer, logo, product card, Lattice animation
│   ├── layouts/Base.astro  page frame: <head>, SEO tags, header, footer
│   ├── lib/content.ts    reads products and articles
│   ├── brand/symbol.svg  the logo symbol
│   └── styles/global.css colors, font, spacing, pointer field (Deep Field tokens)
├── public/               favicon, share image (og.png)
├── scripts/check-site.mjs  checks links, titles, h1, languages
├── vercel.json           Vercel settings: build, security headers, redirects
├── astro.config.mjs      site address (SITE_URL)
├── .env.example          the one variable the site uses (no secrets)
└── package.json          commands and dependencies
```

## What goes in GitHub, and what never does
- **Commit:** everything above, including `package-lock.json`.
- **Never commit:** `node_modules/`, `dist/`, `.astro/`, `.env` (all listed in `.gitignore`). There are no secrets in this project; the Web3Forms key is public by design.

## Commands
| Command | What it does |
|---|---|
| `npm install` | Install once (needs Node.js 20 or newer) |
| `npm run dev` | Local preview at http://localhost:4321 |
| `npm run build` | Build the site into `dist/` |
| `npm run check` | After a build: checks every page, link, title and language |

## Vercel settings (the existing project)
Vercel reads `vercel.json`, so these are already set:
- Framework: **Astro**, Build command: `npm run build`, Output directory: `dist`
- Environment variable (Settings > Environment Variables): `SITE_URL` = `https://noblessworld.vercel.app` now, `https://nobless.world` after the domain is bought. Without it, the site uses the vercel.app address.

## How GitHub and Vercel work together
1. The code lives in a GitHub repository.
2. In Vercel: Project > Settings > Git > connect that repository (once).
3. Every push to the **main** branch deploys the live site. Every other branch gets its own **preview** link, without touching the live site.

## Updating the site safely (beginner steps)
1. Make the change on a new branch (or ask Claude to), never directly on main.
2. Open the branch's preview link from Vercel (Deployments tab) and check it on phone and computer.
3. If it looks right, merge the branch into main (Pull request > Merge). Vercel deploys it.
4. Check status: Vercel > Deployments. Green "Ready" = live.
5. **Roll back:** Vercel > Deployments > pick the last good deployment > ⋯ > **Promote to Production** (or "Instant Rollback"). Nothing is lost.

## Settings: `src/data/site.json`
Empty values hide their element, so nothing unverified shows.
| Key | Put | While empty |
|---|---|---|
| `web3formsKey` | Key from web3forms.com, after approval and a real test | Form hidden; Contact says it is being set up; NOBEON points to the Journal |
| `formProvider` | Name of the form service, e.g. `Web3Forms` | Privacy page names Web3Forms by default once a key exists |
| `contactEmail` | A real, working inbox | No email shown |
| `sinceYear` | e.g. `2023`, only once verified | No "Since…" |
| `hosting` | `Vercel` (current) | No hosting line on Legal/Privacy |
| `social` | Real account links | No social links |

## Design
- **One typeface:** Readex Pro (Latin + Arabic, free OFL licence), self-hosted, variable weight and width (HEXP axis on Latin headings).
- **Interactive, calm:** the Lattice forms the logo in the hero; on computers a faint dot field follows the pointer and cards light up under it; headlines settle from thin to normal weight.
- **Reduced motion:** with "reduce motion" on (phone or computer settings) all of this is static. Phones never get the pointer field.

## Deploy checklist (every update)
**Before:** `npm run build` and `npm run check` pass · change made on a branch, not main · Vercel preview link checked on phone and computer (FR, EN, AR, menu, language switch, 404) · nothing in `site.json` that is not verified.
**Deploy:** merge the pull request into main · Vercel > Deployments shows "Ready" · open the live site and repeat the quick check.
**Roll back if:** a page is blank or broken, the menu or language switch fails, or wrong information shows. Vercel > Deployments > last good one > Promote to Production.

## Journal
Articles live in `src/data/journal/<slug>/en.md` (+ `fr.md`, `ar.md`). Header fields: `title`, `date`, `category` (announcements, nobeon, build, research, roadmap), `status` (fact, wip, plan), `product`, `excerpt`, `draft`. `draft: true` keeps an article off the site. To read drafts locally: `SHOW_DRAFTS=1 npm run dev` (never set SHOW_DRAFTS in Vercel). Drafts waiting for approval: `how-we-build` (EN, FR, AR) and an older `introducing-nobless` (EN). To publish one, change `draft: true` to `draft: false`.

## Rules kept in the code
Three principles only: Honesty, Innovation, Accessibility. No names, faces, invented numbers, customers, partners, dates or legal details. NOBEON is shown as "In exploration". Arabic writes NOBLESS in Latin letters; the logo is never mirrored.
