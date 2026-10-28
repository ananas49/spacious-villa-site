# Spacious Villa – site de réservation directe

Site statique bilingue (EN à la racine, FR sous /fr/) pour la villa de Cul-de-Sac, Saint-Martin.

- `config.py` : tarifs, horaires, contact, mentions légales, URL du widget Smoobu
- `content.py` : tous les textes EN/FR, la FAQ et les guides
- `static/` : styles, script ; `static/img/` : photos de la villa
- `python3 build.py` génère le site dans `dist/` (c'est ce que fait Netlify à chaque mise à jour)
