"""Generates the wireframe site's HTML pages.

Run from this folder:  python3 build.py
Every page is written as <path>/index.html so the clean URLs work
(/resources/sf/ etc.) on GitHub Pages or any static server.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
ABOUT_FRIARS = "https://capuchinswest.org/"
UPDATED = "October 20, 2026"

ICON = {
    "chev": '<svg class="chev" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>',
    "out": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>',
    "clock": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "phone": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "globe": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/></svg>',
}


def page(path, title, body, crumbs=None):
    crumb_html = ""
    if crumbs:
        parts = []
        for i, (label, href) in enumerate(crumbs):
            if i == len(crumbs) - 1:
                parts.append(f'<span aria-current="page">{escape(label)}</span>')
            else:
                parts.append(f'<a href="{href}">{escape(label)}</a><span aria-hidden="true">›</span>')
        crumb_html = f'<nav class="breadcrumb" aria-label="Breadcrumb">{"".join(parts)}</nav>\n'
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · Capuchin Family Kitchen</title>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="logo" href="/resources/"><img src="/assets/img/logo.png" alt="Capuchin Family Kitchen" width="72" height="60"></a>
    <nav class="nav" aria-label="Main">
      <a class="desktop-only" href="/resources/sf/">San Francisco</a>
      <a class="desktop-only" href="/resources/oak/">Oakland</a>
      <a href="{ABOUT_FRIARS}">About the Friars ↗</a>
    </nav>
  </div>
</header>
<main>
  <div class="wrap">
{crumb_html}{body}
  </div>
</main>
<footer class="site-footer">
  <div class="wrap"><p>This website is maintained by volunteers. Last updated {UPDATED}</p></div>
</footer>
</body>
</html>
"""
    out = ROOT / path.strip("/") / "index.html" if path != "/" else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print("wrote", out.relative_to(ROOT))


def tile(href, title, sub=None):
    sub_html = f'<span class="tile-sub">{escape(sub)}</span>' if sub else ""
    return f'<a class="tile" href="{href}"><span class="tile-text"><span class="tile-title">{escape(title)}</span>{sub_html}</span>{ICON["chev"]}</a>'


def mass(href, img, alt, pos, parish, city):
    return f"""<a class="mass" href="{href}">
  <img src="/assets/img/{img}" alt="{escape(alt)}" style="object-position: {pos}">
  <span class="scrim" aria-hidden="true"></span>
  <span class="mass-text">
    <span class="tile-text"><span class="mass-title">Join us for Mass</span><span class="mass-sub">{escape(parish)} · {escape(city)}</span></span>
    <span class="badge">{ICON["out"]}</span>
  </span>
</a>"""


def resource(n, kind):
    return f"""<li class="resource">
  <div class="who"><h2>[{kind} resource {n}]</h2><p class="blurb">[One line describing the resource]</p></div>
  <div class="meta hours">{ICON["clock"]}[Days · hours]</div>
  <div class="reach">
    <div class="meta phone">{ICON["phone"]}[Phone number]</div>
    <a class="desktop-web" href="#">{ICON["globe"]}Website ↗</a>
  </div>
  <div class="actions">
    <a class="btn btn-call" href="#">{ICON["phone"]}Call</a>
    <a class="btn btn-web" href="#">{ICON["globe"]}Website ↗</a>
  </div>
</li>"""


# / -> /resources/
(ROOT / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Capuchin Family Kitchen</title>
<meta http-equiv="refresh" content="0; url=/resources/">
<link rel="canonical" href="/resources/">
<script>location.replace("/resources/");</script>
</head>
<body><p><a href="/resources/">Continue to the Capuchin Family Kitchen</a></p></body>
</html>
""")
print("wrote index.html (redirect)")

page("/resources/", "Welcome", f"""<img class="photo" src="/assets/img/friars.jpg" alt="Three Capuchin friars walking down a San Francisco sidewalk" width="1072" height="852">
<div class="intro">
  <h1>Welcome</h1>
  <p>We are the Capuchin Family Kitchen, a ministry of the <a href="https://shrinesf.org/">National Shrine of St. Francis of Assisi</a>.</p>
  <p>This website contains information about the faith that moves us, how to join us, and resources to meet basic needs in and around the San Francisco Bay Area.</p>
</div>
<div class="tiles two">
  {tile("/resources/sf/", "San Francisco", "Recovery · Housing · Meals")}
  {tile("/resources/oak/", "Oakland", "Resources coming soon")}
</div>""")

page("/resources/sf/", "Free Resources in San Francisco", f"""<div class="intro"><h1>Free Resources in San Francisco</h1></div>
<div class="tiles">
  {tile("/resources/recovery/", "Recovery")}
  {tile("/resources/housing/", "Housing")}
  {tile("/resources/meals/", "Meals")}
</div>
{mass("https://shrinesf.org/", "sf_shrine.jpg", "The white Gothic towers of the National Shrine of St. Francis of Assisi in San Francisco", "50% 30%", "National Shrine of St. Francis of Assisi", "San Francisco, CA")}""",
     crumbs=[("Resources", "/resources/"), ("San Francisco", "")])

page("/resources/oak/", "Free Resources in Oakland", f"""<div class="intro"><h1>Free Resources in Oakland</h1></div>
<div class="soon">
  <h2>Resources coming soon</h2>
  <p>Recovery, housing and meal resources for Oakland will appear here.</p>
  <a href="/resources/sf/">See San Francisco resources →</a>
</div>
{mass("https://saintjarlath.org/", "st_jarlath.jpg", "The brick facade of St. Jarlath Church in Oakland", "35% 45%", "St. Jarlath Parish", "Oakland, CA")}""",
     crumbs=[("Resources", "/resources/"), ("Oakland", "")])

for slug, title, count in [("recovery", "Recovery", 5), ("housing", "Housing", 3), ("meals", "Meals", 7)]:
    items = "\n".join(resource(i, title) for i in range(1, count + 1))
    page(f"/resources/{slug}/", f"{title} in San Francisco", f"""<div class="intro">
  <h1>{title}</h1>
</div>
<ul class="listing">
{items}
</ul>
<a class="back" href="/resources/sf/">← Back to San Francisco</a>""",
         crumbs=[("Resources", "/resources/"), ("San Francisco", "/resources/sf/"), (title, "")])
