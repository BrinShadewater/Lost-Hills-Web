# Changelog

Notable changes to Lost Hills Web are tracked here.

## Unreleased

- Sidebar ads are served at the size they render (320 px variants via `srcset`; the zoom popup keeps the full scan), every ad image has explicit dimensions, and the home page's section headings are `h2`s under the `h1`. Local mobile Lighthouse performance 76 → 94, LCP 6.9 s → 3.2 s (#9).
- Added repository documentation, contribution guidance, security notes, issue templates, and pull request template.
- Added project brief and maintenance documentation for the static archive site.
- Added more expressive README headings and voice while keeping the documentation professional.

## 2026-09-04

- The sidebar advertiser cards point at a real anchor on the directory page. Sixty-eight of them linked ids that never existed; with JavaScript on the popup hid it.
- The site check verifies every fragment link against the target page's ids and legacy name anchors, so the next dead anchor fails the build.

## 2026-09-02

- CI runs the README review checklist.

## 2026-07-30

- Content from the critique backlog: a boot-sequence skip, more visible lore, and the link-rot story.
- Polish pass: the horror device renders, mobile fixed, deep links on the board.

## 2026-07-25

- Restored robots.txt, styles.css and sitemap.xml, which had shipped truncated. deploy.py is retired; deploy by git push.
