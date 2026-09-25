"""Generate a dedicated landing page per UAE city.

A single page cannot rank for "pandit in Dubai", "pandit in Abu Dhabi" and
"pandit in Sharjah" at once — competitors each run a separate page per city
and per puja. These pages give every city its own URL, title, description,
heading, schema and genuinely distinct copy (thin near-duplicate pages get
filtered, so nothing here is boilerplate with the city name swapped).

Output: pandit-in-<slug>/index.html, served at
https://deepakthapliyal.com/pandit-in-<slug>/

Run:  python build-city-pages.py
"""

import io
import os

SITE = "https://deepakthapliyal.com"

WA = ("https://wa.me/919410770925?text="
      "Namaste%20Acharya%20Ji%2C%20I%20would%20like%20to%20book%20a%20puja%20in%20")

WA_SVG = ('<svg viewBox="0 0 32 32" class="icon-sm" aria-hidden="true"><path d="M16.04 3C8.86 3 3.02 8.84 3.02 '
          '16.02c0 2.29.6 4.53 1.75 6.5L3 29l6.65-1.74a12.95 12.95 0 0 0 6.39 1.67h.01c7.18 0 13.02-5.84 '
          '13.02-13.02 0-3.48-1.36-6.75-3.82-9.21A12.92 12.92 0 0 0 16.04 3zm0 23.73h-.01c-1.99 0-3.94-.54-5.64'
          '-1.55l-.4-.24-4.2 1.1 1.12-4.1-.26-.42a10.7 10.7 0 0 1-1.65-5.7c0-5.96 4.86-10.82 10.83-10.82 2.89 0 '
          '5.61 1.13 7.65 3.18a10.75 10.75 0 0 1 3.17 7.66c0 5.97-4.85 10.89-10.61 10.89zm5.95-8.11c-.33-.16-1.93'
          '-.95-2.23-1.06-.3-.11-.52-.16-.73.17-.22.32-.84 1.05-1.03 1.27-.19.22-.38.24-.7.08-.33-.16-1.38-.51'
          '-2.62-1.62-.97-.86-1.62-1.93-1.81-2.25-.19-.33-.02-.5.14-.66.15-.15.33-.38.49-.58.16-.19.22-.33.33-.55'
          '.11-.22.05-.41-.03-.58-.08-.16-.73-1.76-1-2.41-.26-.63-.53-.55-.73-.56l-.62-.01c-.22 0-.58.08-.88.41'
          '-.3.33-1.15 1.13-1.15 2.75s1.18 3.19 1.34 3.41c.16.22 2.32 3.54 5.62 4.96.79.34 1.4.54 1.87.7.79.25 '
          '1.5.21 2.07.13.63-.09 1.93-.79 2.2-1.55.27-.76.27-1.42.19-1.55-.08-.14-.3-.22-.63-.38z"/></svg>')

SERVICE_LINKS = [
    ("griha-pravesh-puja", "Griha Pravesh Puja"),
    ("satyanarayan-katha", "Satyanarayan Katha"),
    ("hindu-wedding-pandit", "Hindu Wedding"),
    ("havan-puja", "Havan & Fire Rituals"),
    ("kundali-matching", "Kundali Matching"),
    ("mata-ki-chowki", "Mata Ki Chowki"),
]

CITIES = [
    {
        "slug": "dubai",
        "name": "Dubai",
        "title": "Pandit in Dubai | Hindu Priest for Puja, Havan & Wedding — Acharya Deepak Thapliyal",
        "desc": ("Book an experienced Hindu pandit in Dubai for griha pravesh, Satyanarayan Katha, havan, "
                 "Ganesh puja and Vedic weddings. Acharya Deepak Thapliyal serves Bur Dubai, Karama, Deira, "
                 "Al Barsha, JLT and Dubai Marina. Call +971 50 827 3876."),
        "kw": ("pandit in Dubai, Hindu priest Dubai, pandit ji Dubai, purohit Dubai, pujari in Dubai, "
               "griha pravesh puja Dubai, Satyanarayan Katha Dubai, havan Dubai, Hindu wedding priest Dubai, "
               "Indian pandit Bur Dubai, pandit Karama, pandit Al Barsha"),
        "lede": ("A Hindu pandit serving families right across Dubai — from a quiet griha pravesh in a "
                 "Marina apartment to a full Vedic wedding in a hotel banquet hall."),
        "body": [
            ("Dubai keeps its own rhythm. Ceremonies here are booked around work shifts and school runs, often "
             "at short notice, and just as often in an apartment rather than a family home with a courtyard. "
             "<strong>Acharya Deepak Thapliyal</strong> has shaped his practice around that reality: early "
             "morning muhurats before the working day, evening pujas once families are home, and a samagri list "
             "sent ahead on WhatsApp so nothing has to be hunted down at the last minute."),
            ("The most frequent request in Dubai is <strong>griha pravesh</strong>. New arrivals moving into a "
             "flat in Al Barsha, JLT, Silicon Oasis or Business Bay want the home blessed before the first night "
             "is spent in it. A full griha pravesh with havan runs about ninety minutes; where building rules or "
             "smoke alarms make an open fire impractical, the havan is adapted so the rite is completed properly "
             "without setting off half the tower. That judgement — knowing what can be adjusted and what "
             "genuinely cannot — comes from having done it many times over."),
            ("For weddings, Acharya Ji conducts the complete <strong>vivah sanskar</strong>, from mandap muhurat "
             "and ganesh puja through kanyadaan, saptapadi and the vidai, narrating each step in Hindi and "
             "English as it happens so that guests who never learned Sanskrit still follow what is being "
             "promised. He works comfortably alongside hotel banqueting teams and wedding planners, and is "
             "familiar with the practicalities of venues across the emirate."),
        ],
        "areas": ["Bur Dubai", "Karama", "Deira", "Al Barsha", "JLT", "Dubai Marina", "Silicon Oasis",
                  "Business Bay", "International City", "Discovery Gardens", "Jumeirah", "Al Quoz",
                  "Mirdif", "Dubai Hills", "Jebel Ali"],
        "pujas": [
            ("🏠", "Griha Pravesh", "Blessing a new Dubai apartment or villa before you move in — the most booked ceremony in the emirate."),
            ("📖", "Satyanarayan Katha", "The full katha and puja, commonly held on a Purnima or after a family milestone."),
            ("💍", "Vivah — Hindu Wedding", "Complete Vedic wedding rites, conducted at hotels, banquet halls and private venues."),
            ("🔥", "Havan &amp; Fire Rituals", "Purification havan arranged safely for apartment living, with smoke kept manageable."),
            ("🐘", "Ganesh Puja", "The first invocation before a new home, new business or any auspicious beginning."),
            ("🕊️", "Antim Sanskar", "Compassionate guidance through funeral rites and the thirteen-day observances."),
        ],
        "faq": [
            ("How quickly can a pandit come for a puja in Dubai?",
             "Often within a day or two, and sometimes the same day for a simple puja. Griha pravesh and "
             "weddings are best booked further ahead so the muhurat can be chosen properly rather than forced."),
            ("Can a havan be performed inside a Dubai apartment?",
             "Yes. Many towers restrict open flame or have sensitive smoke detectors, so the havan is adapted — "
             "a smaller kund, controlled samagri, and ventilation arranged beforehand. The rite is completed in "
             "full; only the scale of the fire changes."),
            ("Do you travel to venues outside central Dubai?",
             "Yes — across the whole emirate including Jebel Ali, Mirdif, Dubai Hills and the outer communities, "
             "and on to Abu Dhabi and Sharjah."),
            ("Which languages will the ceremony be in?",
             "Mantras in Sanskrit, with the meaning explained as it goes in Hindi and English so every "
             "generation present understands the ritual."),
        ],
    },
    {
        "slug": "abu-dhabi",
        "name": "Abu Dhabi",
        "title": "Pandit in Abu Dhabi | Hindu Priest & Jyotish — Acharya Deepak Thapliyal, Electra Street",
        "desc": ("Hindu pandit based in Abu Dhabi at Al Reem Tower, Electra Street (TCA). Puja, havan, griha "
                 "pravesh, Satyanarayan Katha, kundali matching and horoscope analysis across TCA, Khalidiya, "
                 "Al Reem Island, Mussafah and Khalifa City. Call +971 50 827 3876."),
        "kw": ("pandit in Abu Dhabi, Hindu priest Abu Dhabi, purohit Abu Dhabi, pandit ji Abu Dhabi, "
               "astrologer in Abu Dhabi, jyotish Abu Dhabi, kundali matching Abu Dhabi, griha pravesh Abu Dhabi, "
               "pandit Electra Street, pandit TCA Abu Dhabi, pandit Khalidiya, pandit Mussafah"),
        "lede": ("Acharya Deepak Thapliyal is based in Abu Dhabi — available at short notice for puja at home, "
                 "and for jyotish consultations in person."),
        "body": [
            ("Abu Dhabi is home. Acharya Ji lives at <strong>Al Reem Tower, Electra Street (TCA)</strong>, which "
             "means families here are not waiting on someone travelling in from another emirate. A puja can "
             "often be arranged the same day, and for bereavements — where waiting is the last thing a family "
             "needs — he can usually be there within hours."),
            ("Being based in the city also makes <strong>jyotish consultation</strong> practical in a way it "
             "rarely is elsewhere. As a qualified <strong>Jyotishacharya</strong>, Acharya Ji reads janam "
             "patrika for marriage, career, health and property decisions, and performs <strong>Patrika Milan</strong> "
             "(kundali matching) for families weighing a proposal. These are conversations, not pronouncements: "
             "he explains what the chart indicates, what it does not, and which remedies are worth the effort "
             "against which are not. Consultations are held in person in Abu Dhabi, or online for families "
             "spread between the Emirates and India."),
            ("Alongside the rituals, he is a <strong>katha vachak</strong> and a Sangeet Prabhakar — a trained "
             "devotional singer. Musical Sunderkand, Bhajan Sandhya and Akhand Ramayan are led personally with "
             "harmonium rather than played from a recording, which is what turns an evening of prayer into "
             "something the whole building remembers."),
        ],
        "areas": ["TCA", "Electra Street", "Hamdan Street", "Khalidiya", "Al Reem Island", "Mussafah",
                  "Khalifa City", "Al Raha", "Al Bateen", "Corniche", "Yas Island", "Saadiyat",
                  "Mohammed Bin Zayed City", "Al Ain", "Baniyas"],
        "pujas": [
            ("✨", "Janam Patrika Vishleshan", "Detailed horoscope analysis with dasha readings, timing and practical remedies."),
            ("💞", "Patrika Milan", "Kundali matching for marriage — guna milan, mangal dosha and clear guidance."),
            ("🎶", "Musical Sunderkand", "Sunderkand paath sung live with harmonium — a Sangeet Prabhakar's speciality."),
            ("🏠", "Griha Pravesh", "Housewarming rites for a new apartment or villa anywhere in the capital."),
            ("📖", "Satyanarayan Katha", "The devotional katha and puja, performed for gratitude and good fortune."),
            ("🔱", "Navratri Paath", "Durga Saptashati paath and the nine nights observed in full, with daily aarti."),
        ],
        "faq": [
            ("Where exactly is Acharya Ji based in Abu Dhabi?",
             "Flat 601, Block-A, Al Reem Tower (Amisa Showroom Building), Electra Street, TCA, Abu Dhabi. "
             "Being in the city means short notice bookings are usually possible."),
            ("Can I get a kundali matching done in person?",
             "Yes. Patrika Milan and full horoscope analysis are done face to face in Abu Dhabi, which is far "
             "better for a real discussion than a report sent over email. Online consultations are available "
             "when the family is spread across countries."),
            ("Do you cover Al Ain and the wider emirate?",
             "Yes — Al Ain, Khalifa City, Mussafah, Yas and Saadiyat are all covered, with travel arranged by "
             "prior notice."),
            ("Can you help urgently with funeral rites?",
             "Yes. Antim sanskar and the thirteen-day observances are handled with care and, being based in the "
             "city, he can usually attend at short notice."),
        ],
    },
    {
        "slug": "sharjah",
        "name": "Sharjah",
        "title": "Pandit in Sharjah | Hindu Priest for Mata Ki Chowki, Bhajan &amp; Puja — Acharya Deepak Thapliyal",
        "desc": ("Book a Hindu pandit in Sharjah for Mata Ki Chowki, Bhajan Sandhya, Akhand Ramayan, griha "
                 "pravesh and family pujas. Serving Al Nahda, Al Majaz, Al Qasimia, Muweilah and Rolla. "
                 "Call +971 50 827 3876."),
        "kw": ("pandit in Sharjah, Hindu priest Sharjah, purohit Sharjah, pandit ji Sharjah, "
               "mata ki chowki Sharjah, bhajan sandhya Sharjah, akhand ramayan Sharjah, griha pravesh Sharjah, "
               "pandit Al Nahda, pandit Al Majaz, pandit Rolla Sharjah"),
        "lede": ("A Hindu pandit for Sharjah families — devotional evenings, family pujas and full ceremonies, "
                 "with all samagri brought along."),
        "body": [
            ("Sharjah has a settled, close Indian community, and the ceremonies families ask for here reflect "
             "that. Where Dubai books griha pravesh for people newly arrived, Sharjah books the gatherings that "
             "bring neighbours and extended family into one room: <strong>Mata Ki Chowki</strong>, "
             "<strong>Bhajan Sandhya</strong>, <strong>Akhand Ramayan</strong> and the annual observances "
             "families have kept for years."),
            ("Acharya Deepak Thapliyal leads these himself. As a <strong>Sangeet Prabhakar</strong> — a trained "
             "devotional musician — the chowki and the bhajan sandhya are sung live with harmonium, with the "
             "room drawn into the singing rather than listening to a recording. An Akhand Ramayan, the unbroken "
             "recitation of the Ramcharitmanas, is organised end to end: the sthapana, the reading rota through "
             "the night, and the closing havan and bhog the following day."),
            ("Everyday rites are equally at home here — Satyanarayan Katha, Ganesh puja, namkaran, birthday "
             "pujan and griha pravesh for apartments and villas across Al Nahda, Al Majaz and Muweilah. Samagri "
             "is brought along or a complete list is shared in advance, so families are not sent hunting around "
             "Rolla the evening before."),
        ],
        "areas": ["Al Nahda", "Al Majaz", "Al Qasimia", "Muweilah", "Rolla", "Al Taawun", "Al Khan",
                  "Abu Shagara", "Al Nabba", "Butina", "University City", "Al Yarmook",
                  "Industrial Area", "Ajman (nearby)", "Al Riqqa"],
        "pujas": [
            ("🪔", "Mata Ki Chowki", "A night of jagran and devotion to the Mother Goddess, with chowki sthapana and aarti."),
            ("🪕", "Bhajan Sandhya", "An evening of devotional singing led live — festivals, anniversaries, family gatherings."),
            ("📿", "Akhand Ramayan", "Unbroken recitation of the Ramcharitmanas, organised from sthapana to closing bhog."),
            ("📖", "Satyanarayan Katha", "The full katha and puja, a Sharjah family favourite for thanksgiving."),
            ("🏠", "Griha Pravesh", "Housewarming rites for apartments and villas across the emirate."),
            ("👶", "Namkaran &amp; Mundan", "Naming ceremonies and first-haircut rites to welcome a new child."),
        ],
        "faq": [
            ("Do you bring the samagri for a Mata Ki Chowki in Sharjah?",
             "Yes. For a chowki or bhajan sandhya everything needed is brought along, or a complete list is "
             "shared in advance if you prefer to arrange it yourself."),
            ("Is the bhajan singing live?",
             "Yes — Acharya Ji is a Sangeet Prabhakar and sings with harmonium himself. Nothing is played from "
             "a recording."),
            ("How long does an Akhand Ramayan take to arrange?",
             "It runs continuously for about twenty-four hours, so a week or two of notice is ideal to organise "
             "the reading rota and the closing havan and bhog."),
            ("Do you cover Ajman as well?",
             "Yes — Ajman is close by and covered by prior arrangement, as are the other northern emirates."),
        ],
    },
]


def esc(t):
    return t


def build(city):
    slug, name = city["slug"], city["name"]
    url = f"{SITE}/pandit-in-{slug}/"
    wa = WA + name.replace(" ", "%20") + "."

    faq_json = ",\n".join(
        '        {{ "@type": "Question", "name": "{q}", "acceptedAnswer": {{ "@type": "Answer", "text": "{a}" }} }}'
        .format(q=q.replace('"', "'"), a=a.replace("<strong>", "").replace("</strong>", "").replace('"', "'"))
        for q, a in city["faq"]
    )

    pujas_html = "\n".join(
        f'''      <article class="service-card">
        <div class="service-icon" aria-hidden="true">{icon}</div>
        <h3>{t}</h3>
        <p>{d}</p>
      </article>''' for icon, t, d in city["pujas"]
    )

    areas_html = "".join(f"<li>{a}</li>" for a in city["areas"])

    body_html = "\n".join(f"      <p>{p}</p>" for p in city["body"])

    faq_html = "\n".join(
        f'''      <details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in city["faq"]
    )

    service_links = "".join(
        f'<li><a href="../{sl}/">{nm}</a></li>' for sl, nm in SERVICE_LINKS
    )

    others = "".join(
        f'<li><a href="../pandit-in-{c["slug"]}/">Pandit in {c["name"]}</a></li>'
        for c in CITIES if c["slug"] != slug
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{city["title"]}</title>
<meta name="description" content="{city["desc"]}">
<meta name="keywords" content="{city["kw"]}">
<meta name="author" content="Acharya Deepak Thapliyal">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta name="geo.region" content="AE">
<meta name="geo.placename" content="{name}">
<meta property="og:type" content="website">
<meta property="og:title" content="{city["title"]}">
<meta property="og:description" content="{city["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/photo-hero-portrait.jpg">
<meta property="og:locale" content="en_AE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{city["title"]}">
<meta name="twitter:description" content="{city["desc"]}">
<meta name="twitter:image" content="{SITE}/images/photo-hero-portrait.jpg">
<meta name="theme-color" content="#2B0808">
<link rel="icon" href="../images/logo-mark.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Marcellus&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Work+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../styles.css">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": ["LocalBusiness", "ProfessionalService"],
      "@id": "{url}#business",
      "name": "Acharya Deepak Thapliyal — Pandit in {name}",
      "description": "{city["desc"]}",
      "url": "{url}",
      "image": "{SITE}/images/photo-hero-portrait.jpg",
      "telephone": "+919410770925",
      "email": "dthapliyal2011@gmail.com",
      "priceRange": "$$",
      "address": {{
        "@type": "PostalAddress",
        "streetAddress": "Flat no. 601, Block-A, Al Reem Tower, Electra Street, TCA",
        "addressLocality": "Abu Dhabi",
        "addressCountry": "AE"
      }},
      "areaServed": {{ "@type": "City", "name": "{name}" }},
      "sameAs": [
        "https://www.youtube.com/@deepakthapliyal",
        "https://www.facebook.com/Acharya-Deepak-Thapliyal-102544104784897"
      ],
      "parentOrganization": {{ "@id": "{SITE}/#business" }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "Pandit in {name}", "item": "{url}" }}
      ]
    }},
    {{
      "@type": "FAQPage",
      "mainEntity": [
{faq_json}
      ]
    }}
  ]
}}
</script>
</head>
<body>

<div class="toran-strip" aria-hidden="true"></div>

<div class="announce-bar">
  <p>
    <span class="announce-dot" aria-hidden="true"></span>
    <strong>Serving {name}</strong> — puja, havan and ceremonies at your home or venue.
    <a href="tel:+971508273876">Call +971 50 827 3876</a>
  </p>
</div>

<header class="site-header" id="header">
  <div class="header-inner">
    <a href="../" class="brand">
      <img src="../images/logo-mark.svg" alt="Acharya Deepak Thapliyal monogram" class="brand-mark" width="46" height="46">
      <span class="brand-text">
        <span class="brand-name">Acharya Deepak Thapliyal</span>
        <span class="brand-sub">Pandit &amp; Purohit &middot; {name}</span>
      </span>
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Main navigation">
      <ul>
        <li><a href="../">Home</a></li>
        <li><a href="../#about">About</a></li>
        <li><a href="../#services">Services</a></li>
        <li><a href="../#youtube">YouTube</a></li>
        <li><a href="../#contact">Contact</a></li>
      </ul>
    </nav>
    <div class="header-actions">
      <a href="tel:+919410770925" class="phone-pill">
        <svg viewBox="0 0 24 24" class="icon-sm" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.7 5.1 6.5 6.5l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1.1.5 1.1 1.1v3.5c0 .6-.5 1.1-1.1 1.1C10.6 21.2 2.8 13.4 2.8 3.1 2.8 2.5 3.3 2 3.9 2h3.5c.6 0 1.1.5 1.1 1.1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1L6.6 10.8z"/></svg>
        <span>+91 94107 70925</span>
      </a>
      <button class="menu-toggle" id="menu-toggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<section class="hero city-hero" id="home">
  <div class="hero-bg-glow" aria-hidden="true"></div>
  <div class="hero-mandala" aria-hidden="true"></div>
  <div class="section-inner">
    <nav class="crumbs" aria-label="Breadcrumb">
      <a href="../">Home</a> <span aria-hidden="true">&rsaquo;</span> <span>Pandit in {name}</span>
    </nav>
    <p class="eyebrow"><span class="om">ॐ</span> Namaste &amp; Welcome</p>
    <h1>Pandit in {name}</h1>
    <p class="hero-lede">{city["lede"]}</p>
    <div class="hero-ctas">
      <a href="{wa}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp Now</a>
      <a href="tel:+971508273876" class="btn btn-gold">Call +971 50 827 3876</a>
    </div>
  </div>
</section>

<div class="toran-strip flip" aria-hidden="true"></div>

<section class="about city-intro">
  <div class="section-inner narrow">
    <p class="eyebrow">Ceremonies in {name}</p>
    <h2>Vedic Rituals, Performed the Way They Should Be</h2>
{body_html}
    <a href="../#about" class="text-link">More about Acharya Deepak Thapliyal &rarr;</a>
  </div>
</section>

<section class="services">
  <div class="section-inner">
    <div class="section-head center">
      <p class="eyebrow">Most Requested</p>
      <h2>Pujas Booked Most Often in {name}</h2>
    </div>
    <div class="services-grid city-pujas">
{pujas_html}
    </div>
  </div>
</section>

<section class="cities">
  <div class="section-inner">
    <div class="section-head center">
      <p class="eyebrow">Coverage</p>
      <h2>Areas Served Across {name}</h2>
      <p class="section-sub">Ceremonies performed at homes, villas, community halls and venues throughout the emirate.</p>
    </div>
    <ul class="area-chips">{areas_html}</ul>
    <div class="link-cols ceremonies-block">
      <div>
        <h3>Ceremonies Performed Here</h3>
        <ul class="link-list">{service_links}</ul>
      </div>
      <div>
        <h3>Other Cities</h3>
        <ul class="link-list">{others}</ul>
      </div>
    </div>
  </div>
</section>

<section class="faq">
  <div class="section-inner">
    <div class="section-head center">
      <p class="eyebrow">Common Questions</p>
      <h2>Booking a Pandit in {name}</h2>
    </div>
    <div class="faq-list">
{faq_html}
    </div>
  </div>
</section>

<section class="contact">
  <div class="hero-mandala small" aria-hidden="true"></div>
  <div class="section-inner narrow center-text">
    <p class="eyebrow">Get in Touch</p>
    <h2>Book a Pandit in {name}</h2>
    <p>Tell Acharya Ji the ceremony, the date and your area, and he will confirm the muhurat, the samagri needed and how long it will take.</p>
    <div class="phone-cards">
      <a class="phone-card primary" href="tel:+919410770925"><span class="pc-flag">Primary</span><strong>+91 94107 70925</strong><span class="pc-note">Call &amp; WhatsApp</span></a>
      <a class="phone-card" href="tel:+971508273876"><span class="pc-flag">UAE</span><strong>+971 50 827 3876</strong><span class="pc-note">Local UAE line</span></a>
      <a class="phone-card" href="tel:+447350254563"><span class="pc-flag">Secondary</span><strong>+44 7350 254563</strong><span class="pc-note">United Kingdom</span></a>
    </div>
    <a href="{wa}" class="btn btn-wa full-width" target="_blank" rel="noopener">{WA_SVG} Message on WhatsApp</a>
    <ul class="contact-details">
      <li><span class="ci">✉️</span> <a href="mailto:dthapliyal2011@gmail.com">dthapliyal2011@gmail.com</a></li>
      <li><span class="ci">🕉️</span> Maa Jwalpa Astrology Research Centre</li>
    </ul>
  </div>
</section>

<footer class="site-footer">
  <div class="toran-strip" aria-hidden="true"></div>
  <div class="section-inner footer-grid">
    <div class="footer-brand">
      <img src="../images/logo-mark.svg" alt="Acharya Deepak Thapliyal monogram" class="brand-mark" width="46" height="46" loading="lazy">
      <p class="footer-tagline">"A family full of love and cooperation is truly heaven on earth.<br>Be good, be happy, be kind."</p>
    </div>
    <div class="footer-col">
      <h4>Other Cities</h4>
      <ul>{others}<li><a href="../">All UAE services</a></li></ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <ul class="plain">
        <li><a href="tel:+919410770925">+91 94107 70925</a> <em>(primary)</em></li>
        <li><a href="tel:+971508273876">+971 50 827 3876</a> <em>(UAE)</em></li>
        <li><a href="mailto:dthapliyal2011@gmail.com">dthapliyal2011@gmail.com</a></li>
        <li>Electra Street, TCA, Abu Dhabi</li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; <span id="year"></span> Acharya Deepak Thapliyal — Hindu Pandit &amp; Purohit, {name}, UAE. All rights reserved.</p>
  </div>
</footer>

<a href="{wa}" class="whatsapp-fab" target="_blank" rel="noopener" aria-label="Chat with Acharya Ji on WhatsApp">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16.04 3C8.86 3 3.02 8.84 3.02 16.02c0 2.29.6 4.53 1.75 6.5L3 29l6.65-1.74a12.95 12.95 0 0 0 6.39 1.67h.01c7.18 0 13.02-5.84 13.02-13.02 0-3.48-1.36-6.75-3.82-9.21A12.92 12.92 0 0 0 16.04 3zm0 23.73h-.01c-1.99 0-3.94-.54-5.64-1.55l-.4-.24-4.2 1.1 1.12-4.1-.26-.42a10.7 10.7 0 0 1-1.65-5.7c0-5.96 4.86-10.82 10.83-10.82 2.89 0 5.61 1.13 7.65 3.18a10.75 10.75 0 0 1 3.17 7.66c0 5.97-4.85 10.89-10.61 10.89zm5.95-8.11c-.33-.16-1.93-.95-2.23-1.06-.3-.11-.52-.16-.73.17-.22.32-.84 1.05-1.03 1.27-.19.22-.38.24-.7.08-.33-.16-1.38-.51-2.62-1.62-.97-.86-1.62-1.93-1.81-2.25-.19-.33-.02-.5.14-.66.15-.15.33-.38.49-.58.16-.19.22-.33.33-.55.11-.22.05-.41-.03-.58-.08-.16-.73-1.76-1-2.41-.26-.63-.53-.55-.73-.56l-.62-.01c-.22 0-.58.08-.88.41-.3.33-1.15 1.13-1.15 2.75s1.18 3.19 1.34 3.41c.16.22 2.32 3.54 5.62 4.96.79.34 1.4.54 1.87.7.79.25 1.5.21 2.07.13.63-.09 1.93-.79 2.2-1.55.27-.76.27-1.42.19-1.55-.08-.14-.3-.22-.63-.38z"/></svg>
</a>

<script src="../script.js"></script>
</body>
</html>
'''


for city in CITIES:
    d = f'pandit-in-{city["slug"]}'
    os.makedirs(d, exist_ok=True)
    io.open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(build(city))
    print(f'  {d}/index.html  ({len(build(city))//1024} KB)')
