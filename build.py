"""Génère le site statique.

  python3 build.py            -> dist/     (version en ligne : URLs propres, photos dans /img)
  python3 build.py preview    -> preview/  (aperçu : liens relatifs, photos de l'ancien site)
"""
import html, json, os, posixpath, shutil, sys, math
import config as C
from content import PHOTOS, PAGES, UI, HOME, GUIDES, faq, page_meta

MODE = "preview" if "preview" in sys.argv[1:] else "prod"
OUT = os.path.join(os.path.dirname(__file__), "preview" if MODE == "preview" else "dist")
LANG_IDX = {"en": 0, "fr": 1}
e = html.escape


def img_src(i):
    name, uuid, *_ = PHOTOS[i]
    local = os.path.join(os.path.dirname(__file__), "static", "img", name)
    if MODE == "preview" and os.path.exists(local):
        return "img/" + name
    if MODE == "preview":
        # Aperçu : photos remplacées par un aplat, l'hébergeur d'aperçu bloquant les images externes
        label = PHOTOS[i][3]
        svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 1067'><rect width='1600' height='1067' fill='#0D7480'/>"
               "<circle cx='1250' cy='260' r='120' fill='#F2C230'/><path d='M0 820 Q400 700 800 800 T1600 760 V1067 H0Z' fill='#15302A' opacity='.35'/>"
               f"<text x='60' y='1010' font-family='sans-serif' font-size='40' fill='#ffffff' opacity='.85'>Photo : {html.escape(label)}</text></svg>")
        from urllib.parse import quote
        return "data:image/svg+xml," + quote(svg)
    # Tant que la photo n'est pas dans static/img, on utilise celle de l'ancienne annonce
    if not os.path.exists(os.path.join(os.path.dirname(__file__), "static", "img", name)):
        return f"https://cozy-stays-curator.lovable.app/__l5e/assets-v1/{uuid}/{name}"
    return f"/img/{name}"


def img_abs(i):
    s = img_src(i)
    return s if s.startswith("http") else C.DOMAIN + s


def clean(path):
    """Chemin public propre : fr/index.html -> /fr/ ; pinel-island.html -> /pinel-island"""
    if path.endswith("index.html"):
        return "/" + path[: -len("index.html")]
    return "/" + path[:-5]


def url(path):
    return C.DOMAIN + clean(path)


def link(frm, to, anchor=""):
    if MODE == "prod":
        return clean(to) + anchor
    rel = posixpath.relpath(to, posixpath.dirname(frm) or ".")
    return rel + anchor


def asset_version(name):
    import hashlib
    p = os.path.join(os.path.dirname(__file__), "static", name)
    if not os.path.exists(p):
        return ""
    return "?v=" + hashlib.md5(open(p, "rb").read()).hexdigest()[:8]


def asset(frm, name):
    if MODE == "prod":
        return "/" + name + asset_version(name)
    return posixpath.relpath(name, posixpath.dirname(frm) or ".")


def head(lang, key, title, desc, path, image_i=0, jsonld=None, noindex=False):
    en_p, fr_p = PAGES[key]
    alt = "\n".join([
        f'<link rel="alternate" hreflang="en" href="{url(en_p)}">',
        f'<link rel="alternate" hreflang="fr" href="{url(fr_p)}">',
        f'<link rel="alternate" hreflang="x-default" href="{url(en_p)}">',
    ])
    ld = ""
    for block in (jsonld or []):
        ld += '<script type="application/ld+json">' + json.dumps(block, ensure_ascii=False) + "</script>\n"
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index, follow, max-image-preview:large">'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{robots}
<link rel="canonical" href="{url(path)}">
{alt}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(C.SITE_NAME)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url(path)}">
<meta property="og:image" content="{img_abs(image_i)}">
<meta property="og:locale" content="{'en_US' if lang == 'en' else 'fr_FR'}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F2C230">
<link rel="icon" href="{asset(path, 'favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="preload" as="image" href="{img_src(image_i)}" fetchpriority="high">
<link rel="stylesheet" href="{asset(path, 'styles.css')}">
{ld}</head>
<body>
"""


def header(lang, key, path):
    u = UI[lang]
    i = LANG_IDX[lang]
    home = PAGES["home"][i]
    other = "fr" if lang == "en" else "en"
    other_path = PAGES[key][LANG_IDX[other]]
    links = "".join(
        f'<a href="{link(path, PAGES[k][i])}"{" aria-current=\"page\"" if k == key else ""}>{e(t)}</a>' for k, t in u["nav"])
    return f"""<a class="skip" href="#main">{u['skip']}</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="{link(path, home)}"><span class="brand-mark" aria-hidden="true"></span>{e(C.SITE_NAME)}</a>
<nav class="nav" aria-label="Main">{links}</nav>
<a class="lang" href="{link(path, other_path)}" hreflang="{other}" lang="{other}" aria-label="{e(u['switch_label'])}">{u['switch']}</a>
<a class="btn header-cta" href="{link(path, PAGES['book'][i])}">{e(u['book'])}</a>
<details class="menu"><summary aria-label="{e(u['menu'])}"><span></span><span></span><span></span></summary>
<nav aria-label="{e(u['menu'])}">{links}<a href="{link(path, PAGES['book'][i])}"{' aria-current="page"' if key == 'book' else ''}>{e(u['book_nav'])}</a></nav></details>
</div></header>
"""


def footer(lang, path):
    u = UI[lang]
    i = LANG_IDX[lang]
    home = PAGES["home"][i]
    guides = "".join(f'<li><a href="{link(path, PAGES[k][i])}">{e(GUIDES[k][lang]["h1"])}</a></li>' for k in GUIDES)
    contact = []
    if C.EMAIL:
        contact.append(f'<li><a href="mailto:{e(C.EMAIL)}">{e(C.EMAIL)}</a></li>')
    if C.WHATSAPP:
        contact.append(f'<li><a href="{e(C.whatsapp_link())}" rel="noopener">WhatsApp : {e(C.whatsapp_display())}</a></li>')
    if C.INSTAGRAM:
        contact.append(f'<li><a href="{e(C.INSTAGRAM)}">Instagram</a></li>')
    contact_html = f"<h2>{u['contact']}</h2><ul>{''.join(contact)}</ul>" if contact else ""
    mobile = ""
    if path not in (PAGES["thanks"][i], PAGES["book"][i]):
        mobile = f"""<div class="mobile-bar"><span><strong>{e(C.SITE_NAME)}</strong>{e(u['mobile_from'])}</span><a class="btn" href="{link(path, PAGES['book'][i])}">{e(u['book_short'])}</a></div>"""
    return f"""<footer class="site-footer"><div class="wrap">
<div class="footer-grid">
<div><h2>{e(C.SITE_NAME)}</h2><p>{e(u['footer_about'])}</p>{contact_html}</div>
<div><h2>{u['footer_guides']}</h2><ul>{guides}</ul></div>
<div><h2>{u['footer_info']}</h2><ul>
<li><a href="{link(path, PAGES['book'][i])}">{e(u['book_nav'])}</a></li>
<li><a href="{link(path, PAGES['faq'][i])}">FAQ</a></li>
<li><a href="{link(path, PAGES['legal'][i])}">{u['legal']}</a></li>
<li><a href="{link(path, PAGES['privacy'][i])}">{u['privacy']}</a></li>
</ul></div>
</div>
<p class="footer-legal">© 2026 {e(C.SITE_NAME)} · Cul-de-Sac, Saint-Martin</p>
</div></footer>
{mobile}
<script src="{asset(path, 'site.js')}" defer></script>{PREVIEW_JS if MODE == "preview" else ""}
</body></html>
"""


def guest_options(lang, selected=2):
    return "".join(f'<option value="{n}"{" selected" if n == selected else ""}>{UI[lang]["guest_n"](n)}</option>' for n in range(1, 9))


def date_fields(lang, prefix="", names=("checkin", "checkout", "guests")):
    u = UI[lang]
    n_in, n_out, n_g = names
    return f"""<div class="field-row">
<div><label for="{prefix}checkin">{u['checkin']}</label><input type="date" id="{prefix}checkin" name="{n_in}" data-role="checkin" required></div>
<div><label for="{prefix}checkout">{u['checkout']}</label><input type="date" id="{prefix}checkout" name="{n_out}" data-role="checkout" required></div>
</div>
<label for="{prefix}guests">{u['guests']}</label><select id="{prefix}guests" name="{n_g}" data-role="guests">{guest_options(lang)}</select>"""


def rates_json(lang="fr"):
    """Tarifs pour l'estimation affichée dans le formulaire."""
    s = {x[0]: x for x in getattr(C, "SEASONS", [])}
    if not s:
        return ""
    conv = C.usd if lang == "en" else (lambda x: x)
    d = {"low": [conv(s["Low season"][4]), s["Low season"][5]],
         "high": [conv(s["High season"][4]), s["High season"][5]],
         "holiday": [conv(s["Holidays"][4]), s["Holidays"][5]],
         "holidayFrom": C.HOLIDAYS[0], "holidayTo": C.HOLIDAYS[1],
         "cleaning": conv(C.CLEANING_FEE_EUR or 0),
         "weekly": [C.WEEKLY_MIN_NIGHTS, C.WEEKLY_DISCOUNT],
         "depositPct": C.DEPOSIT_PCT, "balanceDays": C.BALANCE_DAYS,
         "labels": {"low": s["Low season"][0 if lang == "en" else 1],
                    "high": s["High season"][0 if lang == "en" else 1],
                    "holiday": s["Holidays"][0 if lang == "en" else 1]}}
    return json.dumps(d)


def jsonld_rental(lang):
    h = HOME[lang]
    amen = [a for _, items in HOME["en"]["amenities"] for a in items]
    return {
        "@context": "https://schema.org",
        "@type": "VacationRental",
        "@id": C.DOMAIN + "/#villa",
        "name": C.SITE_NAME + " – " + (C.SITE_TAGLINE_EN if lang == "en" else C.SITE_TAGLINE_FR),
        "description": h["desc"],
        "url": url(PAGES["home"][LANG_IDX[lang]]),
        "image": [img_abs(i) for i in range(len(PHOTOS))],
        "address": {"@type": "PostalAddress", "addressLocality": "Cul-de-Sac", "addressRegion": "Saint-Martin", "postalCode": "97150", "addressCountry": "MF"},
        "geo": {"@type": "GeoCoordinates", "latitude": C.GEO[0], "longitude": C.GEO[1]},
        "containsPlace": {
            "@type": "Accommodation",
            "additionalType": "EntirePlace",
            "numberOfBedrooms": 4,
            "numberOfFullBathrooms": 3,
            "numberOfPartialBathrooms": 1,
            "occupancy": {"@type": "QuantitativeValue", "maxValue": 8},
            "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": a, "value": True} for a in amen],
        },
        "checkinTime": C.CHECKIN_TIME or None,
        "checkoutTime": C.CHECKOUT_TIME or None,
        "petsAllowed": bool(getattr(C, "PETS_ALLOWED", False)),
        "priceRange": (f"From {C.money(lang, C.PRICE_FROM_EUR)}/night" if C.PRICE_FROM_EUR else None),
        "knowsLanguage": ["en", "fr"],
    }


def strip_none(d):
    if isinstance(d, dict):
        return {k: strip_none(v) for k, v in d.items() if v is not None}
    if isinstance(d, list):
        return [strip_none(x) for x in d]
    return d


def whatsapp_block(lang):
    if not C.WHATSAPP:
        return ""
    en = lang == "en"
    q = "A question before booking?" if en else "Une question avant de réserver ?"
    label = "Message us on WhatsApp" if en else "Écrivez-nous sur WhatsApp"
    msg = ("Hello, I have a question about Spacious Villa in Cul-de-Sac." if en
           else "Bonjour, j'ai une question sur Spacious Villa à Cul-de-Sac.")
    return (f'<div class="wa"><p>{q}</p><a class="btn btn-ghost wa-btn" href="{e(C.whatsapp_link(msg))}" rel="noopener">'
            f'<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.1-1.2l-.4-.2z"/></svg>'
            f'{label}</a></div>')


def page_head(lang, path, h1, lede):
    u = UI[lang]
    home = PAGES["home"][LANG_IDX[lang]]
    return f"""<div class="wrap page-head">
<p class="crumbs"><a href="{link(path, home)}">{e(u['home'])}</a> / {e(h1)}</p>
<h1>{e(h1)}</h1><p class="page-lede">{e(lede)}</p>
</div>
"""


def cta(lang, path):
    u = UI[lang]
    book = PAGES["book"][LANG_IDX[lang]]
    wa = ""
    if C.WHATSAPP:
        wa = f'<a class="btn btn-ghost" href="{e(C.whatsapp_link())}" rel="noopener">WhatsApp</a>'
    return f"""<section class="cta"><div class="wrap cta-in">
<div><h2>{e(u['cta_h'])}</h2><p>{e(u['cta_p'])}</p></div>
<div class="cta-btns"><a class="btn" href="{link(path, book)}">{e(u['book'])}</a>{wa}</div>
</div></section>
"""


def sec_intro(lang, path, full):
    i = LANG_IDX[lang]
    h, u = HOME[lang], UI[lang]
    spec = "".join(f"<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>" for a, b in h["spec"])
    if C.MIN_NIGHTS:
        spec += f"<div><dt>{'Minimum stay' if lang == 'en' else 'Séjour minimum'}</dt><dd>{'From' if lang == 'en' else 'Dès'} {C.MIN_NIGHTS} {'nights' if lang == 'en' else 'nuits'}</dd></div>"
    if C.CHECKIN_TIME and C.CHECKOUT_TIME:
        spec += f"<div><dt>{'Check-in / out' if lang == 'en' else 'Arrivée / départ'}</dt><dd>{C.CHECKIN_TIME} / {C.CHECKOUT_TIME}</dd></div>"
    paras = h["intro_body"] if full else h["intro_body"][:1]
    body = "".join(f"<p>{e(p)}</p>" for p in paras)
    if full:
        btn = f'<a class="btn" href="{link(path, PAGES["book"][i])}">{e(u["book"])}</a>'
    else:
        btn = f'<a class="btn btn-ghost" href="{link(path, PAGES["villa"][i])}">{e(u["discover"])}</a>'
    side = f'<dl class="spec">{spec}</dl>'
    if not full and C.RATING:
        side = (f'<div class="intro-score"><p class="score">{C.RATING}<small>{e(h["rev_sub"](C.RATING, C.REVIEW_COUNT))}</small></p>'
                f'<p>{e(h["rev_p"])}</p></div>')
    return f"""<section id="villa"><div class="wrap intro">
<div><h2>{e(h['intro_h'])}</h2><p class="lead">{e(h['intro_lead'])}</p>{body}
<p>{btn}</p></div>
{side}
</div></section>
"""


def sec_mural(lang):
    i = LANG_IDX[lang]
    h = HOME[lang]
    return f"""<section class="mural" aria-labelledby="mural-title">
<img src="{img_src(1)}" alt="{e(PHOTOS[1][3 + i])}" width="{PHOTOS[1][2][0]}" height="{PHOTOS[1][2][1]}" loading="lazy">
<div class="wrap mural-cap"><h2 id="mural-title">{e(h['mural_h'])}</h2><p>{e(h['mural_p'])}</p></div>
</section>
"""


def sec_gallery(lang, path, teaser=False):
    i = LANG_IDX[lang]
    h, u = HOME[lang], UI[lang]
    photos_page = PAGES["photos"][i]
    if teaser:
        tiles = ""
        for n in (0, 2, 3, 4, 5):
            tiles += f'<a href="{link(path, photos_page)}" class="g{n}"><img src="{img_src(n)}" alt="{e(PHOTOS[n][3 + i])}" loading="lazy" width="{PHOTOS[n][2][0]}" height="{PHOTOS[n][2][1]}"></a>'
        return f"""<section id="photos"><div class="wrap">
<div class="section-head"><h2>{e(h['photos_h'])}</h2><a class="more" href="{link(path, photos_page)}">{e(u['see_photos'])} ({len(PHOTOS)})</a></div>
<div class="gallery gallery-teaser">{tiles}</div>
</div></section>
"""
    gal = ""
    for n in range(len(PHOTOS)):
        gal += f'<button type="button" class="g{n}"><img src="{img_src(n)}" alt="{e(PHOTOS[n][3 + i])}" loading="lazy" width="{PHOTOS[n][2][0]}" height="{PHOTOS[n][2][1]}"></button>'
    return f"""<section id="photos" class="tight"><div class="wrap">
<div class="gallery">{gal}</div>
</div></section>
<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Photos">
<button class="lb-btn lb-close" type="button" aria-label="{'Close' if lang == 'en' else 'Fermer'}">×</button>
<button class="lb-btn lb-prev" type="button" aria-label="{'Previous photo' if lang == 'en' else 'Photo précédente'}">‹</button>
<figure style="margin:0"><img src="" alt=""><figcaption></figcaption></figure>
<button class="lb-btn lb-next" type="button" aria-label="{'Next photo' if lang == 'en' else 'Photo suivante'}">›</button>
</div>
"""


def sec_highlights(lang):
    h = HOME[lang]
    hl = "".join(f"<div><h3>{e(t)}</h3><p>{e(d)}</p></div>" for t, d in h["highlights"])
    return f"""<section class="band"><div class="wrap"><h2>{e(h['hl_h'])}</h2><div class="highlights">{hl}</div></div></section>
"""


def sec_amenities(lang):
    h = HOME[lang]
    am = "".join(f"<div><h3>{e(t)}</h3><ul>{''.join(f'<li>{e(x)}</li>' for x in items)}</ul></div>" for t, items in h["amenities"])
    return f"""<section id="amenities" class="tight"><div class="wrap"><h2>{e(h['am_h'])}</h2><div class="amenities">{am}</div></div></section>
"""


def sec_location(lang, with_title=True):
    h = HOME[lang]
    stops = f'<div class="stop" style="left:0"><span class="dot"></span><span class="t">{e(h["route_from"])}</span><span class="n">Cul-de-Sac</span></div>'
    n_stops = len(h["route"])
    for idx, (mins, t, name, how) in enumerate(h["route"], start=1):
        pos = idx / n_stops * 100  # ordered by travel time, evenly spaced
        above = f'<span class="above">{e(how)}</span>' if how else ""
        stops += f'<div class="stop" style="left:{pos:.1f}%">{above}<span class="dot"></span><span class="t">{e(t)}</span><span class="n">{e(name)}</span></div>'
    title = f"<h2>{e(h['loc_h'])}</h2>" if with_title else ""
    return f"""<section id="location" class="location"><div class="wrap">
{title}<p>{e(h['loc_p'])}</p>
<div class="route" role="list">{stops}</div>
</div></section>
"""


def sec_reviews(lang):
    h = HOME[lang]
    if not C.RATING:
        return ""
    return f"""<section id="reviews"><div class="wrap reviews">
<p class="score">{C.RATING}<small>{e(h['rev_sub'](C.RATING, C.REVIEW_COUNT))}</small></p>
<div><h2>{e(h['rev_h'])}</h2><p>{e(h['rev_p'])}</p></div>
</div></section>
"""


def sec_booking(lang, path):
    """Page de réservation : formulaire à gauche, carte récapitulative à droite (détail du prix)."""
    i = LANG_IDX[lang]
    h, u = HOME[lang], UI[lang]
    en = lang == "en"
    steps = "".join(f"<li><strong>{e(s)}</strong><span>{e(d)}</span></li>" for s, d in h["steps"](C.DEPOSIT_PCT, C.BALANCE_DAYS))
    thanks = PAGES["thanks"][i]
    smoobu = ""
    if C.SMOOBU_WIDGET_URL:
        smoobu = f'<iframe class="smoobu-frame" src="{e(C.SMOOBU_WIDGET_URL)}" title="{e(u["book"])}" loading="lazy"></iframe>'
    rating = ""
    if C.RATING:
        r = C.RATING if en else C.RATING.replace(".", ",")
        rating = (f'<p class="co-rating"><span aria-hidden="true">★</span> {r} '
                  f'<span>({C.REVIEW_COUNT} {"reviews on Airbnb" if en else "avis sur Airbnb"})</span></p>')
    t = {
        "stay": "Your stay" if en else "Votre séjour",
        "nights": "Nights" if en else "Nuits",
        "you": "Your details" if en else "Vos coordonnées",
        "sub": "Entire villa · 4 bedrooms · Cul-de-Sac, Saint Martin" if en else "Villa entière · 4 chambres · Cul-de-Sac, Saint-Martin",
        "cancel_h": "Free cancellation" if en else "Annulation gratuite",
        "cancel_p": (f"Full refund up to {C.BALANCE_DAYS} days before arrival." if en
                     else f"Remboursement intégral jusqu'à {C.BALANCE_DAYS} jours avant l'arrivée."),
        "price_h": "Price details" if en else "Détail du prix",
    }
    return f"""<section id="book" class="tight"><div class="wrap">
{smoobu}
<form id="enquiry" class="checkout" name="enquiry" method="POST" action="{link(path, thanks)}" data-netlify="true" netlify-honeypot="bot-field" data-lang="{lang}" data-nights="5" data-rates="{e(rates_json(lang))}">
<input type="hidden" name="form-name" value="enquiry">
<input type="hidden" name="subject" value="Nouvelle demande de réservation">
<p class="hp"><label>Leave empty <input name="bot-field"></label></p>

<div class="co-step co-stay">
<h2>{t['stay']}</h2>
<div class="field-row">
<div><label for="checkin">{u['checkin']}</label><input type="date" id="checkin" name="Arrivée" data-role="checkin" required></div>
<div><label for="checkout">{u['checkout']}</label><input type="date" id="checkout" name="Départ" data-role="checkout" required></div>
</div>
<div class="cal" data-cal aria-label="{'Calendar with nightly prices' if en else 'Calendrier avec le prix par nuit'}"></div>
<div class="co-line"><span class="co-label" id="nights-label">{t['nights']}</span>
<span class="stepper" role="group" aria-labelledby="nights-label"><button type="button" class="sim-minus" aria-label="{e(u['fewer'])}">−</button><output class="sim-n" aria-live="polite">5</output><button type="button" class="sim-plus" aria-label="{e(u['more'])}">+</button></span></div>
<div class="co-line"><label class="co-label" for="guests">{u['guests']}</label>
<select id="guests" name="Voyageurs" data-role="guests">{guest_options(lang)}</select></div>
</div>

<aside class="co-card" aria-label="{t['price_h']}">
<div class="co-head"><img src="{img_src(0)}" alt="" width="{PHOTOS[0][2][0]}" height="{PHOTOS[0][2][1]}">
<div><p class="co-title">{e(C.SITE_NAME)}</p><p class="co-sub">{t['sub']}</p>{rating}</div></div>
<div class="co-block"><p class="co-h">{t['cancel_h']}</p><p>{t['cancel_p']}</p></div>
<div class="co-block"><p class="co-h">{t['price_h']}</p>
<div class="estimate" id="estimate" data-estimate aria-live="polite"></div></div>
</aside>

<div class="co-step co-contact">
<h2>{t['you']}</h2>
<input type="hidden" name="Nuits" value="">
<input type="hidden" name="Estimation" value="">
<input type="hidden" name="Langue du client" value="{'Anglais' if en else 'Français'}">
<label for="name">{e(h['name'])}</label><input id="name" name="Nom" autocomplete="name" required>
<div class="field-row">
<div><label for="email">{e(h['email'])}</label><input id="email" name="E-mail" type="email" autocomplete="email" required></div>
<div><label for="phone">{e(h['phone'])}</label><input id="phone" name="Téléphone" type="tel" autocomplete="tel"></div>
</div>
<label for="message">{e(h['message'])}</label><textarea id="message" name="Message" placeholder="{e(h['message_ph'])}"></textarea>
<label class="check"><input type="checkbox" required> <span>{e(h['consent'])} <a href="{link(path, PAGES['privacy'][i])}">{e(u['privacy'])}</a></span></label>
<button class="btn co-submit" type="submit">{e(h['send'])}</button>
<p class="form-note">{e(h['form_note'])}</p>
{whatsapp_block(lang)}
</div>

<div class="co-step co-how">
<h2>{e(h['steps_h'])}</h2><ol class="steps">{steps}</ol>
</div>
</form>
</div></section>
"""


def sec_faq(lang, qa):
    det = "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in qa)
    return f"""<section id="faq" class="tight"><div class="wrap"><div class="faq faq-page">{det}</div></div></section>
"""


def sec_guides(lang, path):
    i = LANG_IDX[lang]
    h = HOME[lang]
    cards = ""
    for k, g in GUIDES.items():
        gp = PAGES[k][i]
        cards += f'<a class="guide-link" href="{link(path, gp)}"><img src="{img_src(g["img"])}" alt="" loading="lazy" width="800" height="600"><h3>{e(g[lang]["h1"])}</h3><p>{e(g[lang]["card"])}</p></a>'
    return f"""<section id="guides"><div class="wrap">
<div class="section-head"><h2>{e(h['guides_h'])}</h2><p>{e(h['guides_p'])}</p></div>
<div class="guides">{cards}</div>
</div></section>
"""


def build_home(lang):
    i = LANG_IDX[lang]
    path = PAGES["home"][i]
    h, u = HOME[lang], UI[lang]
    book = PAGES["book"][i]
    ld = [
        strip_none(jsonld_rental(lang)),
        {"@context": "https://schema.org", "@type": "WebSite", "name": C.SITE_NAME, "url": url(path), "inLanguage": lang},
    ]
    out = head(lang, "home", h["title"], h["desc"], path, 0, ld)
    out += header(lang, "home", path)
    facts = "".join(f"<li><strong>{n}</strong>{e(t)}</li>" for n, t in h["facts"])
    out += f"""<main id="main">
<section class="hero" aria-labelledby="hero-title">
<img src="{img_src(0)}" alt="{e(PHOTOS[0][3 + i])}" width="{PHOTOS[0][2][0]}" height="{PHOTOS[0][2][1]}" fetchpriority="high">
<div class="wrap hero-inner">
<div>
<h1 id="hero-title">{e(h['h1'])}</h1>
<p class="hero-lede">{e(h['lede'])}</p>
<ul class="facts">{facts}</ul>
</div>
<form class="quick-book" id="quick-book" method="GET" action="{link(path, book)}" data-lang="{lang}" data-rates="{e(rates_json(lang))}">
<h2>{e(h['quick_h'])}</h2>
<p>{e(h['quick_p'])}</p>
{date_fields(lang, 'q-')}
<div class="estimate" data-estimate aria-live="polite"></div>
<button class="btn" type="submit" style="width:100%">{e(u['book'])}</button>
</form>
</div>
</section>
"""
    out += sec_intro(lang, path, full=False)
    out += sec_mural(lang)
    out += sec_gallery(lang, path, teaser=True)
    out += cta(lang, path)
    out += "</main>\n"
    out += footer(lang, path)
    return path, out


def build_page(lang, key):
    """Pages intérieures : villa, photos, emplacement, tarifs et réservation, FAQ."""
    i = LANG_IDX[lang]
    path = PAGES[key][i]
    u = UI[lang]
    title, desc, h1, lede = page_meta(lang, C)[key]
    home = PAGES["home"][i]
    ld = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": u["home"], "item": url(home)},
        {"@type": "ListItem", "position": 2, "name": h1, "item": url(path)}]}]
    img = {"villa": 0, "photos": 0, "location": 3, "book": 1, "faq": 0}[key]
    body = ""
    if key == "villa":
        body = sec_intro(lang, path, full=True).replace('<section id="villa">', '<section id="villa" class="tight">') + sec_highlights(lang) + sec_amenities(lang).replace('class="tight"', '') + sec_reviews(lang) + cta(lang, path)
    elif key == "photos":
        body = sec_gallery(lang, path) + cta(lang, path)
    elif key == "location":
        body = sec_location(lang, with_title=False).replace('class="location"', 'class="location tight-top"') + sec_guides(lang, path) + cta(lang, path)
    elif key == "book":
        body = sec_booking(lang, path)
    elif key == "faq":
        qa = faq(lang, C)
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]})
        body = sec_faq(lang, qa) + cta(lang, path)
    out = head(lang, key, title, desc, path, img, ld)
    out += header(lang, key, path)
    out += f'<main id="main">\n{page_head(lang, path, h1, lede)}{body}</main>\n'
    out += footer(lang, path)
    return path, out


def build_guide(lang, key):
    i = LANG_IDX[lang]
    path = PAGES[key][i]
    g = GUIDES[key]
    t = g[lang]
    home = PAGES["home"][i]
    u = UI[lang]
    body = t["body"].replace("{pinel}", link(path, PAGES["pinel"][i])).replace("{gc}", link(path, PAGES["gc"][i]))
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": t["h1"], "description": t["desc"],
         "image": img_abs(g["img"]), "inLanguage": lang, "datePublished": "2026-10-26", "dateModified": "2026-10-26",
         "author": {"@type": "Organization", "name": C.SITE_NAME, "url": url(home)},
         "publisher": {"@type": "Organization", "name": C.SITE_NAME}, "mainEntityOfPage": url(path)},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": u["home"], "item": url(home)},
            {"@type": "ListItem", "position": 2, "name": t["h1"], "item": url(path)}]},
    ]
    out = head(lang, key, t["title"], t["desc"], path, g["img"], ld)
    out += header(lang, key, path)
    cta_h = "Stay three minutes from Pinel Island" if lang == "en" else "Séjournez à trois minutes de l'îlet Pinel"
    cta_p = ("Our private pool villa in Cul-de-Sac sleeps 8 and puts the whole French side within easy reach."
             if lang == "en" else "Notre villa avec piscine privée à Cul-de-Sac accueille 8 personnes et met tout le côté français à portée de main.")
    out += f"""<main id="main"><div class="wrap">
<div class="article-hero">
<p class="crumbs"><a href="{link(path, home)}">{e(u['home'])}</a> / {e(t['h1'])}</p>
<h1>{e(t['h1'])}</h1>
</div>
<img class="article-cover" src="{img_src(g['img'])}" alt="{e(PHOTOS[g['img']][3 + i])}" width="1600" height="800" fetchpriority="high">
<article class="prose">{body}
<div class="panel" style="margin-top:40px"><h2 style="margin-top:0">{e(cta_h)}</h2><p>{e(cta_p)}</p><a class="btn" href="{link(path, PAGES['book'][i])}">{e(u['book'])}</a></div>
</article>
</div></main>
"""
    out += footer(lang, path)
    return path, out


def contact_line(lang):
    parts = []
    if C.EMAIL:
        parts.append(("Email" if lang == "en" else "E-mail") + " : " + e(C.EMAIL))
    if C.WHATSAPP:
        parts.append("WhatsApp : " + e(C.whatsapp_display()))
    return " · ".join(parts) if parts else todo("", lang)


def todo(v, lang):
    return e(v) if v else ("[to be completed]" if lang == "en" else "[à compléter]")


def build_simple(lang, key):
    i = LANG_IDX[lang]
    path = PAGES[key][i]
    en = lang == "en"
    if key == "legal":
        title = "Legal notice" if en else "Mentions légales"
        body = f"""<h2>{'Publisher' if en else 'Éditeur du site'}</h2>
<p>{todo(C.LEGAL_OWNER, lang)}<br>{todo(C.LEGAL_ADDRESS, lang)}{('<br>SIRET : ' + e(C.LEGAL_SIRET)) if C.LEGAL_SIRET else ''}<br>{contact_line(lang)}</p>
<h2>{'Hosting' if en else 'Hébergement'}</h2>
<p>Netlify, Inc. – San Francisco, {'United States' if en else 'États-Unis'} – netlify.com</p>
<h2>{'Photos and content' if en else 'Photos et contenus'}</h2>
<p>{'All photos and texts on this site belong to the publisher and may not be reused without permission.' if en else "Les photos et textes de ce site appartiennent à l'éditeur et ne peuvent être réutilisés sans autorisation."}</p>"""
    elif key == "privacy":
        title = "Privacy policy" if en else "Politique de confidentialité"
        if en:
            body = f"""<p>When you send a booking request, we collect your name, email, phone number, travel dates, number of guests and your message. We use them only to answer your request and, if you book, to manage your stay.</p>
<h2>Who receives your data</h2><p>Only the villa owners. The form is processed by our host, Netlify, and bookings may be managed in our booking software. We never sell or share your data for advertising.</p>
<h2>How long we keep it</h2><p>Requests that do not lead to a booking are deleted after 12 months. Booking records are kept for as long as required by accounting and tax law.</p>
<h2>Your rights</h2><p>You can ask to access, correct or delete your data at any time by contacting us ({contact_line(lang)}). You can also file a complaint with the French data protection authority (CNIL).</p>
<h2>Cookies</h2><p>This site does not use advertising or tracking cookies.</p>"""
        else:
            body = f"""<p>Lorsque vous envoyez une demande de réservation, nous recueillons votre nom, votre e-mail, votre téléphone, vos dates, le nombre de voyageurs et votre message. Ces données servent uniquement à répondre à votre demande et, si vous réservez, à organiser votre séjour.</p>
<h2>Destinataires</h2><p>Seuls les propriétaires de la villa. Le formulaire est traité par notre hébergeur, Netlify, et les réservations peuvent être gérées dans notre logiciel de réservation. Vos données ne sont jamais vendues ni utilisées à des fins publicitaires.</p>
<h2>Durée de conservation</h2><p>Les demandes sans suite sont supprimées après 12 mois. Les données de réservation sont conservées pendant la durée imposée par les obligations comptables et fiscales.</p>
<h2>Vos droits</h2><p>Vous pouvez à tout moment demander l'accès, la rectification ou la suppression de vos données en nous contactant ({contact_line(lang)}). Vous pouvez aussi adresser une réclamation à la CNIL.</p>
<h2>Cookies</h2><p>Ce site n'utilise aucun cookie publicitaire ni de suivi.</p>"""
    else:  # thanks
        title = "Request sent" if en else "Demande envoyée"
        body = None
    desc = title + " – " + C.SITE_NAME
    out = head(lang, key, title + " | " + C.SITE_NAME, desc, path, 0, None, noindex=(key == "thanks"))
    out += header(lang, key, path)
    if body is None:
        home = PAGES["home"][i]
        msg = ("Thank you. We have your dates and will reply within 24 hours with availability and the direct rate."
               if en else "Merci. Nous avons bien reçu vos dates et vous répondons sous 24 heures avec les disponibilités et le tarif direct.")
        out += f"""<main id="main" class="wrap thanks"><div><h1>{e(title)}</h1><p>{e(msg)}</p><p><a class="btn btn-ghost" href="{link(path, home)}">{e(UI[lang]['home'])}</a></p></div></main>"""
    else:
        out += f"""<main id="main"><div class="wrap"><div class="article-hero"><h1>{e(title)}</h1></div><article class="prose" style="padding-top:0">{body}</article></div></main>"""
    out += footer(lang, path)
    return path, out


PREVIEW_JS = """<script>document.addEventListener('submit',function(e){if(e.target.id!=='enquiry')return;e.preventDefault();var n=e.target.querySelector('.form-note');n.textContent=document.documentElement.lang==='fr'?'Aperçu : le formulaire sera actif une fois le site en ligne.':'Preview: the form goes live once the site is online.';});</script>"""


def favicon():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="15" fill="#F2C230"/><path d="M1.6 21h28.8A15 15 0 0 1 1.6 21z" fill="#0D7480"/></svg>'


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(os.path.join(OUT, "fr"))
    pages = []
    for lang in ("en", "fr"):
        pages.append(build_home(lang))
        for k in ("villa", "photos", "location", "book", "faq"):
            pages.append(build_page(lang, k))
        for k in GUIDES:
            pages.append(build_guide(lang, k))
        for k in ("legal", "privacy", "thanks"):
            pages.append(build_simple(lang, k))
    for path, content in pages:
        if MODE == "preview" and "/" in path:  # aperçu : chemins d'images relatifs depuis /fr/
            content = content.replace('"img/', '"../img/')
        with open(os.path.join(OUT, path), "w", encoding="utf-8") as f:
            f.write(content)
    src = os.path.join(os.path.dirname(__file__), "static")
    for name in os.listdir(src):
        p = os.path.join(src, name)
        if os.path.isdir(p):
            shutil.copytree(p, os.path.join(OUT, name))
        else:
            shutil.copy(p, OUT)
    with open(os.path.join(OUT, "favicon.svg"), "w") as f:
        f.write(favicon())
    if MODE == "prod":
        # sitemap with hreflang pairs
        rows = []
        for key, (en_p, fr_p) in PAGES.items():
            if key == "thanks":
                continue
            for p in (en_p, fr_p):
                rows.append(f"""<url><loc>{url(p)}</loc><lastmod>2026-10-26</lastmod>
<xhtml:link rel="alternate" hreflang="en" href="{url(en_p)}"/><xhtml:link rel="alternate" hreflang="fr" href="{url(fr_p)}"/><xhtml:link rel="alternate" hreflang="x-default" href="{url(en_p)}"/></url>""")
        with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n")
        with open(os.path.join(OUT, "robots.txt"), "w") as f:
            f.write(f"User-agent: *\nAllow: /\nDisallow: /thanks\nDisallow: /fr/merci\n\nSitemap: {C.DOMAIN}/sitemap.xml\n")
        pass
    print(f"{len(pages)} pages -> {OUT}")


if __name__ == "__main__":
    main()
