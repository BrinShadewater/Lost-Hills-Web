# Maintenance

## Routine Preview

```shell
npx serve .
```

Open the printed local URL and review changed pages in a browser.

## Link Hygiene

When adding or renaming pages:

- Update navigation links.
- Update relevant cross-links.
- Update `sitemap.xml` for public pages.
- Check relative asset paths.

## Asset Handling

Keep assets descriptive and stable. Prefer WebP for site imagery. If an image is meant to feel period-authentic, preserve that visual logic while still keeping file sizes reasonable.

## Content Tone

Lost Hills works best when the site behaves as if it is not performing. Keep pages civic, local, and matter-of-fact. Avoid explaining the fiction inside the fiction.

## Deployment Notes

The repo includes `vercel.json`. Confirm canonical host and static routing before changing deployment configuration.
