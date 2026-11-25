# Kurnia Tour & Travel: website concept

Design concepts by KL Tech. Not the official Kurnia website and not a live shop.

- `/` Kurnia site, Arah 3 (People First): BM at the root, ID under `/id/`, EN under `/en/`
- `/safar-gifts/` Safar Gifts by Kurnia, Umrah and Hajj gift-pack shop prototype: EN at the root, Arabic (RTL) under `/safar-gifts/ar/`
- Safar Gifts products and prices live in `safar-gifts/catalogue.json` (source copy in `_src/`). Edit it, then rerun `_src/safar-gen.py`.
- Static HTML, CSS and a small JS cart. Hidden from search engines; forms and WhatsApp buttons do not contact anyone.
