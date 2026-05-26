# Lost Hills Online — SEO Action Plan
**Generated:** 2026-05-25  
**Priority:** P1 = Fix before launch | P2 = Fix within 2 weeks of launch | P3 = Nice to have

---

## P1 — Fix Before Launch (High Impact, Low Effort)

### P1-A: Fix Viewport Meta (All 12 pages)
**Effort:** 10 min (find-replace) | **Impact:** Critical — mobile-first indexing

Change every instance of:
```html
<meta name="viewport" content="width=1000">
```
To:
```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
Then add to `styles.css` to preserve the 1000px fixed layout:
```css
.shell { min-width: 1000px; }
```
This lets mobile crawlers see a valid viewport while keeping the retro layout intact.

---

### P1-B: Add `lang="en"` to All `<html>` Tags (All 12 pages)
**Effort:** 5 min (find-replace) | **Impact:** Critical — accessibility + crawlability

Change:
```html
<html>
```
To:
```html
<html lang="en">
```

---

### P1-C: Fix H1 Structure (All 12 pages)
**Effort:** 30 min | **Impact:** Critical — page identity in search

The banner `<h1>Lost Hills Online</h1>` should become a styled `<div>` or `<p>`. Each page's current `<h2>` (e.g. `[#]Shadewater Applied Systems Conference`) should be promoted to `<h1>` and the `[#]` glyph moved to CSS `::before`.

**Example change in conference.html:**
```html
<!-- Banner: change h1 to div -->
<div class="banner-title-heading">Lost Hills Online</div>

<!-- Content: promote h2 to h1, remove [#] from markup -->
<h1 class="page-h1">Shadewater Applied Systems Conference</h1>
```
```css
.page-h1::before { content: "[#] "; font-family: "Courier New", monospace; color: #88826a; font-size: 14px; font-weight: normal; }
```

---

### P1-D: Add Meta Descriptions (All 12 pages)
**Effort:** 30 min | **Impact:** Critical — controls search snippet appearance

Add to each page's `<head>`. Keep 140–160 chars. Stay in-fiction — these are what appears in Google results, so lean into the ARG framing:

| Page | Suggested Meta Description |
|---|---|
| index.html | `The official municipal information network of Lost Hills, Washington. Restored from backup volume B12 after extended archive dormancy. CityNet pilot since 05.17.1993.` |
| conference.html | `Archive of the 1993 Shadewater Applied Systems Conference — May 17–21, Sezzler Resort, Lost Hills WA. Schedule, exhibitors, speakers, and final day records.` |
| about.html | `City of Lost Hills, Washington — civic history, geography, and public records. Population 11,402. Founded 1889. Archive restored from degraded backup.` |
| shadewater.html | `Shadewater Laboratories — civic technology partner to the City of Lost Hills since 1987. Applied systems, archive continuity, and the EACS remote maintenance protocol.` |
| sezzler.html | `Sezzler Hotel & Conference Resort, Lost Hills WA — host venue of the 1993 Shadewater Applied Systems Conference. Towers 1–3, Pavilions A–C.` |
| catfish.html | `Catfish Lake Recreation Area, Lost Hills WA — access permits, environmental monitoring data, and survey records. Boat launch hours and permit issuance notices.` |
| mofa.html | `Lost Hills Museum of Fine Art — current exhibit: "The Shape of Distance." Public gallery, digital exhibit archive, and community submissions.` |
| news.html | `Lost Hills News Archive — civic bulletins and event records from May 1993, restored from CityNet backup volume B12. Some entries withdrawn or pending review.` |
| community.html | `CommunityNet — the Lost Hills public message board, reopened after archive restoration. Local discussion, civic notices, and community posts.` |
| directory.html | `Lost Hills Business Directory — local businesses, civic partners, and services as listed in the 1993 CityNet public index.` |
| contact.html | `Contact the Lost Hills City Clerk's Office — archive corrections, removal requests, and civic inquiries. Response times may vary.` |
| links.html | `Local Links — external resources and partner sites referenced in the Lost Hills Online municipal archive.` |

---

### P1-E: Create robots.txt
**Effort:** 5 min | **Impact:** Critical — crawler control

```
User-agent: *
Allow: /

User-agent: GPTBot
Disallow: /restricted/

User-agent: ClaudeBot
Disallow: /restricted/

User-agent: PerplexityBot
Disallow: /restricted/

User-agent: Google-Extended
Disallow: /restricted/

Sitemap: https://yourdomain.com/sitemap.xml
```
> Replace `yourdomain.com` with actual domain at launch. The `/restricted/` pages are discoverable via internal links (the ARG path) but excluding them from AI scrapers preserves the human-discovery intent.

---

### P1-F: Create sitemap.xml
**Effort:** 10 min | **Impact:** Critical — indexing guarantee

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://yourdomain.com/</loc><priority>1.0</priority></url>
  <url><loc>https://yourdomain.com/conference.html</loc><priority>0.9</priority></url>
  <url><loc>https://yourdomain.com/about.html</loc><priority>0.8</priority></url>
  <url><loc>https://yourdomain.com/shadewater.html</loc><priority>0.8</priority></url>
  <url><loc>https://yourdomain.com/sezzler.html</loc><priority>0.7</priority></url>
  <url><loc>https://yourdomain.com/catfish.html</loc><priority>0.7</priority></url>
  <url><loc>https://yourdomain.com/mofa.html</loc><priority>0.7</priority></url>
  <url><loc>https://yourdomain.com/news.html</loc><priority>0.7</priority></url>
  <url><loc>https://yourdomain.com/community.html</loc><priority>0.6</priority></url>
  <url><loc>https://yourdomain.com/directory.html</loc><priority>0.6</priority></url>
  <url><loc>https://yourdomain.com/contact.html</loc><priority>0.5</priority></url>
  <url><loc>https://yourdomain.com/links.html</loc><priority>0.4</priority></url>
</urlset>
```

---

### P1-G: Remove Phantom Blank `<img>` Tags (10 pages)
**Effort:** 10 min | **Impact:** Warning — prevents bogus HTTP requests

Find and remove (or comment out) all instances of:
```html
<img src="" alt="">
```
These appear once per page — likely a stray template artifact.

---

## P2 — Fix Within 2 Weeks of Launch

### P2-A: Add Open Graph + Twitter Card Tags (All pages)
**Effort:** 45 min | **Impact:** Critical for social sharing / discoverability

Add to each page `<head>`. Template:
```html
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://yourdomain.com/PAGE.html">
<meta property="og:title" content="PAGE TITLE">
<meta property="og:description" content="PAGE DESCRIPTION">
<meta property="og:image" content="https://yourdomain.com/assets/og-image.jpg">
<meta property="og:site_name" content="Lost Hills Online">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="PAGE TITLE">
<meta name="twitter:description" content="PAGE DESCRIPTION">
<meta name="twitter:image" content="https://yourdomain.com/assets/og-image.jpg">
```
**Create an OG image:** A 1200×630px image using the site's green-on-dark aesthetic with the Lost Hills seal and "Lost Hills Online — CityNet Archive Restored" text. This single image can be reused across all pages as a default, with page-specific variants for conference and index.

---

### P2-B: Add Canonical Tags (All pages)
**Effort:** 15 min | **Impact:** Warning — prevents duplicate indexing

Add to each page `<head>`:
```html
<link rel="canonical" href="https://yourdomain.com/PAGE.html">
```

---

### P2-C: Add Lazy Loading + Dimensions to Images
**Effort:** 60 min | **Impact:** Warning — Core Web Vitals (CLS, LCP)

For all images below the fold:
```html
<img ... loading="lazy" width="W" height="H">
```
For above-the-fold hero images (panorama on index, banner on conference):
```html
<img ... loading="eager" fetchpriority="high" width="W" height="H">
```
Run this to get actual image dimensions:
```bash
python3 -c "
from PIL import Image; import os
for f in os.listdir('assets'):
    if f.endswith(('.jpg','.png','.jpeg')):
        img = Image.open(f'assets/{f}')
        print(f'{f}: {img.size}')
"
```

---

### P2-D: Add JSON-LD Schema Markup
**Effort:** 45 min | **Impact:** Critical — rich results eligibility

**index.html** — WebSite + Organization:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Lost Hills Online",
  "url": "https://yourdomain.com/",
  "description": "Official municipal information network of Lost Hills, Washington. Archive restored 2026.",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://yourdomain.com/?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
}
</script>
```

**conference.html** — Event:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Shadewater Applied Systems Conference 1993",
  "startDate": "1993-05-17",
  "endDate": "1993-05-21",
  "location": {
    "@type": "Place",
    "name": "Sezzler Lost Hills Conference Resort",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "1 Civic Center Way",
      "addressLocality": "Lost Hills",
      "addressRegion": "WA"
    }
  },
  "organizer": {
    "@type": "Organization",
    "name": "Shadewater Laboratories"
  },
  "description": "Five-day civic technology expo. The Future Works Here.",
  "eventStatus": "https://schema.org/EventScheduled",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode"
}
</script>
```

**mofa.html** — Museum + Exhibit:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Museum",
  "name": "Lost Hills Museum of Fine Art",
  "url": "https://yourdomain.com/mofa.html"
}
</script>
```

---

### P2-E: Fix Encoding Issues in 3 Pages
**Effort:** 5 min | **Impact:** Warning

`directory.html`, `links.html`, `sezzler.html` returned binary matches on grep, suggesting non-UTF-8 encoding or BOM. Re-save as UTF-8 (no BOM) in your editor.

---

## P3 — Nice to Have

### P3-A: Create llms.txt (Optional — AI search readiness)
```
# Lost Hills Online

> Lost Hills Online is a restored archive of the City of Lost Hills, Washington municipal information network (CityNet), originally launched May 1993 in partnership with Shadewater Laboratories. The archive was placed in emergency standby on May 22, 1993 and has since been restored.

## Public Pages
- [Home](https://yourdomain.com/)
- [1993 Systems Conference](https://yourdomain.com/conference.html)
- [About Lost Hills](https://yourdomain.com/about.html)
- [Shadewater Labs](https://yourdomain.com/shadewater.html)
- [Sezzler Resort](https://yourdomain.com/sezzler.html)
- [News Archive](https://yourdomain.com/news.html)

## Note
This site is a work of interactive fiction. Archive inconsistencies are intentional.
```

### P3-B: Improve Short Titles
Expand generic titles:
- `Lost Hills Online :: Home` → `Lost Hills Online — City of Lost Hills, WA Municipal Archive`
- `Lost Hills Online :: MOFA` → `Lost Hills Museum of Fine Art (MOFA) — Lost Hills Online`
- `Lost Hills Online :: Local Links` → `Local Links — Lost Hills Online CityNet Directory`

### P3-C: Consider a Dedicated "What Is This?" Page
An out-of-fiction landing page (or a very subtle in-fiction breadcrumb) that explains the project for SEO purposes. Currently the site has no content that would rank for searches like "Lost Hills ARG" or "Lost Hills interactive fiction" — the fiction is total but the discoverability relies entirely on people already knowing to search for it.

---

## Quick-Win Checklist (Before Launch)

- [ ] `lang="en"` on all `<html>` tags (find-replace, 5 min)
- [ ] Fix viewport meta to `width=device-width, initial-scale=1` (find-replace, 10 min)
- [ ] Remove blank `<img src="" alt="">` tags (find-replace, 5 min)
- [ ] Add meta descriptions to all 12 pages (30 min)
- [ ] Create `robots.txt` (5 min)
- [ ] Create `sitemap.xml` (10 min)
- [ ] Fix H1 structure sitewide (30 min)
- [ ] Add canonical tags (15 min)

**Total estimated effort for all P1 items: ~2 hours**

