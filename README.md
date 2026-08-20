# risscreativeco.com

Single-page site for Riss Creative Co. LLC — event production and creative direction, Los Angeles.

## What lives here

```
index.html                    the site (all CSS and JS inline)
og-image.png                  link-preview image used by the meta tags
cap-creative-direction.webp   drawing — Creative Direction
cap-galas.webp                drawing — Galas & Fundraisers
cap-activations.webp          drawing — Brand Activations
cap-community.webp            drawing — Community Events
cap-photo-video.webp          drawing — Photo & Video
cap-popups.webp               drawing — Pop-Ups
waxseal.webp                  wax seal behind the enquiries section
robots.txt                    tells crawlers the site is open, points at the sitemap
sitemap.xml                   lists the page so Google indexes it faster
```

The logo, favicon and portrait are base64-encoded inside `index.html`. The six drawings are separate files — **the page breaks without them.**

## Hosting: Vercel

This site is served by Vercel, not GitHub Pages. Deploy one of two ways.

### If Vercel is connected to your GitHub repo

Pushing to the repo redeploys automatically. Upload **every** file in this folder, not just `index.html`. Wait about a minute, then hard-refresh.

### If you drag a folder into vercel.com

Drag the **whole folder**. Dragging `index.html` on its own gives you a live page with six broken images.

### Checking a deploy worked

Open a file directly in the browser:

```
https://risscreativeco.com/cap-galas.webp
```

Drawing loads = deployed. 404 = that file never made it up.

## Files you can ignore

`CNAME` and `.nojekyll` are GitHub Pages artefacts. Vercel doesn't read either one — your domain is configured in the Vercel dashboard under Settings → Domains. Harmless to leave, safe to delete.

Also delete `arch.webp`, `table.webp` and `cart.webp` if they're still in the repo. Nothing references them.

## Making changes later

Edit `index.html`, redeploy. Update `<lastmod>` in `sitemap.xml` after a meaningful content change.

## After deploying

1. Search `site:risscreativeco.com` to check you're indexed.
2. Verify the domain in Google Search Console, submit `https://risscreativeco.com/sitemap.xml`.
3. Run the homepage through `search.google.com/test/rich-results`.
