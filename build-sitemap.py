"""Build sitemap.xml from whatever pages actually exist on disk.

Single owner for the sitemap — the page builders only write pages, so they
cannot clobber each other's URLs.

Run:  python build-sitemap.py
"""

import glob
import io
import os
from datetime import date

SITE = "https://deepakthapliyal.com"
TODAY = date.today().isoformat()

# home first, then city pages, then ceremony pages
paths = ["/"]
paths += sorted(f"/{os.path.dirname(p)}/" for p in glob.glob("pandit-in-*/index.html"))
paths += sorted(f"/{os.path.dirname(p)}/" for p in glob.glob("*/index.html")
                if not os.path.dirname(p).startswith("pandit-in-"))


def priority(path):
    if path == "/":
        return "1.0", "weekly"
    if path.startswith("/pandit-in-"):
        return "0.9", "monthly"
    return "0.8", "monthly"


entries = []
for path in paths:
    p, cf = priority(path)
    entries.append(
        f"  <url>\n    <loc>{SITE}{path}</loc>\n    <lastmod>{TODAY}</lastmod>\n"
        f"    <changefreq>{cf}</changefreq>\n    <priority>{p}</priority>\n  </url>"
    )

io.open("sitemap.xml", "w", encoding="utf-8").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n'
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "\n".join(entries) + "\n</urlset>\n"
)
print(f"sitemap.xml written with {len(paths)} URLs:")
for path in paths:
    print(f"  {SITE}{path}")
