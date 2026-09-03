#!/usr/bin/env python3
"""Mechanises the README's review checklist for a static site.

Two checks, both of which have only ever been done by eye here:

  1. Every internal href/src in every HTML page resolves to a file in the repo.
     A renamed page or a moved asset breaks silently otherwise — the site has no
     build step to notice, and Vercel serves a 404 as happily as a 200.
  2. Every public HTML page is listed in sitemap.xml, and every sitemap entry
     points at a page that exists. Pages under restricted/ are excluded on
     purpose: robots.txt disallows that path, so they must NOT be in the sitemap.

Stdlib only. Exit 0 clean, 1 on any finding. Run from anywhere:

    python scripts/check_site.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_ORIGIN = "https://losthills.net"
EXCLUDED_DIRS = {".git", "node_modules", "scripts", "docs", "uploads"}
NOT_IN_SITEMAP = ("restricted/",)  # disallowed in robots.txt, so never advertised
EXTERNAL = ("http:", "https:", "mailto:", "tel:", "#", "data:", "javascript:")
REF_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
LOC_RE = re.compile(r"<loc>\s*([^<\s]+)\s*</loc>")


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def html_pages() -> list[Path]:
    return sorted(
        p for p in ROOT.rglob("*.html")
        if not (set(p.relative_to(ROOT).parts[:-1]) & EXCLUDED_DIRS)
    )


def check_internal_refs(pages: list[Path]) -> list[str]:
    problems = []
    for page in pages:
        html = page.read_text(encoding="utf-8", errors="replace")
        for m in REF_RE.finditer(html):
            ref = m.group(1).strip()
            if not ref or ref.startswith(EXTERNAL):
                continue
            path = ref.split("#", 1)[0].split("?", 1)[0]
            if not path:
                continue
            target = ROOT / path.lstrip("/") if path.startswith("/") else page.parent / path
            if path.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                problems.append(f"{rel(page)}: '{ref}' does not resolve to a file")
    return problems


def sitemap_path_for(page: Path) -> str:
    r = rel(page)
    return "" if r == "index.html" else r


def check_sitemap(pages: list[Path]) -> list[str]:
    problems = []
    sitemap = ROOT / "sitemap.xml"
    if not sitemap.exists():
        return ["sitemap.xml is missing"]
    locs = LOC_RE.findall(sitemap.read_text(encoding="utf-8"))
    listed = set()
    for loc in locs:
        if not loc.startswith(SITE_ORIGIN):
            problems.append(f"sitemap.xml: '{loc}' is not under {SITE_ORIGIN}")
            continue
        listed.add(loc[len(SITE_ORIGIN):].lstrip("/"))
    public = {sitemap_path_for(p) for p in pages if not rel(p).startswith(NOT_IN_SITEMAP)}
    for missing in sorted(public - listed):
        problems.append(f"sitemap.xml: public page '{missing or 'index.html'}' is not listed")
    for extra in sorted(listed - public):
        if extra.startswith(NOT_IN_SITEMAP):
            problems.append(f"sitemap.xml: '{extra}' is under restricted/, which robots.txt disallows")
        else:
            problems.append(f"sitemap.xml: '{extra}' is listed but no such page exists")
    return problems


def main() -> int:
    pages = html_pages()
    problems = check_internal_refs(pages) + check_sitemap(pages)
    for p in problems:
        print(f"FAIL  {p}")
    print(f"{len(pages)} page(s) checked, {len(problems)} problem(s).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
