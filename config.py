"""Réglages du site. Tout ce qui est « None » ou vide est masqué sur le site
tant que l'information n'est pas fournie."""

# Nom de domaine définitif (sans / final). À remplacer une fois acheté.
DOMAIN = "https://www.spaciousvillasxm.com"

SITE_NAME = "Spacious Villa"
SITE_TAGLINE_EN = "Private pool villa in Cul-de-Sac, Saint Martin"
SITE_TAGLINE_FR = "Villa avec piscine privée à Cul-de-Sac, Saint-Martin"

# Contact (laisser vide pour masquer)
EMAIL = ""            # ex. "hello@spaciousvillasxm.com"
WHATSAPP = "33766440125"         # format international sans + ni espaces, ex. "590690000000"
INSTAGRAM = ""        # ex. "https://instagram.com/spaciousvillasxm"

# Tarifs et conditions (None = « sur demande » / masqué)
PRICE_FROM_EUR = 430
MIN_NIGHTS = 3
CHECKIN_TIME = "15:00"
CHECKOUT_TIME = "11:00"
CLEANING_FEE_EUR = 180
DEPOSIT_EUR = 500
CANCELLATION_EN = "Free cancellation up to 30 days before arrival. Between 30 and 15 days before arrival, 50% of the stay is refunded. Less than 15 days before arrival, the stay is non-refundable."
CANCELLATION_FR = "Annulation gratuite jusqu'à 30 jours avant l'arrivée. Entre 30 et 15 jours avant l'arrivée, 50 % du séjour est remboursé. À moins de 15 jours de l'arrivée, le séjour n'est pas remboursable."

# Moteur de réservation Smoobu : coller ici l'URL du widget quand le compte existe.
SMOOBU_WIDGET_URL = ""

# Avis (annonce actuelle)
RATING = "4.97"
REVIEW_COUNT = 66
SUPERHOST = True

# Coordonnées approximatives (centre de Cul-de-Sac, pas l'adresse exacte)
GEO = (18.0960, -63.0450)

# Mentions légales
LEGAL_OWNER = ""            # nom du loueur ou de la société
LEGAL_ADDRESS = ""
LEGAL_SIRET = ""

PETS_ALLOWED = True

# Saisons : (nom EN, nom FR, période EN, période FR, prix/nuit, nuits minimum)
SEASONS = [
    ("Low season", "Basse saison", "May to November", "Mai à novembre", 430, 3),
    ("High season", "Haute saison", "December to April", "Décembre à avril", 590, 5),
    ("Holidays", "Fêtes de fin d'année", "Christmas and New Year", "Noël et Nouvel An", 700, 3),
]

# Période des fêtes (mois-jour) : nuits du 20 décembre au 2 janvier inclus
HOLIDAYS = ("12-20", "01-02")

# Devise : le site anglais affiche les prix en dollars US, le site français en euros.
# Les prix sont saisis en euros ; le dollar est calculé avec ce taux puis arrondi à 5 $.
USD_RATE = 1.12   # taux EUR -> USD (environ 1,12 début novembre 2026)


def usd(eur):
    return int(round(eur * USD_RATE / 5.0) * 5)


def money(lang, eur):
    """Prix formaté : 400 -> « 400 € » en français, « $450 » en anglais."""
    if lang == "en":
        return f"${usd(eur):,}"
    return f"{eur:,} €".replace(",", "\u202f")

# Réduction pour les séjours d'une semaine ou plus (comme sur Airbnb)
WEEKLY_MIN_NIGHTS = 7
WEEKLY_DISCOUNT = 0.10


def whatsapp_display():
    """+33766440125 -> +33 7 66 44 01 25"""
    n = WHATSAPP
    if n.startswith("33") and len(n) == 11:
        r = n[2:]
        return "+33 " + r[0] + " " + " ".join(r[i:i + 2] for i in range(1, 9, 2))
    return "+" + n


def whatsapp_link(text=""):
    from urllib.parse import quote
    return f"https://wa.me/{WHATSAPP}" + (f"?text={quote(text)}" if text else "")
