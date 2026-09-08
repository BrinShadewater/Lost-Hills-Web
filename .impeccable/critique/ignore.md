# Critique ignore list — adjudicated findings, do not re-raise

## The fixed 1000px layout, and the small type that comes with it

**Settled 2026-07-30 with Alex's approval. This is the intended design.**

The 2026-07-31 critique raised the viewport as a P1: `width=device-width` against a 1000px
min-width shell left a 375px window panning a 1000px page. That was a real defect and it was
fixed — by setting `content="width=1000"` across all fifteen pages, so a phone zooms out and
sees the whole page as one composed layout instead of panning a slice of it. That change shipped
in the 2026-07-30 polish, merged and deployed with Alex's approval.

What is easy to re-flag afterwards is the *result*: the site is not responsive, the type is
small on a phone, and no breakpoint exists. That is the point. Lost Hills Online is a
period-accurate late-1990s municipal site — table layout, Times New Roman, bevelled navigation
buttons, a marquee and a hit counter. A responsive rebuild would make it a modern site wearing a
retro skin, which is the one thing it must not be.

**Do not propose `width=device-width`, breakpoints, a fluid shell, larger base type, or a
"mobile version".** Do not score a mobile-usability heuristic down for the fixed width. If the
premise is ever revisited, that is Alex's call to reopen — not an audit finding.

Related, and also intentional: the tiny fonts and the `#507040` palette are part of the same
period joke. Note that a fixed `width=1000` viewport means `srcset` cannot help phones, because
candidates are chosen by raw device pixel ratio rather than the zoomed-out scale — only smaller
originals help, which is why the 156px sidebar-ad cards benefit from `srcset` and the full-width
content photos do not. That is a measurement fact, not a defect to fix.
