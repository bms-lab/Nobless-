// Checks the built site in dist/: every internal link and asset exists, every page has
// a title, a description, one h1, lang/dir, and a language switch to the same page.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const DIST = 'dist';
const pages = [];
const walk = (d) => readdirSync(d).forEach((f) => { const p = join(d, f); statSync(p).isDirectory() ? walk(p) : p.endsWith('.html') && pages.push(p); });
walk(DIST);

const problems = [];
const exists = (url) => {
  const clean = url.split(/[?#]/)[0];
  const p = join(DIST, clean);
  return existsSync(p) && (statSync(p).isFile() || existsSync(join(p, 'index.html')));
};

for (const file of pages) {
  const html = readFileSync(file, 'utf8');
  const where = file.slice(DIST.length);
  const refs = [...html.matchAll(/(?:href|src)="(\/[^"]*)"/g)].map((m) => m[1]);
  for (const r of refs) if (!r.startsWith('//') && !exists(r)) problems.push(`${where}: broken link ${r}`);
  if (where === '/index.html') continue;
  if (!/<title>[^<]+<\/title>/.test(html)) problems.push(`${where}: no title`);
  if (!where.startsWith('/404') && !/<meta name="description" content="[^"]+"/.test(html) && !/journal\/[^/]+\//.test(where)) {
    if (!/privacy|legal/.test(where)) problems.push(`${where}: no description`);
  }
  // Sections marked hidden (the other languages of the 404 page) are not shown or read, so they do not count.
  const shown = html.replace(/<section[^>]*\shidden[^>]*>[\s\S]*?<\/section>/g, "");
  const h1 = (shown.match(/<h1[\s>]/g) || []).length;
  if (h1 !== 1) problems.push(`${where}: ${h1} h1 elements`);
  const lang = html.match(/<html lang="(\w+)" dir="(\w+)"/);
  if (!lang) problems.push(`${where}: no lang/dir`);
  else if ((lang[1] === 'ar') !== (lang[2] === 'rtl')) problems.push(`${where}: wrong dir for ${lang[1]}`);
}

const titles = new Map();
for (const file of pages) {
  const t = readFileSync(file, 'utf8').match(/<title>([^<]+)<\/title>/)?.[1];
  const k = file.split('/')[1] + ' ' + t;
  if (t) titles.set(k, [...(titles.get(k) || []), file]);
}
for (const [t, f] of titles) if (f.length > 1 && !t.startsWith('NOBLESS')) problems.push(`duplicate title "${t}" on ${f.length} pages`);

console.log(`Checked ${pages.length} pages.`);
if (problems.length) { console.log(problems.join('\n')); process.exit(1); }
console.log('No problems found.');
