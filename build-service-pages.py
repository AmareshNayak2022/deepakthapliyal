"""Generate a dedicated page per puja.

The sites ranking for these searches run one page per ceremony — someone
searching "satyanarayan katha dubai" or "griha pravesh pandit uae" should
land on a page about that ritual, not a homepage that mentions it in a card.

Each page carries genuinely distinct, useful content: what the ritual is,
when it is performed, what it needs, how long it takes, and the practical
realities of doing it in the UAE. Thin pages that just repeat the service
name get filtered, so none of this is boilerplate.

Output: <slug>/index.html  ->  https://deepakthapliyal.com/<slug>/
Run:    python build-service-pages.py
"""

import io
import os

SITE = "https://deepakthapliyal.com"
WA = ("https://wa.me/919410770925?text="
      "Namaste%20Acharya%20Ji%2C%20I%20would%20like%20to%20book%20")

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

CITY_LINKS = [("pandit-in-dubai", "Dubai"), ("pandit-in-abu-dhabi", "Abu Dhabi"), ("pandit-in-sharjah", "Sharjah")]

SERVICES = [
    {
        "slug": "griha-pravesh-puja",
        "name": "Griha Pravesh Puja",
        "h1": "Griha Pravesh Puja in Dubai, Abu Dhabi &amp; Sharjah",
        "title": "Griha Pravesh Puja in UAE | Housewarming Pandit Dubai, Abu Dhabi, Sharjah",
        "desc": ("Book griha pravesh puja in Dubai, Abu Dhabi or Sharjah. Acharya Deepak Thapliyal performs the "
                 "full housewarming rite with vastu shanti and havan, adapted for UAE apartments. "
                 "Call +971 50 827 3876."),
        "kw": ("griha pravesh puja Dubai, griha pravesh Abu Dhabi, housewarming puja UAE, grah pravesh pandit, "
               "vastu shanti puja Dubai, new home puja UAE, pandit for house warming Dubai"),
        "lede": "The rite that blesses a new home before the first night is spent in it — the most requested ceremony in the UAE.",
        "duration": "90 minutes to 2½ hours",
        "best": "Morning, on an auspicious muhurat",
        "where": "Apartments, villas and new offices",
        "body": [
            ("Griha pravesh marks the moment a building becomes a home. Before a family sleeps in a new flat or "
             "villa, the space is cleansed, the household deities are welcomed, and the directions are settled "
             "through <strong>vastu shanti</strong>. In the UAE it is the ceremony families ask for most, "
             "because so many arrive into a new apartment each year."),
            ("The rite opens with <strong>Ganesh puja</strong> to clear obstacles, followed by "
             "<strong>kalash sthapana</strong> — a consecrated pot of water, mango leaves and a coconut placed "
             "at the threshold. <strong>Navgraha</strong> and <strong>vastu</strong> invocations settle the nine "
             "planets and the spirit of the dwelling. A <strong>havan</strong> is then performed, and the "
             "ceremony closes with milk boiled over on the new stove — the overflow signifying abundance — "
             "and the family's first meal cooked in the home."),
            ("There are three practical points specific to the Emirates. First, <strong>timing</strong>: "
             "handover dates slip, so the muhurat is chosen once you have keys in hand, not before. Second, "
             "<strong>the havan</strong>: many towers have sensitive smoke detectors and rules on open flame, so "
             "the fire is scaled to the space, with ventilation arranged and samagri chosen to keep smoke low — "
             "the rite is completed in full, only the scale changes. Third, <strong>samagri</strong>: a complete "
             "list is sent ahead on WhatsApp, and where it is easier, Acharya Ji brings it along."),
            ("It is worth doing the puja <em>before</em> moving furniture in where possible, though a home "
             "already occupied can absolutely still be blessed — many families book it weeks after moving, and "
             "that is perfectly acceptable."),
        ],
        "checklist": ["Kalash, coconut and mango leaves", "Fresh flowers and garlands", "Rice, haldi, kumkum, supari",
                      "Ghee, samidha and havan samagri", "Milk for the boiling-over rite", "Fruit and sweets for prasad",
                      "A photo or murti of your family deity"],
        "faq": [
            ("How long does a griha pravesh puja take?",
             "Between 90 minutes and about 2½ hours depending on whether a full havan and vastu shanti are included."),
            ("Can it be done in an apartment with smoke detectors?",
             "Yes. The havan is scaled to the space with ventilation arranged in advance and low-smoke samagri. "
             "The ritual is completed properly — only the size of the fire changes."),
            ("Should we do the puja before or after moving in?",
             "Before the first night in the home is traditional. If you have already moved in, the puja is still "
             "performed in full and is very commonly booked afterwards."),
            ("Do you bring the samagri?",
             "A complete list is shared in advance, and where it is easier for the family, everything needed can "
             "be brought along."),
        ],
    },
    {
        "slug": "satyanarayan-katha",
        "name": "Satyanarayan Katha",
        "h1": "Satyanarayan Katha in Dubai, Abu Dhabi &amp; Sharjah",
        "title": "Satyanarayan Katha in UAE | Book a Pandit in Dubai, Abu Dhabi, Sharjah",
        "desc": ("Book Satyanarayan Katha and puja in Dubai, Abu Dhabi or Sharjah. The full five-chapter katha "
                 "with havan and prasad, performed at your home by Acharya Deepak Thapliyal. "
                 "Call +971 50 827 3876."),
        "kw": ("satyanarayan katha Dubai, satyanarayan puja Abu Dhabi, satyanarayan katha UAE, "
               "satyanarayan swami vrat katha Sharjah, pandit for satyanarayan katha Dubai"),
        "lede": "The katha of Lord Vishnu in his Satyanarayan form — performed in thanksgiving, and at every new beginning.",
        "duration": "About 2 hours",
        "best": "Purnima, Ekadashi, or any auspicious day",
        "where": "Homes, community halls and temples",
        "body": [
            ("Satyanarayan Katha is the puja families turn to when something has gone well and they wish to give "
             "thanks — a new job, a new home, a wedding anniversary, a child's success, or a vow fulfilled. It "
             "is equally performed at beginnings, and it is among the most accessible of all Hindu rites: no "
             "elaborate preparation, no restriction on who may attend."),
            ("The ceremony begins with <strong>Ganesh puja</strong> and the invocation of the navagraha, "
             "followed by the <strong>kalash sthapana</strong> and the puja of Lord Satyanarayan. The heart of "
             "it is the <strong>katha</strong> itself — five chapters recounting how the vrat came to be "
             "observed, each ending in the reminder that a promise made to the divine must be kept. Acharya Ji "
             "narrates these in Hindi with the meaning drawn out in English, which is what keeps children and "
             "younger relatives genuinely listening rather than waiting for prasad."),
            ("It closes with <strong>aarti</strong> and the distribution of <strong>prasad</strong> — "
             "traditionally sheera (sooji halwa) made with ghee, semolina, sugar and banana, along with "
             "panchamrit. Families often keep the gathering small, though the katha works just as well with a "
             "full room; in Dubai and Sharjah it is frequently held in community halls so neighbours can join."),
            ("Traditionally observed on <strong>Purnima</strong> (full moon), but it may be performed on any "
             "auspicious day — Acharya Ji will advise a suitable date if you are unsure."),
        ],
        "checklist": ["Kalash with coconut and mango leaves", "Photo or murti of Lord Satyanarayan",
                      "Banana leaves and fresh flowers", "Panchamrit: milk, curd, ghee, honey, sugar",
                      "Sooji, ghee, sugar and banana for sheera prasad", "Fruit, betel leaves and supari",
                      "Kumkum, haldi, rice and incense"],
        "faq": [
            ("How long does Satyanarayan Katha take?",
             "About two hours including the puja, all five chapters of the katha, the havan and the aarti."),
            ("When should Satyanarayan Katha be performed?",
             "Purnima is traditional, and it is also performed after a milestone such as a new home, a new job, "
             "a wedding or the fulfilment of a vow. Any auspicious day is suitable."),
            ("How many people can attend?",
             "There is no restriction. It is held for a single family at home or for a large gathering in a "
             "community hall — both are common across the UAE."),
            ("What prasad is prepared?",
             "Sheera (sooji halwa) made with ghee, semolina, sugar and banana, along with panchamrit and fruit."),
        ],
    },
    {
        "slug": "hindu-wedding-pandit",
        "name": "Hindu Wedding Pandit",
        "h1": "Hindu Wedding Pandit in Dubai, Abu Dhabi &amp; Sharjah",
        "title": "Hindu Wedding Pandit in UAE | Vivah Ceremony Dubai, Abu Dhabi, Sharjah",
        "desc": ("Book a Hindu wedding pandit in Dubai, Abu Dhabi or Sharjah. Full Vedic vivah sanskar — mandap, "
                 "kanyadaan, saptapadi — narrated in Hindi and English by Acharya Deepak Thapliyal. "
                 "Call +971 50 827 3876."),
        "kw": ("Hindu wedding pandit Dubai, vivah pandit UAE, wedding priest Abu Dhabi, Hindu marriage ceremony "
               "Dubai, pandit for wedding Sharjah, Vedic wedding UAE, mandap pandit Dubai"),
        "lede": "The complete vivah sanskar, conducted so that both families understand every vow as it is made.",
        "duration": "2 to 4 hours for the main ceremony",
        "best": "On a muhurat chosen from both horoscopes",
        "where": "Hotels, banquet halls, villas and temples",
        "body": [
            ("A wedding priest's work is not only to recite correctly — it is to make sure the couple and both "
             "families understand what is being promised. Acharya Deepak Thapliyal conducts the full "
             "<strong>vivah sanskar</strong> across North Indian, Garhwali and Gujarati traditions, narrating "
             "each stage in Hindi and English as it unfolds. Guests who never learned Sanskrit follow the "
             "ceremony rather than sit through it."),
            ("The ceremony moves through <strong>Ganesh puja</strong> and <strong>mandap muhurat</strong>, the "
             "welcoming of the groom at <strong>milni</strong>, <strong>kanyadaan</strong>, the "
             "<strong>vivah homa</strong> before the sacred fire, <strong>panigrahan</strong> (the taking of "
             "hands), the four <strong>mangal pheras</strong>, <strong>saptapadi</strong> — the seven steps, "
             "each a distinct vow — and then <strong>sindoor daan</strong> and <strong>mangalsutra</strong>, "
             "closing with the blessings of the elders and <strong>vidai</strong>."),
            ("Practically, Acharya Ji works alongside hotel banqueting teams and wedding planners across the "
             "Emirates and is used to venue timings, fire restrictions and the tight turnarounds that come with "
             "them. Where an open fire is not permitted indoors, the homa is arranged to comply while keeping "
             "the rite complete. A <strong>muhurat</strong> is chosen from both horoscopes, and pre-wedding "
             "rites — <strong>ganesh puja</strong>, <strong>mata ki chowki</strong>, "
             "<strong>haldi</strong>, <strong>grah shanti</strong> and <strong>mehendi</strong> ceremonies — "
             "can be arranged across the preceding days."),
            ("One thing worth knowing: the religious ceremony and the <strong>legal registration</strong> of a "
             "marriage in the UAE are separate processes. Acharya Ji performs the sacrament; couples should "
             "arrange registration and any attestation through the appropriate authority or their consulate."),
        ],
        "checklist": ["Mandap and havan kund (often via the venue or decorator)", "Mangalsutra, sindoor and rings",
                      "Garlands for jaimala", "Coconut, rice, haldi, kumkum and supari",
                      "Ghee, samidha and havan samagri", "Sweets and fruit for prasad",
                      "Birth details of both bride and groom for the muhurat"],
        "faq": [
            ("How far in advance should we book a wedding pandit?",
             "As early as you can — the muhurat is chosen from both horoscopes and the best dates go quickly. "
             "A few months ahead is comfortable."),
            ("Which wedding traditions do you perform?",
             "North Indian, Garhwali and Gujarati traditions. If your family follows particular regional "
             "customs, tell Acharya Ji beforehand and the ceremony is arranged accordingly."),
            ("Will guests understand the ceremony?",
             "Yes — that is the point. Mantras are in Sanskrit, and each stage is explained in Hindi and English "
             "as it happens, so every generation present follows what is being promised."),
            ("Does the ceremony make our marriage legally registered in the UAE?",
             "No. The religious ceremony and legal registration are separate. Acharya Ji performs the sacrament; "
             "registration and attestation are arranged through the relevant authority or your consulate."),
        ],
    },
    {
        "slug": "havan-puja",
        "name": "Havan",
        "h1": "Havan &amp; Fire Rituals in Dubai, Abu Dhabi &amp; Sharjah",
        "title": "Havan Puja in UAE | Gayatri, Navgraha & Vastu Havan Dubai, Abu Dhabi",
        "desc": ("Book a havan in Dubai, Abu Dhabi or Sharjah — Gayatri, Navgraha, Ayushya and Vastu havan "
                 "performed by Acharya Deepak Thapliyal, arranged safely for UAE apartments. "
                 "Call +971 50 827 3876."),
        "kw": ("havan Dubai, hawan puja UAE, gayatri havan Abu Dhabi, navgraha havan Dubai, vastu havan Sharjah, "
               "ayushya havan, fire ritual pandit UAE, homam Dubai"),
        "lede": "The sacred fire — the oldest form of Vedic offering, and the core of nearly every major ceremony.",
        "duration": "45 minutes to 2 hours",
        "best": "Morning, though evening havans are common",
        "where": "Apartments, villas, offices and halls",
        "body": [
            ("Havan — also called hawan or homa — is the offering of ghee, grains and herbs into a consecrated "
             "fire while mantras are recited. Agni carries the offering; the rite is used for purification, for "
             "settling planetary influences, for health and long life, and as the closing element of larger "
             "ceremonies such as griha pravesh and vivah."),
            ("Several havans are performed regularly for families in the UAE. <strong>Gayatri Havan</strong> "
             "invokes clarity, wisdom and protection, and is the most commonly requested. "
             "<strong>Navgraha Havan</strong> addresses the nine planets and is performed when a horoscope "
             "indicates difficult planetary periods. <strong>Ayushya Havan</strong> is for health and long "
             "life, often on a birthday. <strong>Vastu Havan</strong> settles a home or workplace, and "
             "<strong>Rudra Havan</strong> is performed to Lord Shiva for relief from persistent difficulty."),
            ("The practical question in the Emirates is always the fire itself. Most towers have sensitive "
             "detectors and rules about open flame, and Acharya Ji arranges the havan accordingly — a "
             "correspondingly sized kund, low-smoke samagri, ventilation prepared in advance, and where "
             "necessary a modified arrangement that satisfies building rules. The offerings, the mantras and the "
             "sequence remain complete; what changes is the scale. For larger havans, villas, community halls "
             "and outdoor terraces are often the better setting, and Acharya Ji will say so plainly rather than "
             "squeeze a ceremony into a space that cannot hold it."),
        ],
        "checklist": ["Havan kund or a suitable fireproof vessel", "Mango wood samidha and camphor",
                      "Pure ghee", "Havan samagri mix", "Rice, sesame, barley and jau",
                      "Kalash, coconut, flowers and mango leaves", "Fruit and sweets for prasad"],
        "faq": [
            ("Can a havan be done inside a Dubai or Sharjah apartment?",
             "Yes, in most cases. The kund is sized to the room, low-smoke samagri is used and ventilation is "
             "arranged beforehand. Where a building strictly prohibits open flame, a compliant arrangement is "
             "used and the rite is still completed in full."),
            ("Which havan do we need?",
             "It depends on the purpose — Gayatri for clarity and protection, Navgraha for planetary relief, "
             "Ayushya for health and long life, Vastu for a home or office. Describe the situation and Acharya "
             "Ji will advise."),
            ("How long does a havan take?",
             "From about 45 minutes for a focused havan up to two hours when it forms part of a larger ceremony."),
            ("Do you supply the havan kund and samagri?",
             "Yes, these can be brought along, or a complete list is shared in advance if you would rather "
             "arrange it yourself."),
        ],
    },
    {
        "slug": "kundali-matching",
        "name": "Kundali Matching",
        "h1": "Kundali Matching &amp; Horoscope Analysis in the UAE",
        "title": "Kundali Matching in Dubai & Abu Dhabi | Patrika Milan, Jyotish Consultation UAE",
        "desc": ("Kundali matching and horoscope analysis by a qualified Jyotishacharya in the UAE. Guna milan, "
                 "mangal dosha assessment and janam patrika readings — in person in Abu Dhabi and Dubai, or "
                 "online. Call +971 50 827 3876."),
        "kw": ("kundali matching Dubai, patrika milan UAE, horoscope matching Abu Dhabi, janam patrika analysis, "
               "astrologer in Dubai, jyotish consultation UAE, mangal dosha check, guna milan Sharjah"),
        "lede": "Guna milan, mangal dosha and janam patrika — read by a qualified Jyotishacharya, and explained plainly.",
        "duration": "45 to 90 minutes",
        "best": "In person in Abu Dhabi, or online",
        "where": "Abu Dhabi, Dubai, or by video call",
        "body": [
            ("<strong>Patrika Milan</strong> — kundali matching — compares the birth charts of a prospective "
             "bride and groom before a marriage is agreed. The familiar part is <strong>ashtakoota guna "
             "milan</strong>, which scores eight categories out of a total of 36 points, covering "
             "temperament, mental compatibility, health and progeny among others. Alongside it, "
             "<strong>mangal dosha</strong> (manglik status) is assessed, as are the positions of the moon, "
             "Venus and the seventh house."),
            ("Acharya Deepak Thapliyal is a qualified <strong>Jyotishacharya</strong>, and his approach to "
             "these readings is deliberately plain. A score is not a verdict. A high guna count with a serious "
             "affliction elsewhere in the chart deserves discussion; a moderate score with otherwise sound "
             "placements often does not deserve the alarm families attach to it. He will tell you what the "
             "chart indicates, what it does not indicate, and which remedies are worth the effort rather than "
             "prescribing an expensive list as a matter of course."),
            ("Beyond matching, <strong>Janam Patrika Vishleshan</strong> — full horoscope analysis — covers "
             "career direction, business and job timing, health, property decisions, education and the current "
             "<strong>mahadasha</strong> and <strong>antardasha</strong> periods with practical guidance on "
             "timing. <strong>Kaal Sarp</strong>, <strong>Sade Sati</strong> and <strong>Pitra dosha</strong> "
             "are assessed where relevant, with the appropriate puja or havan recommended only if it is "
             "genuinely called for."),
            ("To prepare a reading, three details are needed for each person: <strong>date of birth, exact time "
             "of birth, and place of birth</strong>. The time matters — even twenty minutes changes the "
             "ascendant and with it much of the chart. Consultations are held in person at Electra Street in "
             "Abu Dhabi, in Dubai by arrangement, or over video call for families spread between the Emirates "
             "and India."),
        ],
        "checklist": ["Date of birth (both people, for matching)", "Exact time of birth",
                      "Place of birth (city and country)", "Existing kundali if you have one",
                      "The specific questions you want addressed"],
        "faq": [
            ("What information do you need for kundali matching?",
             "Date of birth, exact time of birth and place of birth for both the prospective bride and groom. "
             "The birth time matters — a difference of twenty minutes can change the ascendant."),
            ("What is a good guna milan score?",
             "Out of 36 points, 18 and above is generally considered acceptable and higher is better. But a "
             "score alone is not a verdict — mangal dosha and other chart factors are assessed alongside it, "
             "and Acharya Ji will explain what the chart actually indicates."),
            ("Can the consultation be done online?",
             "Yes. Readings are done in person in Abu Dhabi and Dubai, or over video call — which is often "
             "easier when the two families are in different countries."),
            ("Do I have to perform the remedies suggested?",
             "Remedies are recommended only where genuinely warranted, and you are always told why. Nothing is "
             "prescribed as a matter of routine."),
        ],
    },
    {
        "slug": "mata-ki-chowki",
        "name": "Mata Ki Chowki",
        "h1": "Mata Ki Chowki &amp; Bhajan Sandhya in the UAE",
        "title": "Mata Ki Chowki in Dubai, Sharjah & Abu Dhabi | Live Bhajan Sandhya UAE",
        "desc": ("Book Mata Ki Chowki, Bhajan Sandhya or Jagran in Dubai, Sharjah and Abu Dhabi. Sung live with "
                 "harmonium by Acharya Deepak Thapliyal, a trained Sangeet Prabhakar. Call +971 50 827 3876."),
        "kw": ("mata ki chowki Dubai, mata ki chowki Sharjah, bhajan sandhya UAE, jagran Dubai, "
               "devi jagran Abu Dhabi, live bhajan singer UAE, mata ka jagran Sharjah, chowki pandit Dubai"),
        "lede": "An evening of devotion to the Mother Goddess — sung live with harmonium, not played from a recording.",
        "duration": "3 to 5 hours, usually evening",
        "best": "Navratri, or any vow or thanksgiving",
        "where": "Homes, villas and community halls",
        "body": [
            ("Mata Ki Chowki is an evening given over to the Mother Goddess — a gathering of family, neighbours "
             "and friends around the chowki, with bhajans sung through the night. It is held during "
             "<strong>Navratri</strong>, in fulfilment of a vow, in thanksgiving after something has gone well, "
             "or simply as an annual observance a family has kept for years."),
            ("The evening opens with <strong>Ganesh puja</strong> and <strong>chowki sthapana</strong> — the "
             "installation of the Mata's chowki with the sacred kalash, the jyot (lamp) lit to burn through the "
             "evening, and the deity adorned with chunri and flowers. From there it moves into "
             "<strong>bhajans</strong>, <strong>bhents</strong> and <strong>Durga Chalisa</strong>, building "
             "through the night to the <strong>aarti</strong> and the distribution of "
             "<strong>prasad</strong> — traditionally halwa, puri and chana."),
            ("What distinguishes a chowki led by Acharya Deepak Thapliyal is that the music is genuinely live. "
             "He is a <strong>Sangeet Prabhakar</strong> — formally trained in devotional music — and sings "
             "with harmonium himself, drawing the room into the singing rather than performing at it. For "
             "families used to a recorded track playing in the background, the difference is the whole evening."),
            ("The same applies to <strong>Bhajan Sandhya</strong> — a shorter devotional evening for "
             "anniversaries, birthdays and festivals — and to <strong>Jagran</strong>, which runs through the "
             "night. In Sharjah and Dubai these are frequently held in community halls so that neighbours can "
             "join; in villas across Abu Dhabi they are just as often a family affair."),
        ],
        "checklist": ["Chowki, chunri and Mata's picture or murti", "Kalash, coconut and mango leaves",
                      "Akhand jyot: ghee or oil lamp with cotton wicks", "Flowers, garlands and incense",
                      "Fruit, mishri and dry fruit for bhog", "Halwa, puri and chana for prasad",
                      "Seating and a sound point for the harmonium"],
        "faq": [
            ("Is the bhajan singing live or recorded?",
             "Live. Acharya Ji is a trained Sangeet Prabhakar and sings with harmonium himself — nothing is "
             "played from a recording."),
            ("How long does a Mata Ki Chowki last?",
             "Usually three to five hours in the evening. A full jagran runs through the night."),
            ("How many people can attend?",
             "Anything from a family gathering at home to a full community hall. In Sharjah and Dubai, halls "
             "are commonly booked so neighbours can join."),
            ("What prasad is prepared?",
             "Traditionally halwa, puri and chana, along with fruit and mishri offered as bhog during the evening."),
        ],
    },
]


def build(sv):
    slug, name = sv["slug"], sv["name"]
    url = f"{SITE}/{slug}/"
    wa = WA + name.replace(" ", "%20").replace("&amp;", "and") + "%20in%20the%20UAE."

    faq_json = ",\n".join(
        '        {{ "@type": "Question", "name": "{q}", "acceptedAnswer": {{ "@type": "Answer", "text": "{a}" }} }}'
        .format(q=q.replace('"', "'"), a=a.replace('"', "'"))
        for q, a in sv["faq"]
    )
    faq_html = "\n".join(
        f'''      <details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>''' for q, a in sv["faq"]
    )
    body_html = "\n".join(f"      <p>{p}</p>" for p in sv["body"])
    check_html = "".join(f"<li>{c}</li>" for c in sv["checklist"])
    cities_html = "".join(
        f'<li><a href="../{s}/">Pandit in {n}</a></li>' for s, n in CITY_LINKS
    )
    others_html = "".join(
        f'<li><a href="../{o["slug"]}/">{o["name"]}</a></li>' for o in SERVICES if o["slug"] != slug
    )

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{sv["title"]}</title>
<meta name="description" content="{sv["desc"]}">
<meta name="keywords" content="{sv["kw"]}">
<meta name="author" content="Acharya Deepak Thapliyal">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta name="geo.region" content="AE">
<meta name="geo.placename" content="Dubai, Abu Dhabi, Sharjah">
<meta property="og:type" content="website">
<meta property="og:title" content="{sv["title"]}">
<meta property="og:description" content="{sv["desc"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/photo-hero-portrait.jpg">
<meta property="og:locale" content="en_AE">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{sv["title"]}">
<meta name="twitter:description" content="{sv["desc"]}">
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
      "@type": "Service",
      "@id": "{url}#service",
      "name": "{name}",
      "description": "{sv["desc"]}",
      "url": "{url}",
      "serviceType": "{name}",
      "provider": {{
        "@type": "LocalBusiness",
        "@id": "{SITE}/#business",
        "name": "Acharya Deepak Thapliyal — Pandit & Purohit in UAE",
        "telephone": "+919410770925",
        "url": "{SITE}/"
      }},
      "areaServed": [
        {{ "@type": "City", "name": "Dubai" }},
        {{ "@type": "City", "name": "Abu Dhabi" }},
        {{ "@type": "City", "name": "Sharjah" }},
        {{ "@type": "Country", "name": "United Arab Emirates" }}
      ],
      "availableChannel": {{
        "@type": "ServiceChannel",
        "servicePhone": "+971508273876",
        "serviceUrl": "{url}"
      }}
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}/" }},
        {{ "@type": "ListItem", "position": 2, "name": "{name}", "item": "{url}" }}
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
    <strong>{name}</strong> — performed across Dubai, Abu Dhabi &amp; Sharjah.
    <a href="tel:+971508273876">Call +971 50 827 3876</a>
  </p>
</div>

<header class="site-header" id="header">
  <div class="header-inner">
    <a href="../" class="brand">
      <img src="../images/logo-mark.svg" alt="Acharya Deepak Thapliyal monogram" class="brand-mark" width="46" height="46">
      <span class="brand-text">
        <span class="brand-name">Acharya Deepak Thapliyal</span>
        <span class="brand-sub">Pandit &amp; Purohit &middot; UAE</span>
      </span>
    </a>
    <nav class="main-nav" id="main-nav" aria-label="Main navigation">
      <ul>
        <li><a href="../">Home</a></li>
        <li><a href="../#about">About</a></li>
        <li><a href="../#services">Services</a></li>
        <li><a href="../pandit-in-dubai/">Dubai</a></li>
        <li><a href="../pandit-in-abu-dhabi/">Abu Dhabi</a></li>
        <li><a href="../pandit-in-sharjah/">Sharjah</a></li>
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
      <a href="../">Home</a> <span aria-hidden="true">&rsaquo;</span> <span>{name}</span>
    </nav>
    <p class="eyebrow"><span class="om">ॐ</span> Sacred Offerings</p>
    <h1>{sv["h1"]}</h1>
    <p class="hero-lede">{sv["lede"]}</p>
    <div class="hero-ctas">
      <a href="{wa}" class="btn btn-wa" target="_blank" rel="noopener">{WA_SVG} WhatsApp Now</a>
      <a href="tel:+971508273876" class="btn btn-gold">Call +971 50 827 3876</a>
    </div>
    <ul class="quick-facts">
      <li><strong>Duration</strong><span>{sv["duration"]}</span></li>
      <li><strong>Best Time</strong><span>{sv["best"]}</span></li>
      <li><strong>Performed At</strong><span>{sv["where"]}</span></li>
    </ul>
  </div>
</section>

<div class="toran-strip flip" aria-hidden="true"></div>

<section class="about city-intro">
  <div class="section-inner narrow">
    <p class="eyebrow">About the Ceremony</p>
    <h2>What {name} Involves</h2>
{body_html}
  </div>
</section>

<section class="services">
  <div class="section-inner narrow">
    <div class="section-head center">
      <p class="eyebrow">Preparation</p>
      <h2>What to Arrange</h2>
      <p class="section-sub">A complete samagri list is shared on WhatsApp once your date is confirmed — and where it is easier, Acharya Ji brings it along.</p>
    </div>
    <ul class="check-list samagri-list">{check_html}</ul>
  </div>
</section>

<section class="faq">
  <div class="section-inner">
    <div class="section-head center">
      <p class="eyebrow">Common Questions</p>
      <h2>{name} — Your Questions</h2>
    </div>
    <div class="faq-list">
{faq_html}
    </div>
  </div>
</section>

<section class="cities">
  <div class="section-inner">
    <div class="section-head center">
      <p class="eyebrow">Also Available</p>
      <h2>Where &amp; What Else</h2>
    </div>
    <div class="link-cols">
      <div>
        <h3>By City</h3>
        <ul class="link-list">{cities_html}</ul>
      </div>
      <div>
        <h3>Other Ceremonies</h3>
        <ul class="link-list">{others_html}</ul>
      </div>
    </div>
  </div>
</section>

<section class="contact">
  <div class="hero-mandala small" aria-hidden="true"></div>
  <div class="section-inner narrow center-text">
    <p class="eyebrow">Get in Touch</p>
    <h2>Book {name}</h2>
    <p>Tell Acharya Ji your preferred date and area, and he will confirm the muhurat, what is needed and how long it will take.</p>
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
      <h4>Ceremonies</h4>
      <ul>{others_html}</ul>
    </div>
    <div class="footer-col">
      <h4>Cities</h4>
      <ul>{cities_html}<li><a href="../">All UAE services</a></li></ul>
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
    <p>&copy; <span id="year"></span> Acharya Deepak Thapliyal — Hindu Pandit &amp; Purohit, UAE. All rights reserved.</p>
  </div>
</footer>

<a href="{wa}" class="whatsapp-fab" target="_blank" rel="noopener" aria-label="Chat with Acharya Ji on WhatsApp">
  <svg viewBox="0 0 32 32" aria-hidden="true"><path d="M16.04 3C8.86 3 3.02 8.84 3.02 16.02c0 2.29.6 4.53 1.75 6.5L3 29l6.65-1.74a12.95 12.95 0 0 0 6.39 1.67h.01c7.18 0 13.02-5.84 13.02-13.02 0-3.48-1.36-6.75-3.82-9.21A12.92 12.92 0 0 0 16.04 3zm0 23.73h-.01c-1.99 0-3.94-.54-5.64-1.55l-.4-.24-4.2 1.1 1.12-4.1-.26-.42a10.7 10.7 0 0 1-1.65-5.7c0-5.96 4.86-10.82 10.83-10.82 2.89 0 5.61 1.13 7.65 3.18a10.75 10.75 0 0 1 3.17 7.66c0 5.97-4.85 10.89-10.61 10.89zm5.95-8.11c-.33-.16-1.93-.95-2.23-1.06-.3-.11-.52-.16-.73.17-.22.32-.84 1.05-1.03 1.27-.19.22-.38.24-.7.08-.33-.16-1.38-.51-2.62-1.62-.97-.86-1.62-1.93-1.81-2.25-.19-.33-.02-.5.14-.66.15-.15.33-.38.49-.58.16-.19.22-.33.33-.55.11-.22.05-.41-.03-.58-.08-.16-.73-1.76-1-2.41-.26-.63-.53-.55-.73-.56l-.62-.01c-.22 0-.58.08-.88.41-.3.33-1.15 1.13-1.15 2.75s1.18 3.19 1.34 3.41c.16.22 2.32 3.54 5.62 4.96.79.34 1.4.54 1.87.7.79.25 1.5.21 2.07.13.63-.09 1.93-.79 2.2-1.55.27-.76.27-1.42.19-1.55-.08-.14-.3-.22-.63-.38z"/></svg>
</a>

<script src="../script.js"></script>
</body>
</html>
'''


for sv in SERVICES:
    os.makedirs(sv["slug"], exist_ok=True)
    html = build(sv)
    io.open(os.path.join(sv["slug"], "index.html"), "w", encoding="utf-8").write(html)
    print(f'  {sv["slug"]}/index.html  ({len(html)//1024} KB)')
