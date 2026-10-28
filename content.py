"""Textes du site, en anglais et en français."""

PHOTOS = [
    ("villa-pool-gazebo.jpg", "", (1452, 966),
     "Private pool, gazebo and yellow villa beneath the Saint Martin hills",
     "Piscine privée, gazebo et villa jaune au pied des collines de Saint-Martin"),
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
    "pinel":   ("pinel-island.html", "fr/ilet-pinel.html"),
    "gc":      ("grand-case-restaurants.html", "fr/restaurants-grand-case.html"),
    "beaches": ("saint-martin-beaches.html", "fr/plages-saint-martin.html"),
    "legal":   ("legal-notice.html", "fr/mentions-legales.html"),
    "privacy": ("privacy.html", "fr/confidentialite.html"),
    "thanks":  ("thanks.html", "fr/merci.html"),
}

UI = {
    "en": {
        "nav": [("#villa", "The villa"), ("#photos", "Photos"), ("#location", "Location"), ("#faq", "FAQ")],
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
        "nav": [("#villa", "La villa"), ("#photos", "Photos"), ("#location", "Emplacement"), ("#faq", "FAQ")],
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
        "price_on_req": "Rate on request",
        "price_from": lambda p: f"From <strong>€{p}</strong> per night",
        "form_h": "Request your dates",
        "name": "Full name", "email": "Email", "phone": "Phone or WhatsApp", "message": "Anything we should know?",
        "message_ph": "Arrival time, children's ages, occasion…",
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
        "price_on_req": "Tarif sur demande",
        "price_from": lambda p: f"À partir de <strong>{p} €</strong> la nuit",
        "form_h": "Demandez vos dates",
        "name": "Nom complet", "email": "E-mail", "phone": "Téléphone ou WhatsApp", "message": "Quelque chose à nous dire ?",
        "message_ph": "Heure d'arrivée, âge des enfants, occasion…",
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
                    "Yes: 3 nights in low season, 5 nights in high season and 7 nights over Christmas and New Year." if en else "Oui : 3 nuits en basse saison, 5 nuits en haute saison et 7 nuits pour Noël et le Nouvel An."))
    if getattr(cfg, "SEASONS", None):
        rows = ("; " if en else " ; ").join(
            (f"{s[0].lower()} ({s[2][0].lower() + s[2][1:] if not s[2].startswith(('May','December','Christmas')) else s[2]}): €{s[4]} per night, minimum {s[5]} nights" if en
             else f"{s[1].lower()} ({s[3][0].lower() + s[3][1:] if not s[3].startswith('Noël') else s[3]}), {s[4]} € la nuit et {s[5]} nuits minimum") for s in cfg.SEASONS)
        out.append(("How much does the villa cost per night?" if en else "Quel est le prix de la villa par nuit ?",
                    (f"Our direct rates are: {rows}." if en else f"Nos tarifs en direct : {rows}.")
                    + ((f" A cleaning fee of €{cfg.CLEANING_FEE_EUR} applies once per stay." if en
                        else f" Des frais de ménage de {cfg.CLEANING_FEE_EUR} € s'ajoutent une fois par séjour.") if cfg.CLEANING_FEE_EUR else "")))
    if cfg.DEPOSIT_EUR:
        out.append(("Is there a security deposit?" if en else "Y a-t-il une caution ?",
                    f"Yes, €{cfg.DEPOSIT_EUR}. It is a hold on your card, not a charge, and it is released after your stay if nothing is damaged." if en
                    else f"Oui, {cfg.DEPOSIT_EUR} €. C'est une empreinte bancaire, pas un débit : elle est levée après le séjour si rien n'est endommagé."))
    out.append(("Is the villa cleaned during my stay?" if en else "Le ménage est-il fait pendant le séjour ?",
                "Yes, weekly housekeeping is included in the stay." if en else "Oui, un ménage hebdomadaire est inclus dans le séjour."))
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
        "img": 2,
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
        "img": 6,
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
        "img": 5,
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
}
