import site from '../data/site.json';
import nobeon from '../data/products/nobeon.json';
import type { Lang } from '../i18n/strings';

export { site };

export const isRealKey = (k: string) => !!k && k !== 'REPLACE_ME';

export const href = (lang: Lang, path = '') => `/${lang}/${path ? path.replace(/^\/|\/$/g, '') + '/' : ''}`;

export const products = [nobeon].sort((a, b) => a.order - b.order);
export type Product = (typeof products)[number];

export interface Article {
  slug: string;
  lang: Lang;
  isFallback: boolean;
  title: string;
  date: string;
  category: string;
  status: string;
  product: string;
  excerpt: string;
  Content: any;
}

const files = import.meta.glob('../data/journal/*/*.md', { eager: true }) as Record<string, any>;

const bySlug = new Map<string, Record<string, any>>();
for (const [path, mod] of Object.entries(files)) {
  const m = path.match(/journal\/([^/]+)\/(en|fr|ar)\.md$/);
  if (!m) continue;
  const [, slug, lang] = m;
  // Drafts are never built, except locally with SHOW_DRAFTS=1 (for review only, never on production).
  if (mod.frontmatter?.draft && !import.meta.env.SHOW_DRAFTS) continue;
  if (!bySlug.has(slug)) bySlug.set(slug, {});
  bySlug.get(slug)![lang] = mod;
}

// An article shows in a language only in that language, or in English with a clear note.
export function articles(lang: Lang): Article[] {
  const out: Article[] = [];
  for (const [slug, langs] of bySlug) {
    const mod = langs[lang] ?? langs.en;
    if (!mod) continue;
    const fm = mod.frontmatter;
    out.push({
      slug, lang, isFallback: !langs[lang],
      title: fm.title, date: String(fm.date).slice(0, 10), category: fm.category, status: fm.status,
      product: fm.product ?? '', excerpt: fm.excerpt ?? '', Content: mod.Content,
    });
  }
  return out.sort((a, b) => b.date.localeCompare(a.date));
}

export const fmtDate = (d: string, lang: Lang) =>
  new Date(d + 'T00:00:00Z').toLocaleDateString(lang === 'ar' ? 'ar-MA' : lang, { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
