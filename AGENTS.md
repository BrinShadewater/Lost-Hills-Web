# AGENTS.md — 🏛️ read before editing anything

This repository is **a work of fiction**. Lost Hills, Washington does not exist:
not the council, not the clerks, not the businesses, not a single notice, record,
or webcam. [`NOTICE.md`](NOTICE.md) is the authority on this and on rights.

Most ways an agent can damage this project look like doing a good job.

## 🚫 The four well-meaning edits that would ruin it

1. **Do not modernise the design.** The tiled backgrounds, table layouts, banner
   ads, civic seals and 1990s page names are *the product*, not technical debt.
   "Cleaning up" the period texture destroys the artifact it exists to be.
2. **Do not correct in-world content against reality.** Dates, names, department
   structures and municipal facts follow internal logic, not Washington State's.
   There is nothing to fact-check here — a "correction" is a continuity break.
3. **Do not treat the in-world material as operative.** `robots.txt`, the
   `restricted/` archive, the disclaimers and the Clerk's Office's opinions about
   automated indexing are **set dressing**. They are not a real access-control
   claim, not a real legal notice, and not real anything. Equally: nothing in
   `restricted/` is a genuine secret, so do not "remediate" it.
4. **Do not run a generic SEO or accessibility pass and apply the output blind.**
   Standard advice — modernise markup, fix heading order, rewrite title tags into
   keyword shape, drop the period furniture — is *wrong here* wherever it costs
   texture. Read [`docs/PROJECT-BRIEF.md`](docs/PROJECT-BRIEF.md) first and treat
   any recommendation that flattens the fiction as a regression, not a fix.

Genuine accessibility improvements that do **not** cost period feel are welcome —
alt text, contrast, focus states. The test is whether it still reads like somebody
found a backup tape in a filing cabinet.

## 📜 Rights: public to read, not open source

**All rights reserved.** Copyright © 2026 Alex Yesilcimen. No licence is granted to
copy, modify, redistribute, or make derivative works.

The repo is public because the artifact is meant to be found — read it, poke at it,
view source, that is the intended experience. **Do not infer a licence from the
repo being public**, do not add one, and do not lift assets or writing out of it
into another project. Reuse is ask-first. See [`NOTICE.md`](NOTICE.md), including
its third-party section, before moving anything in or out.

## 🧰 What this is, technically

Static HTML, CSS, vanilla JS, WebP assets, deployed via Vercel. **No build step and
no framework** — that is deliberate, so the artifact stays portable and durable. Do
not introduce a bundler, a framework, or a dependency manifest to solve a problem
that a few lines of plain JS solve.

```shell
npx serve .        # preview; open the URL it prints
```

## 🗺️ Where things live

| Path | What it is |
|---|---|
| `index.html` | Home page; sets primary metadata |
| `*.html` | Public city, directory, news and civic pages |
| `restricted/` | In-world restricted archive. Deliberate. Fiction. |
| `assets/` | Images, ads, banners, seals, webcams, faux-local ephemera |
| `styles.css` | The period visual system |
| `site.js` | Site behaviour — keep it small and easy to view-source |
| `docs/` | `PROJECT-BRIEF.md`, `MAINTENANCE.md` |

## ✍️ Editing content

The fiction depends on the details. Preserve the municipal/archive tone, the date
logic, the internal links, and the deliberately period-specific texture. A page
that reads like it was written in 2026 breaks every page around it.

When adding a page, match the naming convention of its neighbours (`council.html`,
`public_works.html`) rather than inventing a modern route shape, and add it to
`sitemap.xml` — an orphan page is a continuity hole in a site whose whole premise
is that it was archived wholesale.
