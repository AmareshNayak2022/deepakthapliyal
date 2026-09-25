# Acharya Deepak Thapliyal — Pandit in UAE

A static, single-page website for **Acharya Deepak Thapliyal**, Hindu pandit and purohit
serving **Dubai, Abu Dhabi and Sharjah**, styled with a glossy maroon-and-marigold temple
theme. Built for the domain **deepakthapliyal.com**, hosted on GitLab Pages.

## Files

```
index.html       Main page (all sections) + SEO meta + JSON-LD structured data
styles.css       All styling
script.js        Nav toggle, testimonial carousel, scroll reveal, WhatsApp enquiry form
robots.txt       Crawler rules + sitemap pointer
sitemap.xml      Single-URL sitemap for Google Search Console
.gitlab-ci.yml   GitLab Pages deploy pipeline
images/          Photos and decorative graphics
```

## Contact details used across the site

| Purpose   | Number             | Notes                        |
|-----------|--------------------|------------------------------|
| Primary   | +91 94107 70925    | Also the WhatsApp number     |
| UAE       | +971 50 827 3876   | Local UAE line               |
| Secondary | +44 7350 254563    | United Kingdom               |

Email: `dthapliyal2011@gmail.com`
Address: Flat 601, Block-A, Al Reem Tower (Amisa Showroom Building), Electra Street, TCA, Abu Dhabi

To change a number, search `index.html` for the digits and update both the `tel:` href and
the visible text. The WhatsApp number also appears as `WHATSAPP_NUMBER` at the top of the
contact-form handler in `script.js`, and in the `wa.me/` links in `index.html`.

## The contact form

There is no backend. On submit, the form composes the enquiry (name, phone, email, city,
ceremony, message) and opens WhatsApp with it pre-filled — so enquiries arrive as a chat
rather than an email. To switch to email instead, replace the submit handler in `script.js`
with a Formspree (or similar) endpoint.

## SEO

Targeted at "pandit in UAE / Dubai / Abu Dhabi / Sharjah" searches:

- Keyword-led `<title>`, meta description and H1/H2 headings
- `LocalBusiness` + `ProfessionalService` + `Person` + `FAQPage` JSON-LD in `<head>`,
  covering the address, all three phone numbers, service catalogue and areas served
- A dedicated **UAE Cities** section with genuine per-city content (the strongest on-page
  signal for local searches)
- An FAQ section whose questions mirror how people actually search
- Open Graph + Twitter cards, canonical URL, geo meta tags, `robots.txt`, `sitemap.xml`
- Descriptive, keyword-bearing image `alt` text and lazy loading below the fold

**Off-page work still required** — on-page SEO alone will not win the top spot:

1. Create a **Google Business Profile** for Abu Dhabi and verify it. This is what populates
   the map pack, which is what most "pandit near me" searches actually return.
2. Submit the site to **Google Search Console** and request indexing of `sitemap.xml`.
3. Collect **Google reviews** from families served in the UAE.
4. Get listed in UAE Indian-community directories and temple/community pages (backlinks).
5. Publish the six article stubs as real pages — each one is a separate chance to rank.

## Editing content

Everything is plain HTML/CSS — no build tools or frameworks.

- Text, services, cities, FAQ, testimonials: edit directly in `index.html`.
- Colors, fonts, spacing: edit the `:root` variables at the top of `styles.css`.
- Replace a photo by dropping a new image over the same filename in `images/`.

## Running locally

Open `index.html` in a browser — no server required. For live development:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## Deploying to GitLab Pages

1. Push this repository to GitLab. `.gitlab-ci.yml` runs on the default branch and copies
   the site into `public/`, which GitLab Pages serves.
2. **Settings → Pages** shows the generated URL once the first pipeline succeeds.
3. **Deploy → Pages → New domain** — add `deepakthapliyal.com`.
4. At your domain registrar, add the two DNS records GitLab shows you: an `A` record for the
   apex domain and the `_gitlab-pages-verification-code` `TXT` record. Add a `CNAME` for
   `www` pointing at your Pages host if you want the www version too.
5. Wait for verification, then enable **Force HTTPS**.

If the domain ever changes, update the absolute URLs in the `<head>` of `index.html`
(canonical, Open Graph, JSON-LD) and in `sitemap.xml` / `robots.txt`.
