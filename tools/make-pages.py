"""Builds about.html, services.html and contact.html from index.html.
Same page, own title / description / canonical so Google lists each URL.
Run after any change to index.html:  python3 tools/make-pages.py"""
import pathlib, html
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "index.html").read_text()
PAGES = {
  "about": ("About | Riss Creative Co., Los Angeles Web Design Studio",
            "Riss Creative Co. is a Los Angeles digital studio founded by Carissa Lay: websites, brand identity and AI systems, designed and built in-house."),
  "services": ("Services | Website Design, Branding & AI Systems | Riss Creative Co.",
               "Website design and development, brand identity, SEO and Google setup, ongoing care, and practical AI tools for small businesses. Los Angeles."),
  "contact": ("Contact | Riss Creative Co.",
              "Start a project with Riss Creative Co. Email contact@risscreativeco.com or book a 30-minute call. Based in Los Angeles, working with clients everywhere."),
}
def swap(s, old, new):
    assert s.count(old) == 1, old
    return s.replace(old, new)
T0 = "<title>Riss Creative Co. | Websites &amp; AI Consulting for Small Businesses, Los Angeles</title>"
D0 = src[src.index('<meta name="description" content="'):]; D0 = D0[:D0.index('>')+1]
for slug, (title, desc) in PAGES.items():
    url = f"https://risscreativeco.com/{slug}"
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    s = swap(src, T0, f"<title>{t}</title>")
    s = swap(s, D0, f'<meta name="description" content="{d}">')
    s = swap(s, '<link rel="canonical" href="https://risscreativeco.com/">', f'<link rel="canonical" href="{url}">')
    s = swap(s, '<meta property="og:url" content="https://risscreativeco.com/">', f'<meta property="og:url" content="{url}">')
    s = swap(s, '<meta property="og:title" content="Riss Creative Co.">', f'<meta property="og:title" content="{t}">')
    s = swap(s, '<meta name="twitter:title" content="Riss Creative Co.">', f'<meta name="twitter:title" content="{t}">')
    s = swap(s, '<body data-view="home" class="loading">', f'<body data-view="{slug}" class="loading">')
    (root / f"{slug}.html").write_text(s)
    print("wrote", slug + ".html")
