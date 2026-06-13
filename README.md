# Lost Hills Web 🏛️

Static website for **Lost Hills Online**, the restored municipal information network of Lost Hills, Washington.

The site is built as an in-world archive: city pages, public notices, local businesses, restricted records, civic infrastructure, and the visual texture of a dormant 1990s municipal web system brought back online. It should feel like somebody found a backup tape in a filing cabinet and decided the town deserved one more login prompt.

## 📟 What This Site Does

- Presents a fictional municipal web portal as if recovered from an old civic network.
- Collects public city pages, business listings, council material, conference pages, and community notices.
- Includes restricted/archive pages that deepen the world without making the repo hard to navigate.
- Uses static HTML/CSS/JS so the artifact stays portable and durable.
- Keeps the design language intentionally period-specific: banners, local ads, civic seals, tiled backgrounds, and practical page names.

## 🧰 Stack

- Static HTML
- CSS
- Vanilla JavaScript
- WebP image assets
- Vercel deployment configuration

## 🚦 Repository Status

Static production artifact. Most changes are content, visual texture, links, or deployment metadata.

## ⚙️ Local Preview

Because this is a static site, you can preview it with any local static server.

```shell
npx serve .
```

Then open the local URL printed by the command.

## 🗺️ Project Map

```text
index.html          Home page
*.html              Public city, directory, news, and civic pages
restricted/         In-world restricted archive pages
assets/             Images, ads, banners, seals, webcams, and texture assets
styles.css          Global visual system
site.js             Site behavior
robots.txt
sitemap.xml
vercel.json
```

## 🔦 Key Surfaces

- `index.html` sets the homepage and primary metadata.
- `styles.css` carries the period UI language.
- `site.js` contains site behavior; keep it small and easy to inspect.
- `restricted/` contains in-world archive material that should remain deliberate.
- `assets/` contains the site's visual identity and faux-local ephemera.

## 📚 Documentation

- `docs/PROJECT-BRIEF.md`
- `docs/MAINTENANCE.md`
- `README.md`
- `CONTRIBUTING.md`
- `SECURITY.md`
- `CHANGELOG.md`

## 🗄️ Content Notes

The fiction depends on the details. Preserve the municipal/archive tone, date logic, internal links, and deliberately period-specific texture when editing.

## 🚀 Deployment

The site is configured for static hosting. Keep canonical URLs, sitemap entries, and robots rules aligned with the deployed domain.

## ✅ Review Checklist

- Preview locally.
- Check changed links manually.
- Review image paths and alt text where present.
- Confirm new pages belong in `sitemap.xml`.
- Keep the tone bureaucratic, local, and restored rather than modernized.
