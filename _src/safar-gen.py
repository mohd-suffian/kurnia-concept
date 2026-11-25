import json, os, html
OUT = '/home/claude/safar/build'
CAT = json.load(open('/home/claude/safar/catalogue.json'))
P = CAT['products']
L = 'en'
CUR = ''
def t(en, ar): return en if L == 'en' else ar
SLUG = {'home': '', 'shop': 'shop', 'build': 'build-your-pack', 'bulk': 'bulk-orders', 'how': 'how-it-works', 'faq': 'faq', 'cart': 'cart'}
for p in P: SLUG['p-' + p['id']] = 'shop/' + p['id']
def path_of(key, lang): s = SLUG[key]; pre = '' if lang == 'en' else 'ar/'; p = (pre + s).strip('/'); return (p + '/') if p else ''
def rel(x): return '../' * CUR.count('/') + x
def u(key, lang=None): return rel(path_of(key, lang or L)) or './'
def a(x): return rel('assets/' + x)
ITEMS = lambda: {'zamzam': t('Zamzam*', 'زمزم*'), 'dates': t('Dates', 'تمر'), 'sweets': t('Sweets', 'حلويات'), 'tasbih': t('Tasbih', 'مسبحة'), 'dua': t('Dua card', 'بطاقة دعاء')}
TICK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1F4D3A" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
CROSS = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#A39E91" stroke-width="2.5" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
BAG = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F4D3A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 7h12l1 13H5z"/><path d="M9 7a3 3 0 0 1 6 0"/></svg>'
WAI = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-13.5 7.8L3 21l1.2-4.5A9 9 0 1 1 21 12z"/></svg>'
def nm(p): return p['name'][L]
def dims(p): return ' × '.join(str(x).rstrip('0').rstrip('.') if isinstance(x, float) else str(x) for x in p['size']) + ' cm'

def strings():
    return {'added': t('Added to cart', 'أضيف إلى السلة'), 'total': t('Total', 'الإجمالي'), 'sticker': t('personalised sticker', 'ملصق مخصص'),
      'waHello': t('Assalamualaikum Safar Gifts, I would like to order:', 'السلام عليكم سفر للهدايا، أود طلب:'), 'recommended': t('Recommended for you', 'نوصي لك'),
      'overBudget': t('No pack has all those items within this budget. The lowest price with them is {p} per gift.', 'لا توجد باقة بكل هذه العناصر ضمن الميزانية. أقل سعر لها {p} للهدية.'),
      'colour': t('Colour', 'اللون'), 'empty': t('Your cart is empty.', 'سلتك فارغة.'), 'shop': t('Shop gift packs', 'تسوق الباقات'), 'units': t('Units', 'الوحدات'),
      'remove': t('Remove', 'إزالة'), 'delivery': t('Delivery', 'التوصيل'), 'date': t('Date needed', 'التاريخ المطلوب'), 'name': t('Name', 'الاسم'), 'phone': t('Phone', 'الهاتف'),
      'bulkHello': t('Assalamualaikum Safar Gifts, bulk enquiry:', 'السلام عليكم سفر للهدايا، استفسار عن طلب بالجملة:'), 'org': t('Organisation', 'الجهة'),
      'tier': t('Tier', 'الفئة'), 'branding': t('Custom branding', 'علامة تجارية مخصصة'), 'yes': t('Yes', 'نعم'), 'no': t('No', 'لا')}

def head(key, title, desc):
    alt = ''.join(f'<link rel="alternate" hreflang="{lg}" href="{u(key, lg)}">' for lg in ('en', 'ar'))
    pj = json.dumps({'currency': CAT['currency'], 'stickerPerUnit': CAT['stickerPerUnit'], 'customRange': CAT['customRange'], 'products': P}, ensure_ascii=False)
    return f'''<!doctype html><html lang="{L}" dir="{'rtl' if L == 'ar' else 'ltr'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<title>{title} | Safar Gifts</title><meta name="description" content="{html.escape(desc)}">{alt}<link rel="icon" href="{a('safar-icon.svg')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700&family=Inter:wght@400;500;600;700;800&family=Lora:ital@1&family=Amiri:wght@400;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a('safar.css')}"><script>window.CAT={pj};window.T={json.dumps(strings(), ensure_ascii=False)};window.LANG="{L}";window.ASSETS="{a('')}";window.SHOP="{u('shop')}";</script></head><body>'''

def nav():
    return [('shop', t('Shop', 'المتجر')), ('build', t('Build Your Pack', 'صمّم باقتك')), ('bulk', t('Bulk & Agencies', 'الجملة والوكالات')), ('how', t('How It Works', 'كيف نعمل')), ('faq', t('FAQ', 'الأسئلة الشائعة'))]

def header(key):
    other = 'ar' if L == 'en' else 'en'
    on = lambda k: 'on' if k == key or (k == 'shop' and key.startswith('p-')) else ''
    links = ''.join(f'<a class="{on(k)}" href="{u(k)}">{n}</a>' for k, n in nav())
    return f'''<div class="concept">{t('Concept prototype by KL Tech for Safar Gifts by Kurnia. Not a live shop: no orders are taken and no payment is collected.', 'نموذج تجريبي من KL Tech لـ سفر للهدايا من كورنيا. ليس متجرًا فعليًا: لا تُستلم طلبات ولا تُحصّل مدفوعات.')}</div>
<div class="top"><div class="wrap"><span>{t('Easy to carry · Ready to gift · Packs of 10 and 20', 'سهلة الحمل · جاهزة للإهداء · عبوات من 10 و20')}</span><span style="display:flex;gap:18px"><a href="{rel('../')}">{t('Umrah packages by Kurnia', 'باقات العمرة من كورنيا')} →</a><a href="{u(key, other)}" lang="{other}">{'العربية' if L == 'en' else 'English'}</a></span></div></div>
<header class="hdr"><div class="wrap"><a class="brand" href="{u('home')}"><img src="{a('safar-logo.svg')}" alt="Safar Gifts by Kurnia Tour and Travel" width="230" height="62"></a>
<nav class="nav" aria-label="{t('Main', 'الرئيسية')}">{links}</nav>
<div class="row" style="gap:8px"><a class="cartlink" href="{u('cart')}" aria-label="{t('Cart', 'السلة')}">{BAG}<b data-count style="display:none">0</b></a>
<details class="menu"><summary aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F4D3A" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary><div class="panel">{''.join(f'<a href="{u(k)}">{n}</a>' for k, n in nav())}</div></details></div>
</div></header><main>'''

def footer():
    return f'''</main><footer class="ftr"><div class="wrap"><div class="cols">
<div><img src="{a('safar-logo-reverse.svg')}" alt="Safar Gifts by Kurnia Tour and Travel" style="height:58px;width:auto;margin-bottom:10px"><p style="font-family:Lora,serif;font-style:italic;color:#F3E6C8;margin-bottom:6px">Buah Tangan dari Tanah Suci</p><p>{t('Gift packs for pilgrims, by the team behind Kurnia Tour & Travel.', 'هدايا للحجاج والمعتمرين، من فريق كورنيا للسفر والسياحة.')}</p></div>
<div><b>{t('Shop', 'المتجر')}</b>{''.join(f'<a href="{u("p-" + p["id"])}">{CAT["currency"]} {p["price"]} · {nm(p)}</a>' for p in P)}</div>
<div><b>{t('Help', 'المساعدة')}</b><a href="{u('how')}">{t('How it works', 'كيف نعمل')}</a><a href="{u('faq')}">{t('FAQ', 'الأسئلة الشائعة')}</a><a href="{u('bulk')}">{t('Bulk and agency orders', 'طلبات الجملة والوكالات')}</a></div>
<div><b>Kurnia Tour &amp; Travel</b><a href="{rel('../')}">{t('Kurnia Umrah packages', 'باقات العمرة من كورنيا')}</a><a href="{rel('../hadiah-umrah/')}">{t('Safar Gifts on the Kurnia site', 'سفر للهدايا على موقع كورنيا')}</a><span>Makkah · Madinah · Melaka · Cianjur</span></div><div><b>{t('Scan to share', 'امسح للمشاركة')}</b><img src="{a('safar-gifts-qr.png')}" alt="{t('QR code to this shop', 'رمز QR لهذا المتجر')}" style="width:120px;height:120px;border-radius:10px;margin-top:4px"></div>
</div><div class="base"><span>{t('All contents and prices are initial concepts, subject to availability and compliance.', 'جميع المحتويات والأسعار مبدئية، وتخضع للتوفر والامتثال للأنظمة.')}</span><span>{t('Concept by KL Tech', 'تصميم مبدئي من KL Tech')}</span></div></div></footer><div class="toast" role="status"></div><script src="{a('safar.js')}"></script></body></html>'''

def checks(p):
    allitems = ['zamzam', 'dates', 'sweets', 'tasbih', 'dua']
    return '<ul class="checks">' + ''.join(f'<li class="{"" if i in p["items"] else "no"}">{TICK if i in p["items"] else CROSS}<span>{ITEMS()[i]}</span></li>' for i in allitems) + '</ul>'

def tier_card(p, packprice=False):
    bc = 'bur' if p['colour'] == 'burgundy' else ''
    pr = f'<span class="muted" style="font-size:13px">{t("Pack of", "عبوة")} <span data-qtylabel>10</span></span><b data-packprice="{p["price"]}">{CAT["currency"]} {p["price"]*10}</b>' if packprice else f'<span class="muted" style="font-size:13px">{t("per gift", "للهدية")}</span><b>{CAT["currency"]} {p["price"]}</b>'
    return f'''<a class="tier" href="{u('p-' + p['id'])}" data-card data-price="{p['price']}" data-items="{' '.join(p['items'])}"><span class="badge {bc}">{CAT['currency']} {p['price']}</span><div class="img"><img src="{a(p['img'])}" alt="{nm(p)}" loading="lazy"></div><div class="body"><h3>{nm(p)}</h3>{checks(p)}<div class="meta"><span class="chip">{dims(p)}</span><span class="chip">~{p['weightG']} g</span></div><p class="muted" style="font-size:13px">{p['packaging'][L]}</p><div class="price">{pr}</div></div></a>'''

def steps():
    s = [(t('Choose a gift tier', 'اختر فئة الهدية'), t('SAR 3, 5, 10 or 20 per gift.', '3 أو 5 أو 10 أو 20 ريالًا للهدية.')), (t('Select recipients', 'حدد عدد المستلمين'), t('Packs of 10 or 20, or 50 to 1,000 for groups.', 'عبوات من 10 أو 20، أو 50 إلى 1000 للمجموعات.')),
         (t('Add personalisation', 'أضف لمستك'), t('A sticker with your name or a short message.', 'ملصق باسمك أو رسالة قصيرة.')), (t('Delivery or collection', 'التوصيل أو الاستلام'), t('Hotel drop-off in Makkah or Madinah, or collect.', 'توصيل للفندق في مكة أو المدينة، أو استلام.')),
         (t('Receive ready-to-gift packs', 'استلم هدايا جاهزة'), t('Sealed, labelled and ready to hand out at home.', 'مختومة وموسومة وجاهزة للتوزيع.'))]
    return '<div class="steps">' + ''.join(f'<div><b>{h}</b><p>{b}</p></div>' for h, b in s) + '</div>'

def compliance():
    return f'<p class="note">{t("*Zamzam is subject to regulatory feasibility. Saudi rules on Zamzam bottling, resale, labelling and transport are being verified. All food is individually sealed and labelled with its expiry date. Final contents depend on availability and compliance.", "*زمزم مشروط بإمكانية الامتثال للأنظمة. يجري التحقق من الأنظمة السعودية الخاصة بتعبئة زمزم وبيعه ووسمه ونقله. جميع الأطعمة مختومة بشكل فردي وموسومة بتاريخ الانتهاء. المحتويات النهائية تعتمد على التوفر والامتثال.")}</p>'

def p_home():
    tiers = ''.join(tier_card(p) for p in P)
    body = f'''<section class="hero"><div class="wrap"><div style="display:flex;flex-direction:column;gap:18px">
<span class="eyebrow">{t('Umrah & Hajj gift packs', 'هدايا العمرة والحج')}</span>
<h1>{t('Meaningful Gifts from Your Sacred Journey', 'هدايا ذات معنى من رحلتك المباركة')}</h1>
<p class="tag-line">Buah Tangan dari Tanah Suci</p><p class="muted" style="font-weight:600;margin-top:-10px">{t('Easy to carry · Ready to gift', 'سهلة الحمل · جاهزة للإهداء')}</p>
<p class="lead">{t('Compact packs of Zamzam, dates and sweets, sealed and boxed for the people waiting at home. Order in tens or twenties, before, during or after your journey, and collect at your hotel.', 'عبوات صغيرة من زمزم والتمر والحلويات، مختومة ومغلفة لأحبتك في الوطن. اطلب بالعشرات أو العشرينات، قبل رحلتك أو أثناءها أو بعدها، واستلمها في فندقك.')}</p>
<div class="row"><a class="btn btn-em" href="{u('shop')}">{t('Shop Gift Packs', 'تسوق الباقات')}</a><a class="btn btn-line" href="{u('build')}">{t('Build Your Pack', 'صمّم باقتك')}</a></div>
<div class="ticks"><span>✓ {t('From SAR 3 per gift', 'من 3 ريالات للهدية')}</span><span>✓ {t('Fits in hand luggage', 'تناسب حقيبة اليد')}</span><span>✓ {t('Hotel drop-off', 'التوصيل للفندق')}</span></div>
</div><div class="pic"><img src="{a('hero.jpg')}" alt="{t('Safar gift packs in four tiers', 'باقات سفر للهدايا بأربع فئات')}"></div></div></section>
<section class="pat"><div class="wrap"><div class="sec-head"><span class="eyebrow">{t('Four tiers', 'أربع فئات')}</span><h2>{t('A gift for every budget', 'هدية لكل ميزانية')}</h2><div class="rule">✦</div></div><div class="grid g4">{tiers}</div><div style="margin-top:20px">{compliance()}</div></div></section>
<section><div class="wrap"><div class="sec-head"><span class="eyebrow">{t('Practical quantities', 'كميات عملية')}</span><h2>{t('Pack of 10 or Pack of 20', 'عبوة 10 أو عبوة 20')}</h2><p class="muted">{t('Each carry box holds individually wrapped gifts, so you can hand them out straight from your luggage.', 'كل صندوق يحوي هدايا مغلفة فرديًا، لتوزعها مباشرة من حقيبتك.')}</p></div>
<div class="packs"><div class="pack"><img src="{a('pack10.jpg')}" alt=""><div><h3>{t('Pack of 10', 'عبوة 10')}</h3><p class="muted">{t('For close family and friends. From SAR 30.', 'للأهل والأصدقاء المقربين. من 30 ريالًا.')}</p></div></div><div class="pack"><img src="{a('pack20.jpg')}" alt=""><div><h3>{t('Pack of 20', 'عبوة 20')}</h3><p class="muted">{t('For colleagues and the wider family. From SAR 60.', 'للزملاء والعائلة الممتدة. من 60 ريالًا.')}</p></div></div></div></div></section>
<section class="pat"><div class="wrap"><div class="sec-head"><span class="eyebrow">{t('How it works', 'كيف نعمل')}</span><h2>{t('Five simple steps', 'خمس خطوات بسيطة')}</h2></div>{steps()}</div></section>
<section><div class="wrap grid g2" style="align-items:center"><div style="display:flex;flex-direction:column;gap:14px"><span class="eyebrow">{t('For agencies, mutawwif and hotels', 'للوكالات والمطوفين والفنادق')}</span><h2 style="font-size:32px">{t('Gifts for a whole group, with your name on them', 'هدايا لمجموعة كاملة، باسمكم')}</h2><p class="muted">{t('Orders from 50 to 1,000 units, custom stickers or sleeves, and delivery to your group’s hotel.', 'طلبات من 50 إلى 1000 وحدة، ملصقات أو أغلفة مخصصة، وتوصيل إلى فندق مجموعتكم.')}</p><div class="row"><a class="btn btn-em" href="{u('bulk')}">{t('Bulk enquiry', 'استفسار الجملة')}</a></div></div><div class="pic" style="border-radius:22px;overflow:hidden"><img src="{a('pack20.jpg')}" alt=""></div></div></section>'''
    return t('Umrah & Hajj Gift Packs', 'هدايا العمرة والحج'), t('Affordable, travel-friendly gift packs for pilgrims.', 'هدايا ميسورة وسهلة الحمل للحجاج والمعتمرين.'), body

def phero(title, lead): return f'<div class="phero pat"><div class="wrap"><h1>{title}</h1><p>{lead}</p></div></div>'

def p_shop():
    pr = ''.join(f'<label class="opt"><input type="checkbox" name="price" value="{p["price"]}"> {CAT["currency"]} {p["price"]}</label>' for p in P)
    it = ''.join(f'<label class="opt"><input type="checkbox" name="item" value="{k}"> {v}</label>' for k, v in ITEMS().items())
    qt = ''.join(f'<label class="opt"><input type="radio" name="qty" value="{q}" {"checked" if q == 10 else ""}> {t("Pack of", "عبوة")} {q}</label>' for q in CAT['packSizes'])
    body = phero(t('Shop Gift Packs', 'تسوق الباقات'), t('Every pack shows its contents, box size and weight, so you know exactly what fits in your luggage.', 'كل باقة توضح محتوياتها ومقاس العلبة ووزنها، لتعرف ما يناسب حقيبتك.')) + f'''<section style="padding-top:32px"><div class="wrap shop">
<form class="filters" data-filters onsubmit="return false"><fieldset><legend>{t('Price per gift', 'السعر للهدية')}</legend>{pr}</fieldset><fieldset><legend>{t('Quantity', 'الكمية')}</legend>{qt}</fieldset><fieldset><legend>{t('Must include', 'يجب أن تشمل')}</legend>{it}</fieldset><button class="btn btn-line" type="reset">{t('Clear filters', 'مسح الفلاتر')}</button></form>
<div><p class="muted" style="margin-bottom:14px"><span data-shown>4</span> {t('packs', 'باقات')}</p><div class="grid g2">{''.join(tier_card(p, True) for p in P)}</div><div style="margin-top:20px">{compliance()}</div></div></div></section>'''
    return t('Shop', 'المتجر'), '', body

def p_product(p):
    vol = p['size'][0] * p['size'][1] * p['size'][2]
    others = [x for x in P if x['id'] != p['id']][:3]
    body = f'''<section style="padding-top:28px"><div class="wrap"><p class="muted" style="font-size:13px;margin-bottom:16px"><a href="{u('shop')}">{t('Shop', 'المتجر')}</a> / {nm(p)}</p>
<div class="pd" data-product="{p['id']}"><div class="gallery"><div class="main"><img src="{a(p['img'])}" alt="{nm(p)}"></div><div class="thumbs"><button type="button" class="on" aria-label="1"><img src="{a(p['img'])}" alt=""></button><button type="button" aria-label="2"><img src="{a(p['box'])}" alt=""></button><button type="button" aria-label="3"><img src="{a('pack10.jpg')}" alt=""></button></div>
<div class="panel"><h2 style="font-size:22px">{t('Included items', 'المحتويات')}</h2><ul class="checks" style="font-size:16px">{''.join(f'<li>{TICK}<span>{c}</span></li>' for c in p['contents'][L])}</ul>
<div class="facts"><div>{t('Box size', 'مقاس العلبة')}<b>{dims(p)}</b></div><div>{t('Est. weight per gift', 'الوزن التقديري للهدية')}<b>~{p['weightG']} g</b></div><div>{t('Packaging', 'التغليف')}<b>{p['packaging'][L]}</b></div><div>{t('Shelf life', 'الصلاحية')}<b>[{t('Expiry printed on each item', 'التاريخ مطبوع على كل عنصر')}]</b></div></div>{compliance()}</div></div>
<div class="panel" style="position:sticky;top:84px"><span class="badge {'bur' if p['colour'] == 'burgundy' else ''}" style="position:static;align-self:flex-start">{CAT['currency']} {p['price']}</span><h1 style="font-size:34px">{nm(p)}</h1><p class="muted">{p['blurb'][L]}</p>
<div><span class="eyebrow">{t('Quantity', 'الكمية')}</span><div class="seg" style="margin-top:8px"><label><input type="radio" name="mode" value="10" checked>{t('Pack of 10', 'عبوة 10')}<small>{CAT['currency']} {p['price']*10}</small></label><label><input type="radio" name="mode" value="20">{t('Pack of 20', 'عبوة 20')}<small>{CAT['currency']} {p['price']*20}</small></label><label><input type="radio" name="mode" value="custom">{t('Custom', 'مخصص')}<small>50 to 1,000</small></label></div></div>
<div class="row" data-packs-row><span>{t('Number of packs', 'عدد العبوات')}</span><div class="stepper"><button type="button" data-step="-1" aria-label="-1">−</button><input name="packs" value="1" inputmode="numeric" aria-label="{t('Number of packs', 'عدد العبوات')}"><button type="button" data-step="1" aria-label="+1">+</button></div></div>
<label class="f" data-custom-row style="display:none">{t('Units (50 to 1,000)', 'الوحدات (50 إلى 1000)')}<input name="custom" type="number" min="50" max="1000" value="100"></label>
<label class="opt"><input type="checkbox" name="sticker"> {t('Personalised sticker', 'ملصق مخصص')} (+{CAT['currency']} {CAT['stickerPerUnit']} {t('each, sample price', 'للقطعة، سعر تجريبي')})</label>
<label class="f" data-sticker-row style="display:none">{t('Sticker text: your name, family, company or a short message', 'نص الملصق: اسمك أو العائلة أو الشركة أو رسالة قصيرة')}<input name="stickerText" maxlength="40" placeholder="{t('From Makkah with Du’a', 'من مكة مع الدعاء')}"></label>
<div class="facts"><div>{t('Gifts', 'الهدايا')}<b data-units>10</b></div><div>{t('Luggage weight', 'وزن الأمتعة')}<b data-weight>-</b></div><div>{t('Luggage space', 'المساحة في الحقيبة')}<b data-volume>-</b></div><div>{t('Per gift volume', 'حجم الهدية')}<b>{vol:g} cm³</b></div></div>
<div class="total"><div><small>{t('Estimated total', 'الإجمالي التقديري')}</small>{t('Total', 'الإجمالي')}</div><b data-total>-</b></div>
<div class="row"><button type="button" class="btn btn-em" data-add style="flex:1">{t('Add to cart', 'أضف إلى السلة')}</button><button type="button" class="btn btn-wa" data-wa style="flex:1">{WAI} {t('Order on WhatsApp', 'اطلب عبر واتساب')}</button></div>
<div class="wa-preview" aria-live="polite"></div><a class="btn btn-wa" target="_blank" rel="noopener" style="display:none">{t('Open in WhatsApp', 'افتح في واتساب')}</a>
</div></div></div></section>
<section class="pat"><div class="wrap"><div class="sec-head"><h2>{t('Other tiers', 'فئات أخرى')}</h2></div><div class="grid g3">{''.join(tier_card(x) for x in others)}</div></div></section>'''
    return nm(p), p['blurb'][L], body

def p_build():
    budgets = ''.join(f'<option value="{p["price"]}" {"selected" if p["price"] == 10 else ""}>{CAT["currency"]} {p["price"]}</option>' for p in P)
    imgk = {'zamzam': 'zamzam', 'dates': 'dates', 'sweets': 'sweets', 'tasbih': 'tasbih', 'dua': 'dua-card'}
    items = ''.join(f'<label class="opt item"><input type="checkbox" name="bitem" value="{k}" {"checked" if k in ("zamzam", "dates") else ""}><img src="{a("item-" + imgk[k] + ".png")}" alt="" loading="lazy">{v}</label>' for k, v in ITEMS().items())
    cols = [('ivory', t('Ivory', 'عاجي')), ('sand', t('Sand', 'رملي')), ('emerald', t('Emerald', 'زمردي')), ('burgundy', t('Burgundy', 'عنابي'))]
    colhtml = ''.join(f'<label><input type="radio" name="colour" value="{k}" {"checked" if k == "emerald" else ""}>{n}</label>' for k, n in cols)
    locs = [t('Hotel drop-off, Makkah', 'توصيل للفندق، مكة'), t('Hotel drop-off, Madinah', 'توصيل للفندق، المدينة'), t('Collect from our counter', 'الاستلام من نقطة البيع'), t('Deliver before departure (home country)', 'التوصيل قبل السفر (بلدك)')]
    body = phero(t('Build Your Pack', 'صمّم باقتك'), t('Tell us your budget and what each gift should hold. We match you to the right pack and work out the total.', 'أخبرنا بميزانيتك وما تريد في كل هدية، ونختار لك الباقة المناسبة ونحسب الإجمالي.')) + f'''<section style="padding-top:28px"><div class="wrap cartgrid" data-build><form class="panel" onsubmit="return false">
<div class="grid g2"><label class="f">{t('Budget per gift', 'الميزانية للهدية')}<select name="budget">{budgets}</select></label><label class="f">{t('Number of recipients', 'عدد المستلمين')}<input name="recipients" type="number" min="1" max="1000" value="20"></label></div>
<fieldset style="border:0;padding:0;margin:0"><legend class="eyebrow" style="margin-bottom:8px">{t('Each gift includes', 'تشمل كل هدية')}</legend><div class="itemgrid">{items}</div></fieldset>
<div><span class="eyebrow">{t('Packaging colour', 'لون التغليف')}</span><div class="seg" style="grid-template-columns:repeat(4,1fr);margin-top:8px">{colhtml}</div></div>
<label class="opt"><input type="checkbox" name="bsticker"> {t('Personalised sticker', 'ملصق مخصص')}</label><label class="f">{t('Sticker text', 'نص الملصق')}<input name="bstickerText" maxlength="40" placeholder="{t('From Makkah with Du’a', 'من مكة مع الدعاء')}"></label>
<label class="f">{t('Delivery or collection', 'التوصيل أو الاستلام')}<select name="location">{''.join(f'<option>{x}</option>' for x in locs)}</select></label>
</form><div class="panel" style="position:sticky;top:84px"><h2 style="font-size:22px">{t('Your pack', 'باقتك')}</h2><div data-result style="display:flex;flex-direction:column;gap:14px"></div><button type="button" class="btn btn-em" data-badd>{t('Add to cart', 'أضف إلى السلة')}</button><a class="btn btn-line" href="{u('cart')}">{t('View cart', 'عرض السلة')}</a>{compliance()}</div></div></section>'''
    return t('Build Your Pack', 'صمّم باقتك'), '', body

def p_bulk():
    tiers = ''.join(f'<option>{CAT["currency"]} {p["price"]} · {nm(p)}</option>' for p in P) + f'<option>{t("Not sure yet", "لم أقرر بعد")}</option>'
    pts = [(t('50 to 1,000 units', 'من 50 إلى 1000 وحدة'), t('Tiered pricing for larger runs. [Rates to confirm]', 'أسعار متدرجة للكميات الكبيرة. [الأسعار قيد التأكيد]')), (t('Custom branding', 'علامة مخصصة'), t('Your agency name on stickers or sleeves.', 'اسم وكالتكم على الملصقات أو الأغلفة.')), (t('Group hotel delivery', 'التوصيل لفندق المجموعة'), t('Delivered to your group in Makkah or Madinah.', 'نوصلها لمجموعتكم في مكة أو المدينة.')), (t('Agency partnership', 'شراكة الوكالات'), t('Add a gift pack to every package you sell. [Terms to confirm]', 'أضيفوا هدية لكل باقة تبيعونها. [الشروط قيد التأكيد]'))]
    body = phero(t('Bulk and Travel Agency Orders', 'طلبات الجملة والوكالات'), t('For Umrah and Hajj agencies, mutawwif, hotels, companies and community groups.', 'لوكالات العمرة والحج والمطوفين والفنادق والشركات والمجموعات.')) + f'''<section style="padding-top:28px"><div class="wrap cartgrid"><div class="grid g2">{''.join(f'<div class="panel"><h3 style="font-size:19px">{h}</h3><p class="muted">{b}</p></div>' for h, b in pts)}</div>
<form class="panel" data-bulk onsubmit="return false"><h2 style="font-size:22px">{t('Wholesale enquiry', 'استفسار الجملة')}</h2><label class="f">{t('Organisation', 'الجهة')}<input name="org" required></label><div class="grid g2"><label class="f">{t('Contact name', 'اسم المسؤول')}<input name="name" required></label><label class="f">{t('Phone / WhatsApp', 'الهاتف / واتساب')}<input name="phone" type="tel" required></label></div>
<div class="grid g2"><label class="f">{t('Units', 'الوحدات')}<input name="units" type="number" min="50" max="1000" value="200" required></label><label class="f">{t('Tier', 'الفئة')}<select name="tier">{tiers}</select></label></div><label class="opt"><input type="checkbox" name="branding"> {t('Custom branding', 'علامة مخصصة')}</label><label class="f">{t('Date needed', 'التاريخ المطلوب')}<input name="date" type="date"></label><label class="f">{t('Message', 'رسالة')}<textarea name="msg"></textarea></label>
<button type="button" class="btn btn-wa" data-bwa>{WAI} {t('Send enquiry on WhatsApp', 'أرسل الاستفسار عبر واتساب')}</button><div class="wa-preview" aria-live="polite"></div><a class="btn btn-wa" target="_blank" rel="noopener" style="display:none">{t('Open in WhatsApp', 'افتح في واتساب')}</a></form></div></section>'''
    return t('Bulk Orders', 'طلبات الجملة'), '', body

def p_how():
    body = phero(t('How It Works', 'كيف نعمل'), t('From choosing a tier to handing out gifts at home.', 'من اختيار الفئة إلى توزيع الهدايا في الوطن.')) + f'<section><div class="wrap">{steps()}<div class="row" style="justify-content:center;margin-top:28px"><a class="btn btn-em" href="{u("shop")}">{t("Shop Gift Packs", "تسوق الباقات")}</a><a class="btn btn-line" href="{u("build")}">{t("Build Your Pack", "صمّم باقتك")}</a></div></div></section>'
    return t('How It Works', 'كيف نعمل'), '', body

def p_faq():
    q = [(t('How long does the food last?', 'ما مدة صلاحية الطعام؟'), t('Every item is individually sealed and labelled with its expiry date. [Typical shelf life to confirm per supplier.]', 'كل عنصر مختوم بشكل فردي وعليه تاريخ الانتهاء. [مدة الصلاحية المعتادة قيد التأكيد حسب المورد.]')),
         (t('How is the Zamzam packed?', 'كيف تُعبأ زمزم؟'), t('In small sealed bottles, subject to regulatory feasibility. Saudi rules on Zamzam bottling, resale, labelling and transport are being verified before launch.', 'في عبوات صغيرة مختومة، بشرط إمكانية الامتثال. يجري التحقق من الأنظمة السعودية الخاصة بتعبئة زمزم وبيعها ووسمها ونقلها قبل الإطلاق.')),
         (t('Will it fit in my luggage?', 'هل تناسب حقيبتي؟'), t('Each product page shows box size, weight and the total space for your quantity. A Pack of 20 SAR 3 gifts takes about 2.9 litres.', 'كل صفحة منتج تعرض مقاس العلبة والوزن والمساحة الإجمالية لكميتك. عبوة 20 من فئة 3 ريالات تحتاج نحو 2.9 لتر.')),
         (t('Can I take them on an international flight?', 'هل يمكنني حملها في رحلة دولية؟'), t('Packs are designed for checked luggage. Airline and customs rules on liquids and food vary: check with your airline. [Guidance to confirm.]', 'الباقات مصممة للأمتعة المشحونة. تختلف قواعد شركات الطيران والجمارك بشأن السوائل والطعام: راجع شركة الطيران. [الإرشادات قيد التأكيد.]')),
         (t('Can I order a custom pack?', 'هل يمكنني طلب باقة مخصصة؟'), t('Yes. Use Build Your Pack, or the bulk form for 50 to 1,000 units.', 'نعم. استخدم صمّم باقتك، أو نموذج الجملة لـ 50 إلى 1000 وحدة.')),
         (t('Do you deliver in Makkah and Madinah?', 'هل توصلون في مكة والمدينة؟'), t('Hotel drop-off in both cities is planned, plus collection. [Areas and fees to confirm.]', 'التوصيل للفنادق في المدينتين مخطط، مع خيار الاستلام. [المناطق والرسوم قيد التأكيد.]')),
         (t('How much notice do you need?', 'كم من الوقت تحتاجون؟'), t('[Lead time to confirm.] Order before you travel for the widest choice.', '[مدة التجهيز قيد التأكيد.] اطلب قبل السفر لأوسع خيارات.'))]
    body = phero(t('Frequently Asked Questions', 'الأسئلة الشائعة'), '') + '<section style="padding-top:20px"><div class="wrap" style="max-width:820px;display:flex;flex-direction:column;gap:10px">' + ''.join(f'<details class="faq"><summary>{a_}</summary><p>{b}</p></details>' for a_, b in q) + '</div></section>'
    return t('FAQ', 'الأسئلة الشائعة'), '', body

def p_cart():
    dl = [t('Hotel drop-off, Makkah', 'توصيل للفندق، مكة'), t('Hotel drop-off, Madinah', 'توصيل للفندق، المدينة'), t('Collect from our counter', 'الاستلام من نقطة البيع'), t('Delivery to an address', 'التوصيل إلى عنوان')]
    body = phero(t('Your Cart', 'سلتك'), t('Prices in Saudi Riyal. Orders are confirmed on WhatsApp.', 'الأسعار بالريال السعودي. تُؤكد الطلبات عبر واتساب.')) + f'''<section style="padding-top:20px" data-cart><div class="wrap cartgrid"><div data-lines style="display:flex;flex-direction:column;gap:12px"></div>
<div class="panel"><h2 style="font-size:22px">{t('Checkout', 'إتمام الطلب')}</h2><div class="sum"><span>{t('Subtotal', 'المجموع الفرعي')}</span><span data-sub>-</span></div><div class="sum"><span>{t('Delivery', 'التوصيل')}</span><span>[{t('to confirm', 'قيد التأكيد')}]</span></div><div class="sum big"><span>{t('Total', 'الإجمالي')}</span><span data-grand>-</span></div>
<form onsubmit="return false"><label class="f">{t('Delivery or collection', 'التوصيل أو الاستلام')}<select name="delivery">{''.join(f'<option>{x}</option>' for x in dl)}</select></label><label class="f">{t('Hotel or address', 'الفندق أو العنوان')}<input name="place"></label><label class="f">{t('Date needed', 'التاريخ المطلوب')}<input name="date" type="date"></label><div class="grid g2"><label class="f">{t('Name', 'الاسم')}<input name="name" required></label><label class="f">{t('Phone / WhatsApp', 'الهاتف / واتساب')}<input name="phone" type="tel" required></label></div></form>
<button type="button" class="btn btn-wa" data-checkout>{WAI} {t('Place order on WhatsApp', 'أرسل الطلب عبر واتساب')}</button><button type="button" class="btn btn-line" disabled>{t('Pay online (coming soon)', 'الدفع الإلكتروني (قريبًا)')}</button><div class="wa-preview" aria-live="polite"></div><a class="btn btn-wa" target="_blank" rel="noopener" style="display:none">{t('Open in WhatsApp', 'افتح في واتساب')}</a></div></div></section>'''
    return t('Cart', 'السلة'), '', body

PAGES = {'home': p_home, 'shop': p_shop, 'build': p_build, 'bulk': p_bulk, 'how': p_how, 'faq': p_faq, 'cart': p_cart}
for pp in P: PAGES['p-' + pp['id']] = (lambda x: (lambda: p_product(x)))(pp)
n = 0
for lang in ('en', 'ar'):
    L = lang
    for key, fn in PAGES.items():
        CUR = path_of(key, lang)
        title, desc, body = fn()
        d = os.path.join(OUT, CUR); os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(head(key, title, desc or title) + header(key) + body + footer()); n += 1
print('pages', n)
