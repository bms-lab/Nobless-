import { defineConfig } from 'astro/config';

// The public address of the site. Set SITE_URL in Vercel (Settings > Environment Variables)
// when the domain changes, e.g. https://nobless.world after it is bought.
const site = process.env.SITE_URL || 'https://noblessworld.vercel.app';

export default defineConfig({
  site,
  trailingSlash: 'always',
  build: { format: 'directory' },
});
