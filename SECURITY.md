# Security

## Reporting

Report security issues privately through the maintainer's GitHub profile. Do not publish exploit details in public issues.

## Scope

This is a static site, so the main concerns are:

- Unexpected script behavior in `site.js`
- Unsafe external links
- Exposed material under `restricted/`
- Deployment configuration
- Third-party embeds, if added later

## Maintenance

Keep the static surface simple. Avoid adding remote scripts unless they are necessary and reviewed.
