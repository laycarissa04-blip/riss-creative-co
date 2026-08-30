# risscreativeco.com

Single-page site for Riss Creative Co. Everything — CSS, JavaScript, fonts
fallbacks, illustrations and photographs — is contained in `index.html`.
There is no build step and no dependencies to install.

## Files

| File | What it is | Safe to delete? |
|---|---|---|
| `index.html` | The entire site | No |
| `og-image.png` | **You must add this** — see below | No |
| `CNAME` | Tells GitHub Pages the custom domain is `risscreativeco.com` | Only if not using the custom domain |
| `.nojekyll` | Stops GitHub from running Jekyll over the files | No |
| `robots.txt` | Lets search engines crawl, points them at the sitemap | No |
| `sitemap.xml` | Lists the one page, for search engines | No |
| `404.html` | Shown for any bad URL | Yes, but nice to keep |

## ⚠️ Before publishing: add `og-image.png`

`index.html` points at `https://risscreativeco.com/og-image.png` in four
places — the Open Graph tag, the Twitter card, and the Organization `image`
and `logo` in the structured data. That file is **not** in this folder.

Drop your existing `og-image.png` into the repository root, next to
`index.html`. Without it, links shared to Instagram, iMessage, LinkedIn and
Slack will show no preview image, and Google will see a broken logo URL.

Recommended: 1200 × 630 px, under 1 MB. The dimensions are already declared
in the HTML, so match them.

## Publishing on GitHub Pages

1. Create a repository and upload every file in this folder to the root
   (not inside a subfolder).
2. Repository → **Settings** → **Pages**.
3. Under *Build and deployment*, set **Source** to `Deploy from a branch`,
   branch `main`, folder `/ (root)`. Save.
4. Wait a minute, then check the URL GitHub shows you.

### Pointing risscreativeco.com at it

In Settings → Pages → *Custom domain*, enter `risscreativeco.com`.
Then at your domain registrar, create:

- Four **A** records for the apex `@`, pointing to:
  `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- One **CNAME** record for `www`, pointing to `USERNAME.github.io`
  (your GitHub username, no repository name on the end)

DNS can take anywhere from a few minutes to a day. Once it resolves, tick
**Enforce HTTPS** on the Pages settings screen.

Verify the current IPs against GitHub's own docs before relying on them:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Editing the site later

Everything lives in `index.html`. Useful landmarks, in order:

- `<head>` — title, meta description, Open Graph/Twitter tags, favicon
- `<script type="application/ld+json">` — structured data (Person, the
  studio, the Carter Lay Charitable Fund, WebPage, WebSite). A comment above
  it lists the profile URLs still to be filled in.
- `<style>` — all CSS
- `id="top"` — hero
- `id="philosophy"` — Philosophy
- `id="community"` — Community, the newspaper-style block
- `id="caps"` — Capabilities
- `id="contact"` — contact form
- `<script>` blocks at the bottom — the wall collage, typing, scroll effects

The contact form posts to Formspree
(`https://formspree.io/f/xnpaoyyr`). Submissions go to whichever inbox that
Formspree form is configured with — it is not tied to GitHub.

## A note on file size

`index.html` is about 3.7 MB because every image is embedded directly in it
as base64. This keeps the site to one file with nothing to break, but it
means a visitor downloads all of it before the page finishes. If loading
ever feels slow, the fix is to pull the images out into an `/images` folder
and reference them by filename — that is a mechanical change, not a redesign.
