import type { APIRoute } from 'astro';
import { LANGS } from '../i18n/strings';
import { products, articles } from '../lib/content';

// Every public page, in every language, with its language alternates.
export const GET: APIRoute = ({ site }) => {
  const base = site!.toString().replace(/\/$/, '');
  const paths = ['', 'company/', 'principles/', 'products/', 'journal/', 'contact/', 'privacy/', 'legal/',
    ...products.map((p) => `products/${p.slug}/`)];
  const urls: string[] = [];
  for (const path of paths) for (const lang of LANGS) {
    const alts = LANGS.map((l) => `<xhtml:link rel="alternate" hreflang="${l}" href="${base}/${l}/${path}"/>`).join('');
    urls.push(`<url><loc>${base}/${lang}/${path}</loc>${alts}</url>`);
  }
  for (const lang of LANGS) for (const a of articles(lang)) if (!a.isFallback) urls.push(`<url><loc>${base}/${lang}/journal/${a.slug}/</loc><lastmod>${a.date}</lastmod></url>`);
  const xml = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">${urls.join('')}</urlset>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/xml' } });
};
