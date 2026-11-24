"""Textes du site, en anglais et en français."""

PHOTOS = [
    ("villa-pool-gazebo.jpg", "", (1452, 966),
     "Private pool, gazebo and yellow villa beneath the Saint Martin hills",
     "Piscine privée, gazebo et villa jaune au pied des collines de Saint-Martin"),
    ("spacious-villa-mural.jpg", "", (1600, 899),
     "The Spacious Villa mural, a sea turtle and coral reef, painted by the pool",
     "La fresque Spacious Villa, tortue et récif corallien, peinte au bord de la piscine"),
    ("living-room-sea-view.jpg", "", (1164, 890),
     "Living room with vaulted ceiling and sea view",
     "Salon sous plafond cathédrale avec vue mer"),
    ("covered-terrace-sea-view.jpg", "", (1314, 878),
     "Covered dining terrace overlooking the pool and the sea",
     "Terrasse couverte avec table, vue sur la piscine et la mer"),
    ("private-pool.jpg", "", (1322, 860),
     "Private pool with sun loungers",
     "Piscine privée et transats"),
    ("bedroom-balcony.jpg", "", (1146, 860),
     "Bedroom with four-poster bed and balcony",
     "Chambre avec lit à baldaquin et balcon"),
    ("outdoor-lounge-sea-view.jpg", "", (1164, 860),
     "Outdoor lounge under the gazebo with a view of the sea",
     "Salon extérieur sous le gazebo avec vue mer"),
    ("dining-room.jpg", "", (1314, 878),
     "Dining room for eight opening onto the pool",
     "Salle à manger pour huit ouverte sur la piscine"),
    ("tv-lounge.jpg", "", (1322, 860),
     "TV lounge with 75-inch screen and Netflix",
     "Salon TV avec écran 75 pouces et Netflix"),
    ("poolside-lounge.jpg", "", (1164, 758),
     "Lounge area beside the pool",
     "Coin salon au bord de la piscine"),
    ("villa-garden-exterior.jpg", "", (1308, 890),
     "The villa, its garden and covered veranda",
     "La villa, son jardin et sa véranda couverte"),
]

# Pages: key -> (EN path, FR path)
PAGES = {
    "home":    ("index.html", "fr/index.html"),
    "villa":   ("the-villa.html", "fr/la-villa.html"),
    "photos":  ("photos.html", "fr/photos.html"),
    "location": ("location.html", "fr/emplacement.html"),
    "book":    ("rates-booking.html", "fr/tarifs-reservation.html"),
    "faq":     ("faq.html", "fr/faq.html"),
    "pinel":   ("pinel-island.html", "fr/ilet-pinel.html"),
    "gc":      ("grand-case-restaurants.html", "fr/restaurants-grand-case.html"),
    "beaches": ("saint-martin-beaches.html", "fr/plages-saint-martin.html"),
    "season":  ("best-time-to-visit-saint-martin.html", "fr/quand-partir-saint-martin.html"),
    "airport": ("sxm-airport-to-cul-de-sac.html", "fr/aeroport-sxm-cul-de-sac.html"),
    "legal":   ("legal-notice.html", "fr/mentions-legales.html"),
    "privacy": ("privacy.html", "fr/confidentialite.html"),
    "thanks":  ("thanks.html", "fr/merci.html"),
}

UI = {
    "en": {
        "nav": [("villa", "The villa"), ("photos", "Photos"), ("location", "Location"), ("faq", "FAQ")],
        "book_nav": "Rates and booking",
        "menu": "Menu", "see_photos": "See all photos", "discover": "Discover the villa", "rates_h": "Rates",
        "sim_q": "How many nights?", "sim_night": "Per night", "sim_total": lambda n: f"Total for {n} nights",
        "sim_note": lambda pct, k: f"Totals include the cleaning fee. {pct}% off from {k} nights.",
        "sim_min": lambda k: f"{k} nights min.", "fewer": "One night fewer", "more": "One night more",
        "cta_h": "Ready to plan your stay?", "cta_p": "Check the price for your dates and send your request. We reply within 24 hours.",
        "nav_guides": "Island guides",
        "book": "Check availability", "book_short": "Check dates",
        "switch": "Français", "switch_label": "Version française",
        "skip": "Skip to content",
        "guests": "Guests", "checkin": "Check-in", "checkout": "Check-out",
        "guest_n": lambda n: f"{n} guest" + ("s" if n > 1 else ""),
        "footer_about": "A private 4-bedroom pool villa in Cul-de-Sac, on the French side of Saint Martin. Book directly with the owners.",
        "footer_villa": "The villa", "footer_guides": "Guides", "footer_info": "Information",
        "legal": "Legal notice", "privacy": "Privacy",
        "home": "Home", "mobile_from": "Private pool villa · 8 guests",
        "contact": "Contact",
    },
    "fr": {
        "nav": [("villa", "La villa"), ("photos", "Photos"), ("location", "Emplacement"), ("faq", "FAQ")],
        "book_nav": "Tarifs et réservation",
        "menu": "Menu", "see_photos": "Voir toutes les photos", "discover": "Découvrir la villa", "rates_h": "Tarifs",
        "sim_q": "Combien de nuits ?", "sim_night": "Par nuit", "sim_total": lambda n: f"Total pour {n} nuits",
        "sim_note": lambda pct, k: f"Les totaux incluent le ménage. −{pct} % dès {k} nuits.",
        "sim_min": lambda k: f"{k} nuits min.", "fewer": "Une nuit de moins", "more": "Une nuit de plus",
        "cta_h": "Prêt à préparer votre séjour ?", "cta_p": "Calculez le prix pour vos dates et envoyez votre demande. Réponse sous 24 heures.",
        "nav_guides": "Guides de l'île",
        "book": "Voir les disponibilités", "book_short": "Mes dates",
        "switch": "English", "switch_label": "English version",
        "skip": "Aller au contenu",
        "guests": "Voyageurs", "checkin": "Arrivée", "checkout": "Départ",
        "guest_n": lambda n: f"{n} voyageur" + ("s" if n > 1 else ""),
        "footer_about": "Villa privée de 4 chambres avec piscine à Cul-de-Sac, côté français de Saint-Martin. Réservation en direct avec les propriétaires.",
        "footer_villa": "La villa", "footer_guides": "Guides", "footer_info": "Informations",
        "legal": "Mentions légales", "privacy": "Confidentialité",
        "home": "Accueil", "mobile_from": "Villa avec piscine · 8 voyageurs",
        "contact": "Contact",
    },
}

HOME = {
    "en": {
        "title": "Private Pool Villa in Cul-de-Sac, Saint Martin | Sleeps 8 | Book Direct",
        "desc": "4-bedroom villa with private pool and sea views in Cul-de-Sac, French Saint Martin. Sleeps 8, minutes from Pinel Island, Orient Beach and Grand Case. Book direct, no platform fees.",
        "h1": "A private pool villa in Cul-de-Sac",
        "lede": "Four bedrooms, sea views and a fenced garden on the French side of Saint Martin, three minutes from the boat to Pinel Island.",
        "facts": [("8", "guests"), ("4", "bedrooms"), ("3.5", "bathrooms"), ("1", "private pool")],
        "quick_h": "Plan your stay",
        "quick_p": "Send your dates and we reply with availability and the direct rate.",
        "intro_h": "The whole villa, just for you",
        "intro_lead": "A bright, open-plan villa built for easy island living, with room for two families or a group of friends.",
        "intro_body": [
            "Four sunlit bedrooms give everyone their own space. Outside, the private pool, the fenced garden and the shaded gazebo make slow days at home as inviting as days out exploring.",
            "The entire property is yours for the stay: pool, barbecue area, laundry room and private parking. A fully equipped kitchen, a dedicated workspace and fast Wi-Fi make it just as easy to stay for two weeks as for a long weekend.",
        ],
        "spec": [("Property", "Entire villa"), ("Bedrooms", "4"), ("Bathrooms", "3.5"), ("Sleeps", "8 guests"),
                 ("Pool", "Private, outdoor"), ("Parking", "Private, on site"), ("Arrival", "Self check-in"), ("Pets", "Welcome"), ("Housekeeping", "Weekly")],
        "mural_h": "Welcome to Spacious Villa",
        "mural_p": "Our new mural brings the Caribbean reef to the poolside: a sea turtle, coral and tropical fish, painted for our guests.",
        "photos_h": "Inside and out",
        "photos_p": "Tap a photo to see it full screen.",
        "hl_h": "Why guests choose this villa",
        "highlights": [
            ("Your own pool", "A private outdoor pool and sun terrace, never shared with other guests."),
            ("Sea and garden views", "Watch the light change over the water from the gazebo or the outdoor lounge."),
            ("Space for eight", "Four bedrooms, open living areas and a fully fenced garden, good for families with children."),
            ("Made for longer stays", "Full kitchen, washer and dryer, a real workspace and high-speed Wi-Fi."),
        ],
        "am_h": "Amenities",
        "amenities": [
            ("Essentials", ["High-speed Wi-Fi", "Air conditioning", "Towels and bed linen", "Hot water", "Weekly housekeeping", "Dedicated workspace", "Self check-in", "Pets welcome"]),
            ("Kitchen and dining", ["Fully equipped kitchen", "Fridge and freezer", "Oven and gas cooker", "Dishwasher", "Coffee maker", "Outdoor dining area"]),
            ("Outdoor", ["Private pool", "Patio and terrace", "Fenced private garden", "BBQ grill", "Outdoor furniture", "Beach essentials"]),
            ("Comfort", ["75-inch HDTV", "Fire TV, Hulu and Netflix", "Washer and dryer", "Room-darkening blinds", "Ceiling and portable fans", "Books"]),
        ],
        "loc_h": "Close to everything, quiet at home",
        "loc_p": "Cul-de-Sac is a calm bay on the north-east of the French side, facing Pinel Island. Beaches, restaurants and the island's best day trips are a few minutes away. The exact address is shared after booking.",
        "route_from": "Villa",
        "route": [(2, "2 min", "Restaurants", "on foot"), (3, "3 min", "Pinel Island boat", ""), (5, "5 min", "Orient Beach", "by car"),
                  (5, "5 min", "Grand Case", "by car"), (30, "30 min", "SXM Airport", "by car")],
        "rev_h": "Loved by guests",
        "rev_sub": lambda r, n: f"out of 5, from {n} verified reviews on Airbnb",
        "rev_p": "Guests consistently rate the villa near perfect for cleanliness, location and communication, and the hosts are Airbnb Superhosts.",
        "book_h": "Book direct",
        "book_p": "Booking with us directly means a simpler stay and a better deal.",
        "direct": ["No platform service fees", "Talk directly to the owners, before and during your stay", "Flexible on special requests, early arrivals and long stays", "Secure card payment"],
        "steps_h": "How booking works",
        "steps": lambda pct, days: [
            ("Send your dates", "We confirm availability within 24 hours."),
            (f"Pay a {pct}% deposit", "You receive a secure payment link and pay by card. Your dates are then confirmed."),
            (f"Pay the balance {days} days before arrival", f"For a stay starting in less than {days} days, the full amount is due at booking."),
            ("Receive your arrival details", "Address, directions and self check-in instructions, a few days before you land."),
        ],
        "price_on_req": "Rate on request",
        "price_from": lambda p: f"From <strong>{p}</strong> per night",
        "form_h": "Request your dates",
        "name": "Full name", "email": "Email", "phone": "Phone or WhatsApp", "message": "Anything we should know?",
        "message_ph": "Arrival time, children's ages, airport pick-up, car rental…",
        "consent": "I agree that my details are used to answer my request.",
        "send": "Send my request",
        "form_note": "We reply within 24 hours. Nothing is charged at this stage.",
        "faq_h": "Good to know",
        "guides_h": "Make the most of Saint Martin",
        "guides_p": "Our local guides to the island around the villa.",
    },
    "fr": {
        "title": "Villa avec piscine privée à Cul-de-Sac, Saint-Martin | 8 personnes | Réservation directe",
        "desc": "Villa 4 chambres avec piscine privée et vue mer à Cul-de-Sac, Saint-Martin côté français. 8 voyageurs, à quelques minutes de l'îlet Pinel, de la Baie Orientale et de Grand Case. Réservez en direct, sans frais de plateforme.",
        "h1": "Une villa avec piscine privée à Cul-de-Sac",
        "lede": "Quatre chambres, vue mer et jardin clos côté français de Saint-Martin, à trois minutes du bateau pour l'îlet Pinel.",
        "facts": [("8", "voyageurs"), ("4", "chambres"), ("3,5", "salles de bain"), ("1", "piscine privée")],
        "quick_h": "Préparez votre séjour",
        "quick_p": "Envoyez vos dates, nous vous répondons avec les disponibilités et le tarif direct.",
        "intro_h": "Toute la villa, rien que pour vous",
        "intro_lead": "Une villa lumineuse et ouverte, pensée pour la vie sur l'île, avec de la place pour deux familles ou un groupe d'amis.",
        "intro_body": [
            "Quatre chambres baignées de lumière offrent à chacun son espace. Dehors, la piscine privée, le jardin clos et le gazebo ombragé rendent les journées à la maison aussi agréables que les sorties.",
            "Toute la propriété est à vous pendant le séjour : piscine, coin barbecue, buanderie et parking privé. Cuisine entièrement équipée, vrai bureau et Wi-Fi rapide : on y reste aussi bien deux semaines qu'un long week-end.",
        ],
        "spec": [("Logement", "Villa entière"), ("Chambres", "4"), ("Salles de bain", "3,5"), ("Capacité", "8 voyageurs"),
                 ("Piscine", "Privée, extérieure"), ("Parking", "Privé, sur place"), ("Arrivée", "Autonome"), ("Animaux", "Acceptés"), ("Ménage", "Hebdomadaire")],
        "mural_h": "Bienvenue à Spacious Villa",
        "mural_p": "Notre nouvelle fresque fait entrer le récif des Caraïbes au bord de la piscine : une tortue de mer, des coraux et des poissons tropicaux, peints pour nos voyageurs.",
        "photos_h": "Dedans comme dehors",
        "photos_p": "Touchez une photo pour l'agrandir.",
        "hl_h": "Pourquoi nos voyageurs choisissent cette villa",
        "highlights": [
            ("Votre propre piscine", "Une piscine extérieure privée et sa terrasse, jamais partagées avec d'autres voyageurs."),
            ("Vue mer et jardin", "Regardez la lumière changer sur l'eau depuis le gazebo ou le salon extérieur."),
            ("De la place pour huit", "Quatre chambres, de grands espaces de vie et un jardin entièrement clos, idéal avec des enfants."),
            ("Pensée pour les longs séjours", "Cuisine complète, lave-linge et sèche-linge, vrai bureau et Wi-Fi haut débit."),
        ],
        "am_h": "Équipements",
        "amenities": [
            ("L'essentiel", ["Wi-Fi haut débit", "Climatisation", "Serviettes et linge de lit", "Eau chaude", "Ménage hebdomadaire", "Espace de travail", "Arrivée autonome", "Animaux acceptés"]),
            ("Cuisine et repas", ["Cuisine entièrement équipée", "Réfrigérateur et congélateur", "Four et gazinière", "Lave-vaisselle", "Cafetière", "Table extérieure"]),
            ("Extérieur", ["Piscine privée", "Patio et terrasse", "Jardin privé clos", "Barbecue", "Mobilier de jardin", "Équipement de plage"]),
            ("Confort", ["Télévision HD 75 pouces", "Fire TV, Hulu et Netflix", "Lave-linge et sèche-linge", "Rideaux occultants", "Ventilateurs plafond et sur pied", "Livres"]),
        ],
        "loc_h": "Proche de tout, au calme chez vous",
        "loc_p": "Cul-de-Sac est une baie paisible au nord-est de la partie française, face à l'îlet Pinel. Plages, restaurants et plus belles excursions de l'île sont à quelques minutes. L'adresse exacte est communiquée après la réservation.",
        "route_from": "Villa",
        "route": [(2, "2 min", "Restaurants", "à pied"), (3, "3 min", "Bateau pour l'îlet Pinel", ""), (5, "5 min", "Baie Orientale", "en voiture"),
                  (5, "5 min", "Grand Case", "en voiture"), (30, "30 min", "Aéroport SXM", "en voiture")],
        "rev_h": "Plébiscitée par nos voyageurs",
        "rev_sub": lambda r, n: f"sur 5, d'après {n} avis vérifiés sur Airbnb",
        "rev_p": "Les voyageurs notent la villa presque parfaite pour la propreté, l'emplacement et la communication, et les hôtes ont le statut Superhost sur Airbnb.",
        "book_h": "Réservez en direct",
        "book_p": "Réserver directement avec nous, c'est un séjour plus simple et un meilleur prix.",
        "direct": ["Aucuns frais de service de plateforme", "Un contact direct avec les propriétaires, avant et pendant le séjour", "De la souplesse pour les demandes spéciales, arrivées anticipées et longs séjours", "Paiement sécurisé par carte"],
        "steps_h": "Comment se passe la réservation",
        "steps": lambda pct, days: [
            ("Envoyez vos dates", "Nous confirmons la disponibilité sous 24 heures."),
            (f"Réglez un acompte de {pct} %", "Vous recevez un lien de paiement sécurisé et payez par carte. Vos dates sont alors confirmées."),
            (f"Réglez le solde {days} jours avant l'arrivée", f"Pour un séjour qui commence dans moins de {days} jours, la totalité est due à la réservation."),
            ("Recevez vos informations d'arrivée", "Adresse, itinéraire et instructions d'arrivée autonome, quelques jours avant votre départ."),
        ],
        "price_on_req": "Tarif sur demande",
        "price_from": lambda p: f"À partir de <strong>{p}</strong> la nuit",
        "form_h": "Demandez vos dates",
        "name": "Nom complet", "email": "E-mail", "phone": "Téléphone ou WhatsApp", "message": "Quelque chose à nous dire ?",
        "message_ph": "Heure d'arrivée, âge des enfants, navette aéroport, location de voiture…",
        "consent": "J'accepte que mes coordonnées soient utilisées pour répondre à ma demande.",
        "send": "Envoyer ma demande",
        "form_note": "Réponse sous 24 heures. Rien n'est débité à ce stade.",
        "faq_h": "Bon à savoir",
        "guides_h": "Profitez de Saint-Martin",
        "guides_p": "Nos guides de l'île autour de la villa.",
    },
}


def faq(lang, cfg):
    """Questions fréquentes ; les réponses inconnues ne sont pas affichées."""
    en = lang == "en"
    out = []
    if cfg.CHECKIN_TIME and cfg.CHECKOUT_TIME:
        out.append(("What time are check-in and check-out?" if en else "À quelle heure sont l'arrivée et le départ ?",
                    (f"Check-in is from {cfg.CHECKIN_TIME} and check-out is by {cfg.CHECKOUT_TIME}. Arrival is self check-in. We can often adjust these times, just ask."
                     if en else f"L'arrivée se fait à partir de {cfg.CHECKIN_TIME} et le départ avant {cfg.CHECKOUT_TIME}. L'arrivée est autonome, et nous pouvons souvent adapter ces horaires : demandez-nous.")))
    else:
        out.append(("How does arrival work?" if en else "Comment se passe l'arrivée ?",
                    "Arrival is self check-in. We send you the directions and access details before your stay." if en
                    else "L'arrivée est autonome. Nous vous envoyons l'itinéraire et les informations d'accès avant votre séjour."))
    out += [
        ("Can you pick us up at the airport?" if en else "Pouvez-vous venir nous chercher à l'aéroport ?",
         "Yes. We can pick you up at SXM airport and drive you to the villa, and take you back at the end of your stay. Ask us on WhatsApp when you contact us." if en
         else "Oui. Nous pouvons venir vous chercher à l'aéroport SXM et vous conduire à la villa, puis vous y ramener en fin de séjour. Demandez-le-nous sur WhatsApp quand vous nous contactez."),
        ("Can we rent a car?" if en else "Peut-on louer une voiture ?",
         "Yes. We rent our own cars to guests at a friendly daily rate. Ask us on WhatsApp when you contact us. Rental companies are also available at the airport." if en
         else "Oui. Nous louons nos propres voitures à nos voyageurs, à un tarif journalier sympathique. Demandez-le-nous sur WhatsApp quand vous nous contactez. Des loueurs sont aussi présents à l'aéroport."),
        ("Is the pool private?" if en else "La piscine est-elle privée ?",
         "Yes. The pool, the garden and the whole villa are for your group only." if en
         else "Oui. La piscine, le jardin et toute la villa sont réservés à votre groupe."),
        ("Is there parking?" if en else "Y a-t-il un parking ?",
         "Yes, private parking is available on site. We recommend renting a car to explore the island." if en
         else "Oui, un parking privé est disponible sur place. Nous conseillons de louer une voiture pour découvrir l'île."),
        ("How far is the villa from the airport?" if en else "À quelle distance se trouve l'aéroport ?",
         "Princess Juliana International Airport (SXM), on the Dutch side, is about 30 minutes by car." if en
         else "L'aéroport international Princess Juliana (SXM), côté hollandais, est à environ 30 minutes en voiture."),
        ("Is there Wi-Fi? Can I work from the villa?" if en else "Y a-t-il du Wi-Fi ? Peut-on télétravailler ?",
         "Yes. The villa has high-speed Wi-Fi and a dedicated workspace." if en
         else "Oui. La villa dispose du Wi-Fi haut débit et d'un vrai espace de travail."),
        ("Is the villa suitable for children?" if en else "La villa convient-elle aux enfants ?",
         "Yes. The garden is fully fenced and there is plenty of space for families. Please keep an eye on young children around the pool." if en
         else "Oui. Le jardin est entièrement clos et il y a beaucoup d'espace pour les familles. Merci de surveiller les jeunes enfants près de la piscine."),
    ]
    if cfg.MIN_NIGHTS:
        out.append(("Is there a minimum stay?" if en else "Y a-t-il une durée minimum de séjour ?",
                    "Yes: 3 nights in low season and over Christmas and New Year, 5 nights in high season." if en else "Oui : 3 nuits en basse saison et pendant les fêtes, 5 nuits en haute saison."))
    if getattr(cfg, "SEASONS", None):
        lo, hi, ho = (cfg.money(lang, x[4]) for x in cfg.SEASONS)
        clean = cfg.money(lang, cfg.CLEANING_FEE_EUR) if cfg.CLEANING_FEE_EUR else None
        out.append(("How much does the villa cost per night?" if en else "Quel est le prix de la villa par nuit ?",
                    ((f"The price depends on your dates: {lo} per night from May to November, {hi} from December to April, and {ho} over Christmas and New Year. "
                      f"The booking calendar shows the price of each night and the total for your stay."
                      + (f" A cleaning fee of {clean} applies once per stay." if clean else "")) if en else
                     (f"Le prix dépend de vos dates : {lo} la nuit de mai à novembre, {hi} de décembre à avril, et {ho} pour Noël et le Nouvel An. "
                      f"Le calendrier de réservation affiche le prix de chaque nuit et le total de votre séjour."
                      + (f" Des frais de ménage de {clean} s'ajoutent une fois par séjour." if clean else "")))))
    if getattr(cfg, "WEEKLY_DISCOUNT", 0):
        pct = int(cfg.WEEKLY_DISCOUNT * 100)
        out.append(("Is there a discount for longer stays?" if en else "Y a-t-il une réduction pour les longs séjours ?",
                    f"Yes, {pct}% off the nightly rate for stays of {cfg.WEEKLY_MIN_NIGHTS} nights or more. The price calculator applies it automatically." if en
                    else f"Oui, {pct} % de réduction sur les nuits dès {cfg.WEEKLY_MIN_NIGHTS} nuits. Le calculateur de prix l'applique automatiquement."))
    if getattr(cfg, "DEPOSIT_PCT", 0):
        p, d = cfg.DEPOSIT_PCT, cfg.BALANCE_DAYS
        out.append(("How do I pay?" if en else "Comment se passe le paiement ?",
                    (f"A {p}% deposit confirms your booking, paid by card through a secure payment link. The balance is due {d} days before arrival. If your stay starts in less than {d} days, the full amount is due at booking." if en
                     else f"Un acompte de {p} % confirme votre réservation, réglé par carte via un lien de paiement sécurisé. Le solde est dû {d} jours avant l'arrivée. Si votre séjour commence dans moins de {d} jours, la totalité est due à la réservation.")))
    if cfg.DEPOSIT_EUR:
        out.append(("Is there a security deposit?" if en else "Y a-t-il une caution ?",
                    f"Yes, {cfg.money('en', cfg.DEPOSIT_EUR)}. It is a hold on your card, not a charge, and it is released after your stay if nothing is damaged." if en
                    else f"Oui, {cfg.money('fr', cfg.DEPOSIT_EUR)}. C'est une empreinte bancaire, pas un débit : elle est levée après le séjour si rien n'est endommagé."))
    out.append(("Is there a cleaning fee?" if en else "Y a-t-il des frais de ménage ?",
                "No. Final cleaning is included in the nightly rate, and weekly housekeeping is included during your stay." if en
                else "Non. Le ménage de fin de séjour est inclus dans le prix de la nuit, et un ménage hebdomadaire est assuré pendant le séjour."))
    if getattr(cfg, "PETS_ALLOWED", False):
        out.append(("Are pets allowed?" if en else "Les animaux sont-ils acceptés ?",
                    "Yes, pets are welcome. Please tell us about your pet when you send your request." if en
                    else "Oui, les animaux sont les bienvenus. Merci de nous le préciser dans votre demande."))
    out.append(("What are the house rules?" if en else "Quel est le règlement de la villa ?",
                "Up to 8 guests. No parties or events without our prior agreement. No smoking indoors. Please respect the neighbours and the calm of the area, and follow the pool safety instructions." if en
                else "8 personnes maximum. Pas de fêtes ni d'événements sans notre accord préalable. Non-fumeur à l'intérieur. Merci de respecter le voisinage et la tranquillité des lieux, ainsi que les consignes de sécurité de la piscine."))
    canc = cfg.CANCELLATION_EN if en else cfg.CANCELLATION_FR
    if canc:
        out.append(("What is the cancellation policy?" if en else "Quelle est la politique d'annulation ?", canc))
    return out


GUIDES = {
    "pinel": {
        "img": 3,
        "en": {
            "title": "Pinel Island from Cul-de-Sac: Ferry, Beaches and Snorkeling Guide",
            "desc": "How to spend a day on Pinel Island, Saint Martin: the ferry from Cul-de-Sac, the best beach spots, the snorkeling trail and tips from a villa three minutes from the boat.",
            "h1": "A day on Pinel Island",
            "card": "The small boat leaves from Cul-de-Sac, a few minutes from the villa.",
            "body": """
<p>Pinel Island (Îlet Pinel) is the small, uninhabited island facing Cul-de-Sac bay. Calm turquoise water, white sand and a couple of beach restaurants make it one of the easiest and most loved day trips in Saint Martin, and from the villa you are only three minutes from the boat.</p>
<h2>Getting there</h2>
<p>Small ferries leave from the jetty in Cul-de-Sac throughout the day and the crossing takes only a few minutes. Boats run on demand during daytime and there is no accommodation on the island, so check the time of the last boat back when you buy your ticket. Bring cash in case card payment is not available.</p>
<p>If you prefer to paddle, the bay is sheltered enough for kayaks and paddleboards, which can be rented from Cul-de-Sac.</p>
<h2>What to do on the island</h2>
<ul>
<li><strong>Swim in the lagoon.</strong> The main beach faces the bay and the water is shallow and calm, which is ideal for children.</li>
<li><strong>Snorkel.</strong> Pinel is part of the Saint Martin nature reserve. Along the shore you can see fish, sea urchins and sometimes turtles. Bring your own mask or rent one on the beach.</li>
<li><strong>Walk to the viewpoint.</strong> A short path climbs the hill for views over Orient Bay and Tintamarre. Wear proper shoes, not flip-flops.</li>
<li><strong>Lunch with your feet in the sand.</strong> The beach restaurants serve grilled fish, lobster and salads and rent sunbeds and umbrellas.</li>
<li><strong>Look out for iguanas.</strong> They live all over the island and are used to visitors. Please do not feed them.</li>
</ul>
<div class="callout"><p><strong>Our tip:</strong> take the first boats in the morning. The beach is at its quietest, the light is beautiful and you are back at the villa pool for a late lunch.</p></div>
<h2>Good to know</h2>
<ul>
<li>Bring water, sunscreen that is safe for reefs, and a hat. There is little natural shade away from the restaurants.</li>
<li>The nature reserve protects the island: take your rubbish back with you and do not touch the coral.</li>
<li>From the villa, the walk or short drive to the jetty takes about three minutes.</li>
</ul>""",
        },
        "fr": {
            "title": "Îlet Pinel depuis Cul-de-Sac : bateau, plages et snorkeling",
            "desc": "Comment passer une journée sur l'îlet Pinel à Saint-Martin : le bateau depuis Cul-de-Sac, les plages, le sentier sous-marin et nos conseils depuis une villa à trois minutes de l'embarcadère.",
            "h1": "Une journée sur l'îlet Pinel",
            "card": "Le petit bateau part de Cul-de-Sac, à quelques minutes de la villa.",
            "body": """
<p>L'îlet Pinel est la petite île inhabitée qui fait face à la baie de Cul-de-Sac. Eau turquoise et calme, sable blanc et quelques restaurants de plage : c'est l'une des excursions les plus simples et les plus appréciées de Saint-Martin, et depuis la villa vous êtes à trois minutes du bateau.</p>
<h2>Y aller</h2>
<p>De petites navettes partent de l'embarcadère de Cul-de-Sac toute la journée et la traversée ne dure que quelques minutes. Les bateaux circulent en journée et on ne peut pas dormir sur l'îlet : vérifiez l'heure du dernier retour en achetant votre billet. Prévoyez des espèces au cas où la carte ne serait pas acceptée.</p>
<p>Si vous préférez pagayer, la baie est assez abritée pour le kayak et le paddle, que l'on peut louer à Cul-de-Sac.</p>
<h2>Que faire sur l'îlet</h2>
<ul>
<li><strong>Se baigner dans le lagon.</strong> La plage principale donne sur la baie, l'eau y est peu profonde et calme : parfait pour les enfants.</li>
<li><strong>Faire du snorkeling.</strong> Pinel fait partie de la Réserve naturelle de Saint-Martin. Le long du rivage, on voit des poissons, des oursins et parfois des tortues. Apportez votre masque ou louez-en un sur place.</li>
<li><strong>Monter au point de vue.</strong> Un petit sentier grimpe sur la colline, avec vue sur la Baie Orientale et Tintamarre. Prévoyez de vraies chaussures, pas des tongs.</li>
<li><strong>Déjeuner les pieds dans le sable.</strong> Les restaurants de plage servent poisson grillé, langouste et salades, et louent transats et parasols.</li>
<li><strong>Croiser les iguanes.</strong> Ils vivent partout sur l'îlet et sont habitués aux visiteurs. Merci de ne pas les nourrir.</li>
</ul>
<div class="callout"><p><strong>Notre conseil :</strong> prenez les premiers bateaux du matin. La plage est au calme, la lumière est superbe et vous êtes de retour au bord de la piscine pour un déjeuner tardif.</p></div>
<h2>Bon à savoir</h2>
<ul>
<li>Emportez de l'eau, une crème solaire sans danger pour les coraux et un chapeau : il y a peu d'ombre naturelle loin des restaurants.</li>
<li>L'îlet est protégé par la réserve naturelle : rapportez vos déchets et ne touchez pas les coraux.</li>
<li>Depuis la villa, l'embarcadère est à environ trois minutes.</li>
</ul>""",
        },
    },
    "gc": {
        "img": 7,
        "en": {
            "title": "Where to Eat in Grand Case, Saint Martin: Restaurants and Lolos",
            "desc": "A local guide to eating in Grand Case, the culinary capital of Saint Martin: fine dining on the boulevard, beach lolos, Tuesday night street parties and booking tips. Five minutes from our villa.",
            "h1": "Eating in Grand Case",
            "card": "The island's culinary village, five minutes from the villa.",
            "body": """
<p>Grand Case is a small seaside village on the north-west coast of the French side, and it has a big reputation: it is often called the culinary capital of the Caribbean. From the villa in Cul-de-Sac it is about five minutes by car, so it is easy to go for dinner several times during your stay.</p>
<h2>The boulevard</h2>
<p>The main street runs along the beach and is lined with restaurants, many with terraces over the water. The cooking is a mix of French technique and Creole flavours, with plenty of fresh fish and lobster. It is the place for a special dinner at sunset.</p>
<h2>The lolos</h2>
<p>For something relaxed, look for the lolos: open-air grills where locals and visitors share long tables. Expect ribs, grilled chicken, fish and lobster with rice and peas, plantains and johnny cakes, at a much gentler price than the boulevard.</p>
<h2>Tuesday nights</h2>
<p>During the high season, Grand Case hosts a weekly street party on Tuesday evenings, with music, local crafts and food stalls along the boulevard. Arrive early to park and to find a table.</p>
<div class="callout"><p><strong>Our tip:</strong> in high season (roughly December to April), book the restaurants you really want a few days ahead, especially for a sunset table.</p></div>
<h2>Good to know</h2>
<ul>
<li>Parking along the boulevard is limited in the evening. Allow a few extra minutes.</li>
<li>Most restaurants accept cards, but carry some cash for the lolos.</li>
<li>Prices on the French side are usually in euros, and many places also accept US dollars.</li>
</ul>""",
        },
        "fr": {
            "title": "Où manger à Grand Case, Saint-Martin : restaurants et lolos",
            "desc": "Notre guide pour bien manger à Grand Case, capitale gastronomique de Saint-Martin : restaurants du boulevard, lolos, soirées du mardi et conseils de réservation. À cinq minutes de la villa.",
            "h1": "Bien manger à Grand Case",
            "card": "Le village gourmand de l'île, à cinq minutes de la villa.",
            "body": """
<p>Grand Case est un petit village en bord de mer sur la côte nord-ouest de la partie française, et sa réputation le dépasse : on le surnomme souvent la capitale gastronomique des Caraïbes. Depuis la villa à Cul-de-Sac, il est à environ cinq minutes en voiture : facile d'y dîner plusieurs fois pendant le séjour.</p>
<h2>Le boulevard</h2>
<p>La rue principale longe la plage et aligne les restaurants, dont beaucoup ont une terrasse sur l'eau. La cuisine marie technique française et saveurs créoles, avec beaucoup de poisson frais et de langouste. C'est l'adresse pour un dîner d'exception au coucher du soleil.</p>
<h2>Les lolos</h2>
<p>Pour une soirée décontractée, cherchez les lolos : des grills en plein air où habitants et visiteurs partagent de grandes tablées. Au menu, travers de porc, poulet et poisson grillés, langouste, riz aux pois, bananes plantains et johnny cakes, pour un prix bien plus doux que sur le boulevard.</p>
<h2>Les mardis soir</h2>
<p>En haute saison, Grand Case organise chaque mardi soir une fête de rue avec musique, artisanat et stands de nourriture le long du boulevard. Arrivez tôt pour vous garer et trouver une table.</p>
<div class="callout"><p><strong>Notre conseil :</strong> en haute saison (environ de décembre à avril), réservez quelques jours à l'avance les restaurants qui vous tiennent à cœur, surtout pour une table au coucher du soleil.</p></div>
<h2>Bon à savoir</h2>
<ul>
<li>Le stationnement le long du boulevard est limité le soir : prévoyez quelques minutes de plus.</li>
<li>La plupart des restaurants acceptent la carte, mais gardez des espèces pour les lolos.</li>
<li>Côté français, les prix sont généralement en euros, et beaucoup d'adresses acceptent aussi les dollars américains.</li>
</ul>""",
        },
    },
    "beaches": {
        "img": 6,
        "en": {
            "title": "Best Beaches on the French Side of Saint Martin (Local Guide)",
            "desc": "The best beaches of French Saint Martin near Cul-de-Sac: Orient Bay, Pinel Island, Grand Case, Friar's Bay, Happy Bay, Baie Rouge, Baie Longue and Anse Marcel, with tips for families and snorkelers.",
            "h1": "Beaches of the French side",
            "card": "From lively Orient Bay to quiet coves for snorkeling.",
            "body": """
<p>The French side of Saint Martin has some of the island's most beautiful beaches, and from Cul-de-Sac most of them are within a short drive. Here is how we would choose, depending on the day you want.</p>
<h2>Near the villa</h2>
<ul>
<li><strong>Orient Bay (Baie Orientale).</strong> The island's most famous beach, about five minutes away: a long curve of white sand with beach clubs, sunbeds and water sports. Lively, great for a full beach day.</li>
<li><strong>Pinel Island.</strong> Calm, shallow water facing Cul-de-Sac, reached by a short boat ride. Perfect for families. <a href="{pinel}">Read our Pinel Island guide</a>.</li>
<li><strong>Le Galion.</strong> A sheltered, shallow bay on the east coast, popular with families and with kitesurfers when the wind picks up.</li>
<li><strong>Anse Marcel.</strong> A small protected cove to the north, with calm water and a marina.</li>
</ul>
<h2>On the north-west coast</h2>
<ul>
<li><strong>Grand Case.</strong> A long, easygoing beach in front of the restaurants, ideal before dinner. <a href="{gc}">See where to eat in Grand Case</a>.</li>
<li><strong>Friar's Bay (Anse des Pères).</strong> A calm bay with a relaxed local feel and beach bars.</li>
<li><strong>Happy Bay.</strong> A quiet beach reached by a short walk from Friar's Bay. Bring water and shade.</li>
</ul>
<h2>Further west</h2>
<ul>
<li><strong>Baie Rouge.</strong> Golden-pink sand and some of the best snorkeling on the French side, around the rocks at each end.</li>
<li><strong>Baie Longue.</strong> A very long, quiet beach, wonderful at sunset.</li>
</ul>
<div class="callout"><p><strong>Our tip:</strong> the Atlantic-facing beaches on the east coast can receive sargassum seaweed at some times of year. If one beach is affected, the Caribbean-facing west coast is often clear. Ask us, we will tell you where to go that day.</p></div>
<h2>Good to know</h2>
<ul>
<li>A rental car is the easiest way to explore the beaches.</li>
<li>Most beaches have no lifeguards. Check the conditions and keep an eye on children.</li>
<li>Bring reef-safe sunscreen and take your rubbish with you.</li>
</ul>""",
        },
        "fr": {
            "title": "Les plus belles plages de Saint-Martin côté français (guide local)",
            "desc": "Les plus belles plages de la partie française de Saint-Martin près de Cul-de-Sac : Baie Orientale, îlet Pinel, Grand Case, Anse des Pères, Happy Bay, Baie Rouge, Baie Longue et Anse Marcel.",
            "h1": "Les plages du côté français",
            "card": "De la Baie Orientale animée aux criques calmes pour le snorkeling.",
            "body": """
<p>La partie française de Saint-Martin abrite certaines des plus belles plages de l'île, et depuis Cul-de-Sac la plupart sont à quelques minutes de route. Voici comment nous choisirions, selon la journée que vous voulez.</p>
<h2>Près de la villa</h2>
<ul>
<li><strong>Baie Orientale.</strong> La plage la plus célèbre de l'île, à environ cinq minutes : un long arc de sable blanc avec clubs de plage, transats et sports nautiques. Animée, idéale pour une vraie journée plage.</li>
<li><strong>Îlet Pinel.</strong> Eau calme et peu profonde face à Cul-de-Sac, accessible par un court trajet en bateau. Parfait pour les familles. <a href="{pinel}">Lire notre guide de l'îlet Pinel</a>.</li>
<li><strong>Le Galion.</strong> Une baie abritée et peu profonde sur la côte est, appréciée des familles et des kitesurfeurs quand le vent se lève.</li>
<li><strong>Anse Marcel.</strong> Une petite crique protégée au nord, avec une eau calme et une marina.</li>
</ul>
<h2>Sur la côte nord-ouest</h2>
<ul>
<li><strong>Grand Case.</strong> Une longue plage tranquille devant les restaurants, parfaite avant le dîner. <a href="{gc}">Voir où manger à Grand Case</a>.</li>
<li><strong>Anse des Pères (Friar's Bay).</strong> Une baie calme à l'ambiance locale, avec des bars de plage.</li>
<li><strong>Happy Bay.</strong> Une plage paisible accessible par une courte marche depuis l'Anse des Pères. Prévoyez eau et ombre.</li>
</ul>
<h2>Plus à l'ouest</h2>
<ul>
<li><strong>Baie Rouge.</strong> Sable doré rosé et l'un des meilleurs spots de snorkeling côté français, autour des rochers aux deux extrémités.</li>
<li><strong>Baie Longue.</strong> Une très longue plage tranquille, magnifique au coucher du soleil.</li>
</ul>
<div class="callout"><p><strong>Notre conseil :</strong> les plages de la côte est, face à l'Atlantique, peuvent recevoir des sargasses à certaines périodes. Dans ce cas, la côte ouest, côté mer des Caraïbes, est souvent épargnée. Demandez-nous, nous vous dirons où aller ce jour-là.</p></div>
<h2>Bon à savoir</h2>
<ul>
<li>Une voiture de location est le plus simple pour découvrir les plages.</li>
<li>La plupart des plages ne sont pas surveillées : vérifiez les conditions et surveillez les enfants.</li>
<li>Utilisez une crème solaire sans danger pour les coraux et rapportez vos déchets.</li>
</ul>""",
        },
    },
    "season": {
        "img": 4,
        "en": {
            "title": "Best Time to Visit Saint Martin: Weather, Seasons and Events by Month",
            "desc": "When to go to Saint Martin: dry season from December to April, quieter months from May to November, hurricane season, sea temperature, Carnival and the island's main events. A local guide from our villa in Cul-de-Sac.",
            "h1": "The best time to visit Saint Martin",
            "card": "Weather, seasons and events, month by month.",
            "body": """
<p>Saint Martin is warm all year round, with air temperatures that usually stay between the mid-20s and low 30s °C (high 70s to high 80s °F) and sea water warm enough to swim in every month. What changes through the year is rainfall, wind, crowds and prices. Here is how the seasons work, so you can pick the trip that suits you.</p>
<h2>December to April: the dry season</h2>
<p>This is the classic Caribbean high season. Days are sunny, humidity is lower and the trade winds keep evenings pleasant. It is the most popular time to visit, especially around Christmas, New Year and the North American spring breaks, so the best villas and restaurants book up early.</p>
<ul>
<li><strong>Good for:</strong> guaranteed sunshine, beach days, boat trips to Pinel Island and Tintamarre.</li>
<li><strong>Plan ahead:</strong> book your villa and flights several months in advance, and reserve your favourite restaurants in Grand Case a few days ahead.</li>
</ul>
<h2>May to July: the sweet spot</h2>
<p>Early summer is often the best value. The weather is still mostly dry and sunny, the sea is calm and warm, the island is quieter and rates are lower. It is a great time for families and for longer stays.</p>
<h2>August to November: the quiet season</h2>
<p>The Atlantic hurricane season officially runs from 1 June to 30 November, with most activity usually between August and October. Many days are still sunny, with short tropical showers, but some restaurants and hotels close for a few weeks around September and October. If you travel in this period, choose flexible bookings and travel insurance, and keep an eye on the forecast.</p>
<div class="callout"><p><strong>Our tip:</strong> for the best balance of sunshine, calm seas and lower prices, look at late April, May and June. You get the island at its most relaxed.</p></div>
<h2>Events worth planning around</h2>
<ul>
<li><strong>Carnival:</strong> the French side celebrates in the weeks before Lent (usually February or early March), with parades in Marigot and Grand Case. The Dutch side holds its own Carnival later in spring.</li>
<li><strong>Sailing regattas:</strong> the island hosts well-known regattas in late winter and spring, when the bays fill with sailing boats.</li>
<li><strong>Tuesday nights in Grand Case:</strong> during the high season, the village hosts a weekly street party with music and food stalls. <a href="{gc}">See our Grand Case guide</a>.</li>
</ul>
<h2>Good to know whatever the season</h2>
<ul>
<li>The sun is strong all year: bring reef-safe sunscreen, a hat and water.</li>
<li>Sargassum seaweed can reach east-facing beaches at some times of year. The west coast is often clear when the east is affected. <a href="{beaches}">See our beach guide</a>.</li>
<li>Event dates change every year, so check them before you book.</li>
</ul>""",
        },
        "fr": {
            "title": "Quand partir à Saint-Martin : météo, saisons et événements mois par mois",
            "desc": "Quand partir à Saint-Martin : saison sèche de décembre à avril, mois plus calmes de mai à novembre, saison cyclonique, température de l'eau, carnaval et grands événements. Notre guide local depuis la villa à Cul-de-Sac.",
            "h1": "Quand partir à Saint-Martin",
            "card": "Météo, saisons et événements, mois par mois.",
            "body": """
<p>Il fait chaud toute l'année à Saint-Martin : l'air se situe généralement entre 25 et 31 °C, et la mer est assez chaude pour se baigner en toute saison. Ce qui change au fil de l'année, ce sont la pluie, le vent, la fréquentation et les prix. Voici comment fonctionnent les saisons, pour choisir le séjour qui vous ressemble.</p>
<h2>De décembre à avril : la saison sèche</h2>
<p>C'est la haute saison classique des Caraïbes. Les journées sont ensoleillées, l'air est moins humide et les alizés rendent les soirées agréables. C'est la période la plus demandée, surtout autour de Noël, du Nouvel An et des vacances de printemps nord-américaines : les belles villas et les restaurants se réservent tôt.</p>
<ul>
<li><strong>Idéal pour :</strong> le soleil garanti, les journées plage, les sorties en bateau vers l'îlet Pinel et Tintamarre.</li>
<li><strong>À anticiper :</strong> réservez villa et vols plusieurs mois à l'avance, et vos restaurants préférés à Grand Case quelques jours avant.</li>
</ul>
<h2>De mai à juillet : le bon compromis</h2>
<p>Le début de l'été offre souvent le meilleur rapport qualité-prix. Le temps reste en grande partie sec et ensoleillé, la mer est calme et chaude, l'île est plus tranquille et les tarifs sont plus doux. Une très bonne période pour les familles et les longs séjours.</p>
<h2>D'août à novembre : la saison calme</h2>
<p>La saison cyclonique de l'Atlantique s'étend officiellement du 1er juin au 30 novembre, avec l'essentiel de l'activité en général entre août et octobre. Beaucoup de journées restent ensoleillées, avec de courtes averses tropicales, mais certains restaurants et hôtels ferment quelques semaines vers septembre et octobre. Si vous voyagez à cette période, privilégiez une réservation flexible et une assurance voyage, et surveillez la météo.</p>
<div class="callout"><p><strong>Notre conseil :</strong> pour le meilleur équilibre entre soleil, mer calme et prix doux, regardez fin avril, mai et juin. Vous profitez de l'île dans sa version la plus détendue.</p></div>
<h2>Les événements à prévoir</h2>
<ul>
<li><strong>Le carnaval :</strong> le côté français le fête dans les semaines qui précèdent le Carême (en général en février ou début mars), avec des défilés à Marigot et Grand Case. Le côté hollandais organise le sien plus tard au printemps.</li>
<li><strong>Les régates :</strong> l'île accueille des régates réputées à la fin de l'hiver et au printemps, quand les baies se remplissent de voiliers.</li>
<li><strong>Les mardis soir à Grand Case :</strong> en haute saison, le village organise chaque semaine une fête de rue avec musique et stands. <a href="{gc}">Voir notre guide de Grand Case</a>.</li>
</ul>
<h2>Bon à savoir, quelle que soit la saison</h2>
<ul>
<li>Le soleil tape fort toute l'année : crème solaire sans danger pour les coraux, chapeau et eau.</li>
<li>Des sargasses peuvent toucher les plages exposées à l'est à certaines périodes. La côte ouest est souvent épargnée. <a href="{beaches}">Voir notre guide des plages</a>.</li>
<li>Les dates des événements changent chaque année : vérifiez-les avant de réserver.</li>
</ul>""",
        },
    },
    "airport": {
        "img": 10,
        "en": {
            "title": "Getting to Cul-de-Sac from SXM Airport: Flights, Car Rental and Driving Tips",
            "desc": "How to get from Princess Juliana Airport (SXM) to Cul-de-Sac on the French side of Saint Martin: flights, car rental, the 30-minute drive, crossing between the Dutch and French sides, currency and practical tips.",
            "h1": "From SXM airport to the villa",
            "card": "Flights, car rental and the 30-minute drive.",
            "body": """
<p>Most visitors arrive at Princess Juliana International Airport (SXM), on the Dutch side of the island. The villa is in Cul-de-Sac, on the French side, about 30 minutes away by car. Here is everything you need for a smooth arrival.</p>
<h2>Flying in</h2>
<ul>
<li><strong>Princess Juliana International (SXM)</strong> is the island's main airport, with direct flights from several cities in the United States, Canada and Europe, depending on the season. It is famous for the planes landing just above Maho Beach.</li>
<li><strong>Grand Case–Espérance (SFG)</strong> is a small regional airport on the French side, used mainly for short hops to and from nearby islands such as Guadeloupe and St Barths.</li>
</ul>
<h2>Renting a car</h2>
<p>A car is by far the easiest way to explore the beaches, Grand Case and Marigot. Two options:</p>
<ul>
<li><strong>Rent a car from us.</strong> We rent our own cars to guests at a friendly daily rate, and we can also pick you up at the airport and drive you to the villa. Just ask on WhatsApp when you contact us.</li>
<li><strong>Rent from an agency.</strong> Rental companies have desks at or near the airport. Book ahead in high season, when cars can run out.</li>
</ul>
<ul>
<li>Driving is on the right, as in the United States and mainland Europe.</li>
<li>Roads are narrow in places and traffic can be slow around Simpson Bay and Philipsburg at rush hour.</li>
<li>The villa has private parking.</li>
</ul>
<h2>The drive to Cul-de-Sac</h2>
<p>If you prefer not to drive after your flight, we can pick you up at arrivals: ask us on WhatsApp. If you drive yourself, the route crosses from the Dutch side to the French side without any border control: the two sides have shared the island freely for centuries. Count about 30 minutes in normal traffic. We send detailed directions and the exact address after booking, and arrival is self check-in, so you can arrive at your own pace.</p>
<div class="callout"><p><strong>Our tip:</strong> stop at a supermarket on the way for breakfast and drinks, so you can enjoy your first evening by the pool without going out again.</p></div>
<h2>Practical information</h2>
<ul>
<li><strong>Currency:</strong> the euro on the French side, the Caribbean guilder on the Dutch side. US dollars are widely accepted across the island, and cards are accepted in most places.</li>
<li><strong>Language:</strong> French on the French side, but English is spoken almost everywhere.</li>
<li><strong>Electricity:</strong> the French side uses European-style plugs. Bring an adapter for American devices.</li>
<li><strong>Entry requirements:</strong> rules depend on your nationality. Check the official requirements for Saint-Martin before you travel.</li>
</ul>""",
        },
        "fr": {
            "title": "De l'aéroport SXM à Cul-de-Sac : vols, location de voiture et conseils de route",
            "desc": "Comment aller de l'aéroport Princess Juliana (SXM) à Cul-de-Sac, côté français de Saint-Martin : vols, location de voiture, 30 minutes de route, passage entre côté hollandais et côté français, monnaie et conseils pratiques.",
            "h1": "De l'aéroport SXM à la villa",
            "card": "Vols, location de voiture et 30 minutes de route.",
            "body": """
<p>La plupart des voyageurs arrivent à l'aéroport international Princess Juliana (SXM), côté hollandais. La villa se trouve à Cul-de-Sac, côté français, à environ 30 minutes en voiture. Voici tout ce qu'il faut savoir pour une arrivée en douceur.</p>
<h2>En avion</h2>
<ul>
<li><strong>Princess Juliana (SXM)</strong> est l'aéroport principal de l'île, avec des vols directs depuis plusieurs villes des États-Unis, du Canada et d'Europe selon la saison, dont Paris. Il est célèbre pour ses avions qui atterrissent juste au-dessus de la plage de Maho.</li>
<li><strong>Grand Case–L'Espérance (SFG)</strong> est un petit aéroport régional côté français, utilisé surtout pour les liaisons avec les îles voisines comme la Guadeloupe et Saint-Barthélemy.</li>
</ul>
<h2>Louer une voiture</h2>
<p>Une voiture est de loin le plus simple pour découvrir les plages, Grand Case et Marigot. Deux possibilités :</p>
<ul>
<li><strong>Louer une voiture auprès de nous.</strong> Nous louons nos propres voitures à nos voyageurs, à un tarif journalier sympathique, et nous pouvons aussi venir vous chercher à l'aéroport pour vous conduire à la villa. Demandez-le-nous sur WhatsApp quand vous nous contactez.</li>
<li><strong>Louer auprès d'une agence.</strong> Les loueurs ont des comptoirs à l'aéroport ou à proximité. Réservez à l'avance en haute saison, les voitures peuvent manquer.</li>
</ul>
<ul>
<li>On roule à droite, comme en France.</li>
<li>Les routes sont parfois étroites, et la circulation peut être lente autour de Simpson Bay et Philipsburg aux heures de pointe.</li>
<li>La villa dispose d'un parking privé.</li>
</ul>
<h2>La route jusqu'à Cul-de-Sac</h2>
<p>Si vous préférez ne pas conduire après le vol, nous pouvons venir vous chercher à l'arrivée : demandez-le-nous sur WhatsApp. Si vous conduisez vous-même, on passe du côté hollandais au côté français sans aucun contrôle : les deux parties partagent librement l'île depuis des siècles. Comptez environ 30 minutes sans embouteillage. Nous vous envoyons l'itinéraire détaillé et l'adresse exacte après la réservation, et l'arrivée est autonome : vous arrivez à votre rythme.</p>
<div class="callout"><p><strong>Notre conseil :</strong> arrêtez-vous dans un supermarché sur la route pour le petit-déjeuner et les boissons, et profitez de votre première soirée au bord de la piscine sans ressortir.</p></div>
<h2>Infos pratiques</h2>
<ul>
<li><strong>Monnaie :</strong> l'euro côté français, le florin caribéen côté hollandais. Le dollar américain est accepté presque partout, et la carte bancaire dans la plupart des commerces.</li>
<li><strong>Langue :</strong> le français côté français, mais l'anglais est parlé presque partout.</li>
<li><strong>Électricité :</strong> prises européennes côté français, comme en métropole.</li>
<li><strong>Formalités :</strong> elles dépendent de votre nationalité. Vérifiez les conditions officielles d'entrée à Saint-Martin avant de partir.</li>
</ul>""",
        },
    },
}


def page_meta(lang, cfg):
    """Titre, description et en-tête de chaque page (hors accueil et guides)."""
    frm = cfg.money(lang, cfg.PRICE_FROM_EUR)
    pct, k = int(cfg.WEEKLY_DISCOUNT * 100), cfg.WEEKLY_MIN_NIGHTS
    if lang == "en":
        return {
            "villa": ("4-Bedroom Villa with Private Pool in Cul-de-Sac, Saint Martin | Spacious Villa",
                      "Inside Spacious Villa: 4 bedrooms, 3.5 bathrooms, private pool, sea views, fenced garden and full amenities for up to 8 guests in Cul-de-Sac, French Saint Martin.",
                      "The villa", "Four bedrooms, a private pool and room for eight, on the French side of Saint Martin."),
            "photos": ("Photos of Spacious Villa | Pool Villa in Cul-de-Sac, Saint Martin",
                       "See the private pool, sea-view terraces, living spaces and bedrooms of Spacious Villa in Cul-de-Sac, Saint Martin.",
                       "Photos", "The pool, the terraces, the living spaces and the bedrooms. Tap a photo to see it full screen."),
            "location": ("Location: Cul-de-Sac, Minutes from Pinel Island and Orient Bay | Spacious Villa",
                         "Spacious Villa is in Cul-de-Sac, French Saint Martin: 3 minutes from the Pinel Island boat, 5 minutes from Orient Beach and Grand Case, 30 minutes from SXM airport.",
                         "Location", "Close to everything, quiet at home."),
            "book": ("Rates and Booking | Spacious Villa, Saint Martin (Book Direct)",
                     f"Rates from {frm} per night, {pct}% off stays of {k} nights or more, no platform fees. Calculate the price of your stay and request your dates directly with the owners.",
                     "Rates and booking", "Booking with us directly means a simpler stay and a better deal."),
            "faq": ("FAQ: Check-in, Payment, Pets and Cancellation | Spacious Villa",
                    "Answers about check-in times, rates, payment, deposit, pets, house rules and cancellation at Spacious Villa, Cul-de-Sac, Saint Martin.",
                    "Good to know", "What guests ask us before booking."),
        }
    return {
        "villa": ("Villa 4 chambres avec piscine privée à Cul-de-Sac, Saint-Martin | Spacious Villa",
                  "Découvrez Spacious Villa : 4 chambres, 3,5 salles de bain, piscine privée, vue mer, jardin clos et tous les équipements pour 8 voyageurs à Cul-de-Sac, Saint-Martin.",
                  "La villa", "Quatre chambres, une piscine privée et de la place pour huit, côté français de Saint-Martin."),
        "photos": ("Photos de Spacious Villa | Villa avec piscine à Cul-de-Sac, Saint-Martin",
                   "La piscine privée, les terrasses vue mer, les pièces de vie et les chambres de Spacious Villa à Cul-de-Sac, Saint-Martin.",
                   "Photos", "La piscine, les terrasses, les pièces de vie et les chambres. Touchez une photo pour l'agrandir."),
        "location": ("Emplacement : Cul-de-Sac, près de l'îlet Pinel et de la Baie Orientale | Spacious Villa",
                     "Spacious Villa se trouve à Cul-de-Sac, Saint-Martin côté français : à 3 minutes du bateau pour l'îlet Pinel, 5 minutes de la Baie Orientale et de Grand Case, 30 minutes de l'aéroport SXM.",
                     "Emplacement", "Proche de tout, au calme chez vous."),
        "book": ("Tarifs et réservation | Spacious Villa, Saint-Martin (réservation directe)",
                 f"À partir de {frm} la nuit, −{pct} % dès {k} nuits, sans frais de plateforme. Calculez le prix de votre séjour et demandez vos dates directement aux propriétaires.",
                 "Tarifs et réservation", "Réserver directement avec nous, c'est un séjour plus simple et un meilleur prix."),
        "faq": ("FAQ : arrivée, paiement, animaux et annulation | Spacious Villa",
                "Les réponses sur les horaires d'arrivée, les tarifs, le paiement, la caution, les animaux, le règlement et l'annulation à Spacious Villa, Cul-de-Sac, Saint-Martin.",
                "Bon à savoir", "Ce que nos voyageurs nous demandent avant de réserver."),
    }


# Avis réels (Airbnb), texte original + traduction signalée comme telle
REVIEWS = [
    {"name": "Chris", "city": ("Glen Ellyn, Illinois", "Glen Ellyn, Illinois"), "date": ("April 2026", "avril 2026"),
     "trip": ("Stay with children", "Séjour avec enfants"), "lang": "en", "home": False,
     "text": "Stop looking and immediately book Fanilia's home; easily the best value, best host and best location on the island. Have rented many AirBnbs over the years and I can't recall a friendlier, more communicative or just overall nicer host. Fanilia was helpful with local recommendations (beaches, restaurants), proactively reached out about island water shortages (occasionally happen but house has backup) and answered all our questions with a smile. Listing photos reflect the property accurately, with the pool larger than we anticipated. The outdoor area was spacious and outdoor furniture was high quality and plentiful. The views were beautiful (salt flat/ocean) and the house was well stocked (toilet paper, spices, etc). Beach towels, umbrellas, chairs and snorkeling gear provided. Bedroom AC worked really well. Location equidistant from Orient Beach and Grand Case, which we great. Delicious bakery walkable. Loved being higher up on hill for breeze during day and at night. So pleased!",
     "tr": "Arrêtez de chercher et réservez tout de suite la maison de Fanilia : de loin le meilleur rapport qualité-prix, la meilleure hôte et le meilleur emplacement de l'île. J'ai loué beaucoup d'Airbnb au fil des ans et je ne me souviens pas d'une hôte plus aimable, plus communicative ou tout simplement plus agréable. Fanilia nous a donné de bonnes adresses (plages, restaurants), nous a prévenus d'elle-même des coupures d'eau sur l'île (cela arrive parfois, mais la maison a une réserve) et a répondu à toutes nos questions avec le sourire. Les photos de l'annonce sont fidèles, et la piscine est plus grande que prévu. L'extérieur est spacieux, avec du mobilier de jardin de qualité et en quantité. La vue est magnifique (salines et océan) et la maison est bien équipée (papier toilette, épices, etc.). Serviettes de plage, parasols, chaises et matériel de snorkeling fournis. La climatisation des chambres fonctionnait très bien. L'emplacement est à égale distance de la Baie Orientale et de Grand Case, ce qui était parfait. Une délicieuse boulangerie à pied. Nous avons adoré être en hauteur, avec la brise le jour comme la nuit. Ravis !"},
    {"name": "James", "city": ("New Haven, Connecticut", "New Haven, Connecticut"), "date": ("July 2026", "juillet 2026"),
     "trip": ("Stay with children", "Séjour avec enfants"), "lang": "en", "home": False,
     "text": "I must say I've rented many houses all over the world. This host is the best of them all. She was very accommodating and gave amazing suggestions and was very quick to respond. The house is perfect, the flow is very nice and the pool is beautiful. House is very clean and safe. 4 minute drive to Orient Beach and the ferry to Pinel Island. Host has two cars for you to use and trust you to pay her a nominal fee for the days you use the car. I took my family and in-laws. Great vacation. In fact, we are booking it now for two weeks next summer. This might turn out to be one of our favorite spots and we will return again and again.",
     "tr": "J'ai loué beaucoup de maisons dans le monde entier, et cette hôte est la meilleure de toutes. Très arrangeante, d'excellents conseils et très réactive. La maison est parfaite, bien agencée, et la piscine est superbe. La maison est très propre et sûre. À 4 minutes en voiture de la Baie Orientale et du bateau pour l'îlet Pinel. L'hôte met deux voitures à disposition pour un petit montant par jour d'utilisation. J'y suis allé avec ma famille et ma belle-famille : de superbes vacances. D'ailleurs, nous réservons déjà deux semaines pour l'été prochain. Ce sera peut-être l'un de nos endroits préférés, et nous y reviendrons encore et encore."},
    {"name": "Ruth", "city": ("Deposit, New York", "Deposit, New York"), "date": ("March 2026", "mars 2026"),
     "trip": ("Group trip", "Voyage en groupe"), "lang": "en", "home": True,
     "text": "WOW! This place was as beautiful as the pictures. We loved the spaciousness. Fanilia was very responsive to any questions we had. The place was spotless and very nicely kept. It had everything you could possibly need. Easy walk or drive to any place we needed to be. The pool was beautiful - we enjoyed it every day. Wish we could have stayed longer!!!",
     "tr": "WOW ! La maison est aussi belle que sur les photos. Nous avons adoré l'espace. Fanilia a répondu rapidement à toutes nos questions. Tout était impeccable et très bien entretenu, avec tout ce dont on peut avoir besoin. Facile d'aller partout à pied ou en voiture. La piscine est magnifique, nous en avons profité tous les jours. Nous aurions aimé rester plus longtemps !"},
    {"name": "Matt", "city": ("Asheville, North Carolina", "Asheville, Caroline du Nord"), "date": ("December 2025", "décembre 2025"),
     "trip": ("Stay with children", "Séjour avec enfants"), "lang": "en", "home": True,
     "text": "What a gem - the house and the owners! We stayed here for a week with two families. The outdoor space was a dream! Our kids loved the pool floats. We used the provided beach chairs and beach towels every day. The AC units in all the bedrooms worked great. We rented the hosts' cars for the week and it worked out very well. Fani and Jon were so friendly and helpful. Very peaceful neighborhood. Would definitely recommend!",
     "tr": "Une perle, la maison comme les propriétaires ! Nous y avons passé une semaine avec deux familles. L'extérieur est un rêve ! Nos enfants ont adoré les bouées de la piscine. Nous avons utilisé tous les jours les chaises et serviettes de plage fournies. La climatisation fonctionnait très bien dans toutes les chambres. Nous avons loué les voitures des hôtes pour la semaine, et c'était très pratique. Fani et Jon ont été très aimables et serviables. Quartier très paisible. Je recommande sans hésiter !"},
    {"name": "Stéphane", "city": ("Quebec, Canada", "Québec, Canada"), "date": ("January 2026", "janvier 2026"),
     "trip": ("Group trip", "Voyage en groupe"), "lang": "fr", "home": False,
     "text": "L'emplacement est tout simplement parfait, idéal pour explorer la région tout en profitant d'un cadre paisible et pittoresque. La propreté des lieux mérite également d'être soulignée. La piscine a été un véritable atout, offrant des moments de détente inoubliables sous le soleil. La vue depuis la villa est à couper le souffle, nous avons passé de merveilleux moments à simplement admirer le paysage. De plus, nous avons particulièrement apprécié la qualité de la communication avec Fanilia et Jean. Votre disponibilité et votre réactivité ont grandement facilité notre séjour.",
     "tr": "The location is simply perfect, ideal for exploring the area while enjoying a peaceful, picturesque setting. The cleanliness also deserves a mention. The pool was a real highlight, with unforgettable moments of relaxation in the sun. The view from the villa is breathtaking; we spent wonderful moments just admiring the scenery. We especially appreciated the communication with Fanilia and Jean. Your availability and responsiveness made our stay so much easier."},
    {"name": "Jamoris", "city": ("Lake City, Florida", "Lake City, Floride"), "date": ("April 2026", "avril 2026"),
     "trip": ("Short stay", "Séjour de quelques nuits"), "lang": "en", "home": True,
     "text": "The place was amazing, I felt at home the moment I entered onto the property!! The hosts greeted me and my family at check-in. The host introduced us to a transportation guy who helped us around the island!!! If I come back to the island I would choose this spot again. (Home away from home)",
     "tr": "Un endroit incroyable, je me suis senti chez moi dès mon arrivée ! Les hôtes nous ont accueillis, ma famille et moi, à l'arrivée, et nous ont présenté un chauffeur qui nous a fait découvrir l'île ! Si je reviens sur l'île, je choisirai de nouveau cette maison. (Comme à la maison)"},
    {"name": "Pascale", "city": ("Candiac, Canada", "Candiac, Canada"), "date": ("April 2024", "avril 2024"),
     "trip": ("Group trip", "Voyage en groupe"), "lang": "fr", "home": False,
     "text": "Nous avons eu droit au meilleur accueil avec Fanilia. Ils sont très généreux et merveilleux. La maison est magnifique, encore plus belle que sur les photos. Nous avons eu des recommandations locales et avons adoré notre expérience. C'est un des meilleurs Airbnb que j'ai loué dans ma vie et j'en ai fait plusieurs ! Nous étions 4 couples et extrêmement confortables. La piscine a été extrêmement appréciée et la proximité de la plage est géniale. Il y a même des autos à notre disposition moyennant un coût très raisonnable. J'y retournerai sans aucune hésitation.",
     "tr": "We received the warmest welcome from Fanilia. They are so generous and wonderful. The house is gorgeous, even more beautiful than in the photos. We got local recommendations and loved our experience. It is one of the best Airbnbs I have ever rented, and I have rented quite a few! We were four couples and extremely comfortable. Everyone loved the pool, and being so close to the beach is fantastic. There are even cars available for a very reasonable fee. I will go back without hesitation."},
    {"name": "Lakia", "city": ("Fort Lauderdale, Florida", "Fort Lauderdale, Floride"), "date": ("June 2026", "juin 2026"),
     "trip": ("Stay with children", "Séjour avec enfants"), "lang": "en", "home": False,
     "text": "Great stay and host, she was very responsive. We were celebrating a birthday and anniversary, she provided a nice decor with balloons. Very nice Airbnb, plenty of space, the outdoor pool area is a nice vibe.",
     "tr": "Super séjour et super hôte, très réactive. Nous fêtions un anniversaire et un anniversaire de mariage : elle avait préparé une jolie décoration avec des ballons. Très bel Airbnb, beaucoup d'espace, et une super ambiance autour de la piscine."},
]

# Services sur demande (navette aéroport, location de voiture)
SERVICES = {
    "en": {
        "h": "Airport pick-up and car rental",
        "p": "We can pick you up at SXM airport and drive you to the villa, and take you back at the end of your stay. We also rent our own cars to guests, at a friendly daily rate. Just ask on WhatsApp when you contact us.",
        "items": ["Airport pick-up and drop-off on request", "Car rental from the hosts on request", "Local tips: beaches, restaurants, boat trips"],
        "btn": "Ask on WhatsApp",
        "wa": "Hello, we would like to ask about airport pick-up and car rental for our stay at Spacious Villa.",
    },
    "fr": {
        "h": "Navette aéroport et location de voiture",
        "p": "Nous pouvons venir vous chercher à l'aéroport SXM pour vous conduire à la villa, et vous y ramener en fin de séjour. Nous louons aussi nos propres voitures à nos voyageurs, à un tarif journalier sympathique. Demandez-le-nous simplement sur WhatsApp quand vous nous contactez.",
        "items": ["Navette aéroport aller et retour sur demande", "Location de voiture auprès des hôtes sur demande", "Nos bonnes adresses : plages, restaurants, sorties en bateau"],
        "btn": "Demander sur WhatsApp",
        "wa": "Bonjour, nous aimerions avoir des informations sur la navette aéroport et la location de voiture pour notre séjour à Spacious Villa.",
    },
}

# Lieux autour de la villa (page Emplacement). Photo facultative : static/img/places/<clé>.jpg
PLACES = [
    {"key": "pinel", "time": "3 min", "guide": "pinel",
     "en": ("Pinel Island", "by car to the boat", "A small, protected island with calm turquoise water, beach restaurants and a snorkeling trail. The boat leaves from the Cul-de-Sac jetty and the crossing takes only a few minutes."),
     "fr": ("L'îlet Pinel", "en voiture jusqu'au bateau", "Une petite île protégée, une eau turquoise et calme, des restaurants de plage et un sentier sous-marin. Le bateau part de l'embarcadère de Cul-de-Sac et la traversée ne dure que quelques minutes.")},
    {"key": "orient", "time": "5 min", "guide": "beaches",
     "en": ("Orient Bay", "by car", "The island's most famous beach: a long curve of white sand with beach clubs, sunbeds and water sports."),
     "fr": ("La Baie Orientale", "en voiture", "La plage la plus célèbre de l'île : un long arc de sable blanc, des clubs de plage, des transats et des sports nautiques.")},
    {"key": "grandcase", "time": "5 min", "guide": "gc",
     "en": ("Grand Case", "by car", "The culinary village of Saint Martin, with seaside restaurants, beach grills called lolos and a lively street party on Tuesday nights in high season."),
     "fr": ("Grand Case", "en voiture", "Le village gourmand de Saint-Martin : restaurants en bord de mer, grills de plage appelés lolos et fête de rue animée le mardi soir en haute saison.")},
    {"key": "village", "time": "2 min", "guide": None,
     "en": ("Cul-de-Sac village", "on foot", "Restaurants and a bakery within walking distance, and a quiet residential neighbourhood on the hillside, with a breeze day and night."),
     "fr": ("Le village de Cul-de-Sac", "à pied", "Restaurants et boulangerie à pied, dans un quartier résidentiel calme à flanc de colline, avec de la brise le jour comme la nuit.")},
    {"key": "airport", "time": "30 min", "guide": "airport",
     "en": ("SXM airport", "by car", "Princess Juliana International Airport, on the Dutch side. We can pick you up on request."),
     "fr": ("L'aéroport SXM", "en voiture", "L'aéroport international Princess Juliana, côté hollandais. Nous pouvons venir vous chercher sur demande.")},
]
