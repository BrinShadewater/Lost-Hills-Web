# Lost Hills Online — Full SEO Audit Report
**Date:** 2026-05-25  
**Auditor:** Shadewater SEO Skill v2  
**Scope:** 12 pages — local static site (pre-deployment)  
**Base URL target:** To be confirmed at deployment (currently local files)

---

## Overall Score: 32 / 100 — Poor

| Category | Weight | Score | Weighted |
|---|---|---|---|
| Technical SEO | 25% | 28/100 | 7.0 |
| On-Page SEO | 15% | 22/100 | 3.3 |
| Content Quality | 20% | 55/100 | 11.0 |
| Schema / Structured Data | 15% | 0/100 | 0.0 |
| Performance (CWV) | 10% | 45/100 | 4.5 |
| Image Optimization | 10% | 28/100 | 2.8 |
| AI Search Readiness (GEO) | 5% | 10/100 | 0.5 |
| **Total** | | | **29.1 / 100** |

> **Important context:** Lost Hills Online is a fictional ARG / creative project styled as a 1993 municipal website. Recommendations below are calibrated for discoverability and social shareability — the intentional retro aesthetic and fictional framing are *not* flagged as issues.

---

## Critical Findings

### 1. Meta Descriptions — MISSING on all 12 pages
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** `parse_html.py` confirmed `meta_description: null` on every page.
- **Impact:** Google writes its own snippets — often badly. Missing descriptions mean you lose control of how the site appears in every search result. This is the single highest-leverage fix.
- **Fix:** Add unique `<meta name="description">` to every page. 140–160 chars. Should reflect the page's content and the ARG fiction framing.

---

### 2. Broken Viewport Meta — `width=1000` on all pages
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal (Google mobile-first)

- **Evidence:** `<meta name="viewport" content="width=1000">` across all pages (3 pages not even checked — binary-matched as encoding issues).
- **Impact:** Mobile-first indexing means Google crawls and indexes the mobile version first. `width=1000` tells mobile devices to render at a fixed 1000px — this disables responsive rendering and can cause Google to penalise the page for poor mobile UX, even for a deliberately desktop-era site.
- **Fix:** Change to `<meta name="viewport" content="width=device-width, initial-scale=1">`. The fixed 1000px layout can be preserved via CSS `min-width: 1000px` on the shell. The viewport tag controls scaling hint, not layout width.

---

### 3. H1 Tag is "Lost Hills Online" on Every Page
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** All 12 pages share `<h1>Lost Hills Online</h1>` (in the banner). Each page's real content heading is in an H2 (e.g. `[#]Shadewater Applied Systems Conference`).
- **Impact:** Google uses H1 to understand what a page is about. When all pages have the same H1 (the site name), they're treated as undifferentiated. The `[#]` glyph prefix also pollutes H2 text.
- **Fix:** Promote each page's H2 to H1. The banner can use a `<div>` or `<p>` styled visually as H1 — it doesn't need to be a semantic heading. Remove the `[#]` glyph from heading text (can be added via CSS `::before`).

---

### 4. No `<html lang="...">` Attribute
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** `grep` found zero lang attributes across all pages.
- **Impact:** Screen readers can't determine language. Browsers and crawlers default to unknown. Required for accessibility compliance (WCAG 2.1 Level A).
- **Fix:** Add `lang="en"` to all `<html>` opening tags. Site-wide find-replace.

---

### 5. No Open Graph or Twitter Card Tags
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** Zero `og:*` or `twitter:*` meta tags on any page.
- **Impact:** When someone shares a link to Lost Hills Online on any social platform, it renders as a raw URL with no preview image, no title, no description. For an ARG / creative project that depends on word-of-mouth and sharing, this is a significant discoverability loss.
- **Fix:** Add OG + Twitter Card tags to every page. At minimum: `og:title`, `og:description`, `og:image`, `og:url`, `og:type`, `twitter:card`, `twitter:title`, `twitter:description`, `twitter:image`.

---

### 6. No robots.txt
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** File not found at root.
- **Impact:** Without robots.txt, crawlers may index the `/restricted/` directory and its files (clerk_notices, field_contact_log, horizon_mapping_log, clerk_removed_articles). Those pages appear intended as discoverable-but-not-obviously-public ARG content — that's fine, but the lack of robots.txt means no control over AI crawler access or crawl budget.
- **Fix:** Create `robots.txt`. At minimum allow all. Consider disallowing `/restricted/` from AI scrapers (GPTBot, ClaudeBot, etc.) if the ARG discovery path is meant to be human-driven.

---

### 7. No sitemap.xml
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** File not found at root.
- **Impact:** Crawlers discover pages through links, but a sitemap guarantees all pages are submitted for indexing and signals priority/freshness.
- **Fix:** Generate `sitemap.xml` listing all 12 public pages + the restricted pages if you want them indexed.

---

### 8. Zero Schema Markup Sitewide
**Severity:** Critical | **Confidence:** Confirmed | **Scope:** Universal

- **Evidence:** `parse_html.py` found 0 JSON-LD blocks on all 12 pages.
- **Impact:** No rich results eligibility. For a creative/entertainment project that could benefit from `WebSite` + `SearchAction` schema on the homepage and `Event` schema on the conference page, this is a missed opportunity.
- **Fix:** See Action Plan for specific schema recommendations by page type.

---

## Warning Findings

### 9. No Canonical Tags
**Severity:** Warning | **Confidence:** Confirmed

- **Evidence:** `canonical: null` on all pages.
- **Impact:** If/when the site is live under multiple URLs (www vs non-www, http vs https), crawlers will index duplicates. Self-referencing canonicals are cheap insurance.
- **Fix:** Add `<link rel="canonical" href="https://yourdomain.com/pagename.html">` to each page.

---

### 10. No Image Lazy Loading (63 images)
**Severity:** Warning | **Confidence:** Confirmed

- **Evidence:** 0 of 63 `<img>` tags have `loading="lazy"` attributes.
- **Impact:** All images load on page load regardless of viewport position. Hurts LCP and overall page load time — especially on image-heavy pages like conference.html (9 images).
- **Fix:** Add `loading="lazy"` to all images below the fold. Above-the-fold hero images should get `loading="eager"` and `fetchpriority="high"` instead.

---

### 11. 10 Images with Blank src and alt (Phantom `<img>` Tags)
**Severity:** Warning | **Confidence:** Confirmed

- **Evidence:** `src=""` `alt=""` found on 10 pages (one per page). Likely a copy-paste artifact or template placeholder.
- **Impact:** Blank-src images trigger an extra HTTP request to the current page URL, wasting bandwidth and potentially causing 404 logs.
- **Fix:** Remove or replace all `<img src="" alt="">` tags.

---

### 12. 50 Images Missing Explicit width/height Attributes
**Severity:** Warning | **Confidence:** Confirmed

- **Evidence:** Only ~13 of 63 images have both `width` and `height` set.
- **Impact:** Without dimensions, the browser can't reserve layout space before the image loads, causing Cumulative Layout Shift (CLS) — a Core Web Vitals metric.
- **Fix:** Add `width` and `height` attributes matching the intrinsic image dimensions to all `<img>` tags. CSS can override display size independently.

---

### 13. Title Tags Use `::` Separator and Are Short
**Severity:** Warning | **Confidence:** Confirmed

- **Evidence:** Titles range 25–47 chars. Format is `Site Name :: Page Name` or `Page Name :: Site Name`.
- **Impact:** Titles are technically fine but on the short/generic side. `MOFA` (25 chars) and `Home` (25 chars) give Google very little context. The `::` separator is fine — just ensure the page-specific term comes first.
- **Fix:** Consider reversing format to `Page Name | Lost Hills Online` and expanding short titles. `Lost Hills MOFA :: Museum of Fine Art — City of Lost Hills, WA` is more descriptive at minimal effort.

---

### 14. Readability — Very Difficult (Flesch 24–27)
**Severity:** Warning | **Confidence:** Likely | **Scope:** Universal

- **Evidence:** `readability.py` scores both index.html (Flesch 27) and conference.html (Flesch 24) as "Very Difficult / College level." Complex word percentage 22–24%.
- **Impact:** Per E-E-A-T signals, content that's harder to parse reduces engagement. That said, the fictional/ARG nature means some deliberate complexity is appropriate (corrupted log entries, bureaucratic language, etc.).
- **Recommendation:** This is likely *intentional* — the "degraded archive" voice is part of the fiction. No change needed for body copy. However, any content intended to attract real search traffic (e.g. an out-of-fiction "What is Lost Hills Online?" landing page) should use simpler language.

---

### 15. No llms.txt
**Severity:** Info | **Confidence:** Confirmed | **Scope:** Experimental

- **Evidence:** File not found at root.
- **Impact:** Optional file used by some AI crawlers (not a Google requirement). Useful if you want to provide structured context to AI assistants about what the site is and what's off-limits.
- **Fix:** Optional. If added, include title, description, links to key pages, and note the ARG/fiction framing.

---

## Passing Items

| Check | Status |
|---|---|
| UTF-8 charset declared on all pages | ✅ Pass |
| All `<title>` tags present | ✅ Pass |
| Inline JS/CSS kept minimal (external files used) | ✅ Pass |
| No duplicate titles | ✅ Pass |
| Internal link structure well-formed (consistent nav) | ✅ Pass |
| Alt text present on most images (53/63) | ✅ Pass |
| No redirect chains detectable in local files | ✅ Pass (verify at deploy) |
| JavaScript not blocking content render (JS at bottom) | ✅ Pass |

---

## Environment Limitations

- Site is pre-deployment / local files — PageSpeed Insights, Core Web Vitals, live redirect checks, and social meta validation cannot be run until deployed to a public URL.
- Playwright not installed — screenshot analysis unavailable.
- 3 pages (directory.html, links.html, sezzler.html) returned as binary matches on grep — possible encoding issue; recommend re-saving as UTF-8 without BOM.

