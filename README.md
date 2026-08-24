# Deepak Thapliyal — Hindu Priest UK Website

A static, single-page website for Hindu priest **Deepak Thapliyal**, styled with a
glossy maroon-and-marigold temple theme (deep maroon, sindoor red, marigold gold).

## Files

```
index.html      Main page (all sections)
styles.css      All styling
script.js       Nav toggle, testimonial carousel, scroll reveal, form demo
images/         All placeholder graphics (SVG)
```

## Photos

Real photos of Deepak Thapliyal are already in place across the hero, about,
feature and gallery sections (`images/photo-*.jpg`). To swap any of them for a
different shot, just replace the file with a new image of the same name (or
update the `src` attribute in `index.html` to point at your new file).

- `photo-hero-portrait.jpg` — hero banner, arch frame (portrait orientation works best)
- `photo-about-main.jpg` / `photo-about-float.jpg` — About section pair
- `photo-feature-wedding.jpg` / `photo-feature-destination.jpg` — the two alternating feature rows
- `photo-gallery-1.jpg` through `photo-gallery-8.jpg` — gallery grid (square crop, any orientation works — they're auto-cropped to fit)

The blog article thumbnails (`article-*.svg`) are still decorative placeholder
graphics — swap these for real article images the same way once the articles
are written.

## Editing content

Everything is in plain HTML/CSS — no build tools or frameworks needed.

- Text, services, testimonials, contact info: edit directly in `index.html`.
- Colors, fonts, spacing: edit the `:root` variables at the top of `styles.css`.
- Phone number / WhatsApp link / email: search for `+44 1234 567 890` and
  `info@deepakthapliyal.co.uk` in `index.html` and replace with real details.

## Running locally

Just open `index.html` in a browser — no server required. For local development
with live reload, you can also run:

```
python3 -m http.server 8000
```

and visit `http://localhost:8000`.

## Deploying

Upload the whole folder to any static host — Netlify, Vercel, GitHub Pages,
or a standard web host via FTP. No backend is required for the site to display;
the contact form currently shows a confirmation message only (see `script.js`)
and should be wired up to an email service (e.g. Formspree, Netlify Forms) or
your own backend before going live.
