"""Réglages du site. Tout ce qui est « None » ou vide est masqué sur le site
tant que l'information n'est pas fournie."""

# Nom de domaine définitif (sans / final). À remplacer une fois acheté.
DOMAIN = "https://www.spaciousvillasxm.com"

SITE_NAME = "Spacious Villa"
SITE_TAGLINE_EN = "Private pool villa in Cul-de-Sac, Saint Martin"
SITE_TAGLINE_FR = "Villa avec piscine privée à Cul-de-Sac, Saint-Martin"

# Contact (laisser vide pour masquer)
EMAIL = ""            # ex. "hello@spaciousvillasxm.com"
WHATSAPP = ""         # format international sans + ni espaces, ex. "590690000000"
INSTAGRAM = ""        # ex. "https://instagram.com/spaciousvillasxm"

# Tarifs et conditions (None = « sur demande » / masqué)
PRICE_FROM_EUR = 300
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
    ("Low season", "Basse saison", "May to November", "Mai à novembre", 300, 3),
    ("High season", "Haute saison", "December to April", "Décembre à avril", 400, 5),
    ("Holidays", "Fêtes de fin d'année", "Christmas and New Year", "Noël et Nouvel An", 550, 7),
]

# Période des fêtes (mois-jour) : nuits du 20 décembre au 2 janvier inclus
HOLIDAYS = ("12-20", "01-02")
