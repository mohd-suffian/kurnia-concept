import os, html
OUT = '/home/claude/kurnia-site/build'
LANGS = ['bm', 'id', 'en']
PREFIX = {'bm': '', 'id': 'id/', 'en': 'en/'}
HTMLLANG = {'bm': 'ms', 'id': 'id', 'en': 'en'}

SLUG = {
 'home': ('', '', ''),
 'packages': ('pakej', 'paket', 'packages'),
 'cat-umrah': ('pakej/umrah', 'paket/umroh', 'packages/umrah'),
 'cat-plus': ('pakej/umrah-plus', 'paket/umroh-plus', 'packages/umrah-plus'),
 'cat-haji': ('pakej/haji-khusus', 'paket/haji-khusus', 'packages/hajj'),
 'pkg-madinah': ('pakej/umrah-9-hari-madinah', 'paket/umroh-9-hari-madinah', 'packages/umrah-9-days-madinah'),
 'pkg-aqsa': ('pakej/umrah-plus-al-aqsa', 'paket/umroh-plus-al-aqsa', 'packages/umrah-plus-al-aqsa'),
 'pkg-haji': ('pakej/haji-khusus-1448', 'paket/haji-khusus-1448', 'packages/hajj-khusus-1448'),
 'guides': ('mutawwif', 'muthawif', 'our-guides'),
 'guide': ('mutawwif/contoh', 'muthawif/contoh', 'our-guides/sample'),
 'stories': ('kisah-jemaah', 'kisah-jamaah', 'stories'),
 'faq': ('soalan-lazim', 'pertanyaan-umum', 'faq'),
 'about': ('tentang-kami', 'tentang-kami', 'about'),
 'licence': ('lesen-dan-bayaran', 'izin-dan-pembayaran', 'licence-and-payments'),
 'contact': ('hubungi', 'kontak', 'contact'),
 'register': ('daftar', 'daftar', 'register'),
 'thanks': ('terima-kasih', 'terima-kasih', 'thank-you'),
 'terms': ('terma', 'syarat-ketentuan', 'terms'),
 'privacy': ('privasi', 'privasi', 'privacy'),
 'cancel': ('pembatalan', 'pembatalan', 'cancellation'),
 'gifts': ('hadiah-umrah', 'oleh-oleh-umroh', 'umrah-gifts'),
}

L = 'bm'
def t(bm, id_, en):
    return {'bm': bm, 'id': id_, 'en': en}[L]

CUR = ''  # current page path from root
def path_of(key, lang):
    s = SLUG[key][LANGS.index(lang)]
    p = (PREFIX[lang] + s).strip('/')
    return (p + '/') if p else ''
def rel(target):
    depth = CUR.count('/')
    return ('../' * depth) + target
def u(key, lang=None):
    return rel(path_of(key, lang or L))
def a(name):
    return rel('assets/' + name)

WA = '#konsep'
CHECK = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#A6060F" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
PLAY = '<span class="play"><svg width="22" height="22" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="#fff"/></svg></span>'
WAICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a9 9 0 0 1-13.5 7.8L3 21l1.2-4.5A9 9 0 1 1 21 12z"/></svg>'

# ---------- data ----------
def PKGS():
    return [
     dict(key='pkg-madinah', cat='cat-umrah', img='ill-nabawi.jpg', tag=t('Promo','Promo','Promo'),
          name=t('Umrah 9 Hari, Mendarat di Madinah','Umroh 9 Hari, Landing Madinah','Umrah 9 Days, Landing in Madinah'),
          desc=t('Mula dengan tenang di kota Nabi, kemudian ke Makkah bersama mutawwif.','Awali dengan tenang di kota Nabi, lalu ke Makkah bersama muthawif.','Start calmly in the Prophet’s city, then on to Makkah with your guide.'),
          chips=[t('9 hari','9 hari','9 days'),'Oman Air',t('Setaraf 3 bintang','Setaraf bintang 3','3-star equivalent')]),
     dict(key='pkg-aqsa', cat='cat-plus', img='ill-aqsa.jpg', tag='Plus',
          name=t('Umrah Plus Al-Aqsa','Umroh Plus Al-Aqsa','Umrah Plus Al-Aqsa'),
          desc=t('Umrah dan ziarah ke Masjid Al-Aqsa dalam satu perjalanan.','Umroh dan ziarah ke Masjid Al-Aqsa dalam satu perjalanan.','Umrah and a visit to Masjid Al-Aqsa in one journey.'),
          chips=[t('[N] hari','[N] hari','[N] days'),t('[Syarikat penerbangan]','[Maskapai]','[Airline]'),t('[Kategori hotel]','[Kelas hotel]','[Hotel tier]')]),
     dict(key='pkg-haji', cat='cat-haji', img='ill-arafah.jpg', tag=t('Haji','Haji','Hajj'),
          name=t('Haji Khusus 1448H','Haji Khusus 1448H','Hajj Khusus 1448H'),
          desc=t('Persediaan manasik penuh dan layanan khas di Arafah dan Mina.','Persiapan manasik lengkap dan pelayanan khusus di Arafah dan Mina.','Full manasik preparation and dedicated care in Arafah and Mina.'),
          chips=[t('[N] hari','[N] hari','[N] days'),t('Senarai menunggu','Daftar tunggu','Waiting list')]),
    ]
def GUIDES():
    return [('av-mutawwif.jpg', t('[Nama mutawwif 1]','[Nama muthawif 1]','[Guide name 1]')),
            ('av-2.jpg', t('[Nama mutawwif 2]','[Nama muthawif 2]','[Guide name 2]')),
            ('av-1.jpg', t('[Nama mutawwifah 3]','[Nama muthawifah 3]','[Guide name 3]'))]
def CLIPS():
    return [('makkah.jpg', t('City tour Makkah bersama jemaah Kurnia','City tour Makkah bersama jamaah Kurnia','Makkah city tour with Kurnia jemaah')),
            ('clip-thaif.jpg', t('Ziarah ke Thaif','Ziarah ke Thaif','Day trip to Thaif')),
            ('clip-dinner.jpg', t('Makan malam di hotel Makkah','Makan malam di hotel Makkah','Dinner at the Makkah hotel')),
            ('clip-sai.jpg', t('Sai dari Safa ke Marwah','Sa’i dari Shafa ke Marwah','Sa’i between Safa and Marwah'))]
def VOICES():
    return [('av-1.jpg', t('[Testimoni sebenar jemaah, dengan izin. Satu atau dua ayat tentang mutawwif.]','[Testimoni asli jamaah, dengan izin. Satu atau dua kalimat tentang muthawif.]','[Real jemaah testimonial, with permission. A line or two about their guide.]')),
            ('av-2.jpg', t('[Testimoni sebenar jemaah warga emas atau keluarga.]','[Testimoni asli jamaah lansia atau keluarga.]','[Real testimonial from an elderly jemaah or a family.]')),
            ('av-3.jpg', t('[Testimoni sebenar jemaah kali pertama.]','[Testimoni asli jamaah pertama kali.]','[Real testimonial from a first-time jemaah.]'))]

# ---------- components ----------
def nav_items():
    return [('packages', t('Pakej','Paket','Packages')), ('guides', t('Mutawwif Kami','Muthawif Kami','Our Guides')),
            ('stories', t('Kisah Jemaah','Kisah Jamaah','Stories')), ('faq', t('Soalan Lazim','Tanya Jawab','FAQ')),
            ('gifts', t('Hadiah Umrah','Oleh-oleh','Gifts')), ('about', t('Tentang Kami','Tentang Kami','About')), ('contact', t('Hubungi','Kontak','Contact'))]

def head(key, title, desc):
    alts = ''.join(f'<link rel="alternate" hreflang="{HTMLLANG[lg]}" href="{u(key, lg) or "./"}">' for lg in LANGS)
    return f'''<!doctype html>
<html lang="{HTMLLANG[L]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{title} | Kurnia Tour &amp; Travel (konsep)</title>
<meta name="description" content="{html.escape(desc)}">
{alts}
<link rel="icon" href="{a('icon.svg')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Kaushan+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{a('style.css')}">
</head>
<body>'''

def header(key):
    langs = ''.join(f'<a href="{u(key, lg) or "./"}" class="{"on" if lg == L else ""}" lang="{HTMLLANG[lg]}">{lg.upper() if lg != "bm" else "BM"}</a>' for lg in LANGS)
    navs = ''.join(f'<a href="{u(k)}" class="{"on" if k == key or (k == "packages" and key.startswith(("cat-", "pkg-"))) or (k == "guides" and key == "guide") else ""}">{n}</a>' for k, n in nav_items())
    panel = ''.join(f'<a href="{u(k)}">{n}</a>' for k, n in nav_items())
    return f'''<div class="concept" id="konsep">{t('Konsep reka bentuk oleh KL Tech untuk Kurnia Tour &amp; Travel. Bukan laman web rasmi. Borang dan butang WhatsApp tidak menghantar apa-apa.','Konsep desain oleh KL Tech untuk Kurnia Tour &amp; Travel. Bukan website resmi. Formulir dan tombol WhatsApp tidak mengirim apa pun.','Design concept by KL Tech for Kurnia Tour &amp; Travel. Not the official website. Forms and WhatsApp buttons send nothing.')}</div>
<div class="topbar"><div class="wrap"><span>{t('Pengendali Umrah &amp; Haji berlesen','Penyelenggara Umroh &amp; Haji berizin','Licensed Umrah &amp; Hajj operator')} · [{t('No. lesen','No. izin','Licence no.')}] · {t('Sejak 2010','Sejak 2010','Since 2010')}</span><nav class="lang" aria-label="{t('Bahasa','Bahasa','Language')}">{langs}</nav></div></div>
<header class="header"><div class="wrap">
<a class="logo" href="{u('home') or './'}"><img src="{a('logo.svg')}" alt="Kurnia tour and travel" width="130" height="64"></a>
<nav class="nav" aria-label="{t('Utama','Utama','Main')}">{navs}</nav>
<a class="btn btn-red" href="{WA}">WhatsApp {t('kami','kami','us')}</a>
<details class="menu"><summary aria-label="Menu"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#232325" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary><div class="panel">{panel}<a href="{WA}" style="color:#A6060F">WhatsApp {t('kami','kami','us')}</a></div></details>
</div></header>
<main>'''

def footer():
    return f'''</main>
<footer class="footer"><div class="wrap">
<div class="cols">
<div><img src="{a('logo-reverse.svg')}" alt="Kurnia tour and travel" style="height:68px;width:auto;margin-bottom:12px"><span>PT. Kurnia Jaya International · Alfaidah Grup</span><br><span>[{t('No. lesen PPIU / PIHK / MOTAC','No. izin PPIU / PIHK / MOTAC','PPIU / PIHK / MOTAC licence nos.')}]</span></div>
<div><b>Malaysia</b><span>Taman Tanjong Minyak Ria, Melaka</span><br><span>+60 17-611 2236</span></div>
<div><b>Indonesia</b><span>Jl. Raya Gading Asri No. 8, Cianjur</span><br><span>+62 857-2266-6585</span></div>
<div><b>{t('Pautan','Tautan','Links')}</b><a href="{u('packages')}">{t('Pakej','Paket','Packages')}</a><a href="{u('gifts')}">{t('Hadiah Umrah (Safar Gifts)','Oleh-oleh Umroh (Safar Gifts)','Umrah Gifts (Safar Gifts)')}</a><a href="{u('licence')}">{t('Lesen dan bayaran','Izin dan pembayaran','Licence and payments')}</a><a href="{u('terms')}">{t('Terma dan Syarat','Syarat dan Ketentuan','Terms')}</a><a href="{u('privacy')}">{t('Dasar Privasi','Kebijakan Privasi','Privacy')}</a><a href="{u('cancel')}">{t('Pembatalan dan bayaran balik','Pembatalan dan pengembalian dana','Cancellation and refunds')}</a></div>
</div>
<div class="base"><span>© Kurnia Tour &amp; Travel</span><span>{t('Konsep reka bentuk oleh KL Tech','Konsep desain oleh KL Tech','Design concept by KL Tech')}</span></div>
</div></footer>
<a class="fab" href="{WA}" aria-label="WhatsApp">{WAICON}</a>
</body></html>'''

def page_hero(crumb, title, lead):
    return f'<div class="phero"><div class="wrap"><div class="crumb"><a href="{u("home") or "./"}">{t("Utama","Beranda","Home")}</a> / {crumb}</div><h1>{title}</h1><p>{lead}</p></div></div>'

def pkg_card(p):
    g = GUIDES()[0]
    return f'''<a class="card" href="{u(p['key'])}"><div class="img"><img src="{a(p['img'])}" alt="" loading="lazy"><span class="tag">{p['tag']}</span></div><div class="body">
<h3>{p['name']}</h3><p>{p['desc']}</p><div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in p['chips'])}</div>
<div class="leader"><img src="{a(g[0])}" alt="">{t('Dibimbing oleh','Dibimbing oleh','Led by')} {g[1]}</div>
<div class="price"><span class="muted">{t('dari','mulai','from')}</span><b>[{t('HARGA','HARGA','PRICE')}]</b></div></div></a>'''

def clips_section():
    cl = ''.join(f'<a class="clip" href="{WA}"><img src="{a(i)}" alt="" loading="lazy">{PLAY}<b>{tt}</b><small>[{t("Tarikh","Tanggal","Date")}] · [N] {t("tontonan","tayangan","views")}</small></a>' for i, tt in CLIPS())
    return f'''<section class="sec-dark"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{t('Dari Tanah Suci, minggu ini','Dari Tanah Suci, minggu ini','From the Holy Land, this week')}</span><h2>{t('Tengok sendiri perjalanan jemaah kami','Lihat sendiri perjalanan jamaah kami','See our jemaah’s journey for yourself')}</h2></div><a href="{WA}" style="color:#fff;font-weight:800;border-bottom:2px solid #FF5A5F">{t('Ikuti di TikTok','Ikuti di TikTok','Follow on TikTok')} @[handle]</a></div><div class="clips">{cl}</div></div></section>'''

def voices_section(title=True):
    v = ''.join(f'<div class="voice"><p>{q}</p><div class="who"><img src="{a(i)}" alt=""><div><b>[{t("Nama","Nama","Name")}], [{t("Bandar","Kota","City")}]</b><small>{t("Umrah","Umroh","Umrah")} [{t("Bulan Tahun","Bulan Tahun","Month Year")}]</small></div></div></div>' for i, q in VOICES())
    h = f'<div class="sec-head"><div><span class="eyebrow">{t("Kisah jemaah","Kisah jamaah","Jemaah stories")}</span><h2>{t("Kata mereka sendiri","Kata mereka sendiri","In their own words")}</h2></div></div>' if title else ''
    return f'<section><div class="wrap">{h}<div class="grid g3">{v}</div></div></section>'

def trust_strip():
    items = [t('Pengendali berlesen, nombor lesen di setiap halaman','Penyelenggara berizin, nomor izin di setiap halaman','Licensed operator, licence number on every page'),
             t('Resit rasmi bagi setiap bayaran [sahkan]','Kuitansi resmi untuk setiap pembayaran [konfirmasi]','Official receipt for every payment [to confirm]'),
             t('Mutawwif dari berlepas hingga pulang','Muthawif dari berangkat hingga pulang','A guide from departure to return'),
             t('Pejabat di Cianjur dan Melaka','Kantor di Cianjur dan Melaka','Offices in Cianjur and Melaka')]
    return f'<section class="sec-sand" style="padding:28px 0"><div class="wrap trust">{"".join(f"<div>{CHECK}<span>{i}</span></div>" for i in items)}</div></section>'

def cta(title, body, btn_key=None):
    href = u(btn_key) if btn_key else WA
    return f'<section><div class="wrap"><div class="cta"><div><h2>{title}</h2><p>{body}</p></div><a class="btn btn-white" href="{href}">{t("WhatsApp kami","WhatsApp kami","WhatsApp us") if not btn_key else t("Daftar sekarang","Daftar sekarang","Register now")}</a></div></div></section>'

def guide_cards():
    out = ''
    for i, (img, nm) in enumerate(GUIDES()):
        out += f'''<a class="card guide" href="{u('guide')}"><img src="{a(img)}" alt=""><h3>{nm}</h3><p class="muted">[N] {t('tahun membimbing jemaah','tahun membimbing jamaah','years guiding jemaah')}</p><div class="chips" style="justify-content:center"><span class="chip">BM</span><span class="chip">ID</span><span class="chip">{t('Arab','Arab','Arabic')}</span></div><span style="font-weight:800">{t('Kenali beliau','Kenali beliau','Meet them')} →</span></a>'''
    return out

# ---------- pages ----------
def p_home():
    g = GUIDES()[0]
    pk = ''.join(pkg_card(p) for p in PKGS())
    body = f'''<div class="hero"><div class="wrap">
<div class="hero-text">
<span class="live"><i></i>{t('Kumpulan [Bulan] sedang di Makkah','Rombongan [Bulan] sedang di Makkah','The [Month] group is in Makkah now')}</span>
<h1>{t('Umrah bersama orang yang anda <span class="script">kenal</span>, bukan sekadar agensi.','Umroh bersama orang yang Anda <span class="script">kenal</span>, bukan sekadar agen.','Umrah with people you <span class="script">know</span>, not just an agency.')}</h1>
<p class="lead">{t('Kenali mutawwif anda sebelum berlepas. Tengok sendiri perjalanan jemaah kami minggu ini. Tanya terus di WhatsApp, kami jawab macam kawan.','Kenali muthawif Anda sebelum berangkat. Lihat sendiri perjalanan jamaah kami minggu ini. Tanya langsung di WhatsApp, kami jawab seperti teman.','Meet your guide before you fly. Watch our jemaah’s journey this week. Ask us on WhatsApp and we’ll answer like a friend.')}</p>
<div class="btn-row"><a class="btn btn-red" href="{u('guides')}">{t('Kenali mutawwif kami','Kenali muthawif kami','Meet our guides')}</a><a class="btn btn-line" href="{u('packages')}">{t('Lihat pakej','Lihat paket','See packages')}</a></div>
<div style="display:flex;gap:28px;flex-wrap:wrap;padding-top:8px"><div class="stat"><b>2010</b><span>{t('Mula berkhidmat','Mulai melayani','Serving since')}</span></div><div class="stat"><b>25K+</b><span>{t('Pengikut Instagram','Pengikut Instagram','Instagram followers')}</span></div><div class="stat"><b>[N]</b><span>{t('Jemaah dibawa','Jamaah diberangkatkan','Jemaah served')}</span></div></div>
</div>
<div class="collage">
<div class="big"><img src="{a('makkah.jpg')}" alt="{t('Ilustrasi Masjidil Haram pada waktu senja','Ilustrasi Masjidil Haram saat senja','Illustration of Masjidil Haram at dusk')}"><div class="mcard"><img src="{a(g[0])}" alt=""><div><b>{g[1]}</b><small>[N] {t('tahun membimbing · BM, ID, Arab','tahun membimbing · BM, ID, Arab','years guiding · BM, ID, Arabic')}</small></div><a href="{WA}">{t('Tanya beliau','Tanya beliau','Ask them')}</a></div></div>
<div class="tile"><img src="{a('ph-jemaah.jpg')}" alt=""></div>
<div class="tile"><img src="{a('ph-family.jpg')}" alt=""></div>
<div class="band"><span class="script">{t('Jemaah kami sedang di Makkah','Jamaah kami sedang di Makkah','Our jemaah are in Makkah now')}</span><span>{t('Kumpulan [Bulan] · [N] jemaah · kemas kini harian di TikTok','Rombongan [Bulan] · [N] jamaah · update harian di TikTok','[Month] group · [N] jemaah · daily updates on TikTok')}</span></div>
</div></div></div>
{trust_strip()}
{clips_section()}
<section><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{t('Pakej','Paket','Packages')}</span><h2>{t('Pilih perjalanan anda','Pilih perjalanan Anda','Choose your journey')}</h2></div><a href="{u('packages')}" style="font-weight:800">{t('Semua pakej','Semua paket','All packages')} →</a></div><div class="grid g3">{pk}</div></div></section>
<section class="sec-sand"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{t('Mutawwif kami','Muthawif kami','Our guides')}</span><h2>{t('Kenali siapa yang akan membimbing anda','Kenali siapa yang akan membimbing Anda','Meet the people who will guide you')}</h2></div><a href="{u('guides')}" style="font-weight:800">{t('Semua mutawwif','Semua muthawif','All guides')} →</a></div><div class="grid g3">{guide_cards()}</div></div></section>
<section style="padding:0"><div class="wrap"><a href="{u('gifts')}" style="display:flex;flex-wrap:wrap;align-items:center;gap:24px;background:#FBF6EC;border:1px solid #E2D6BF;border-radius:24px;padding:20px;color:#22231F"><img src="{a('safar-hero.jpg')}" alt="" style="width:260px;max-width:100%;border-radius:16px"><div style="flex:1 1 300px"><img src="{a('safar-logo.svg')}" alt="Safar Gifts" style="height:44px;width:auto;margin-bottom:8px"><b style="font-size:22px;display:block;color:#1F4D3A">{t('Hadiah Umrah dari SAR 3 sebiji','Oleh-oleh Umroh mulai SAR 3 per buah','Umrah gifts from SAR 3 each')}</b><span style="color:#4A4A44">{t('Zamzam, kurma dan manisan dalam pek 10 atau 20, diambil di hotel anda.','Zamzam, kurma dan manisan dalam paket isi 10 atau 20, diambil di hotel Anda.','Zamzam, dates and sweets in packs of 10 or 20, collected at your hotel.')}</span></div><span class="btn btn-line">{t('Lihat','Lihat','See more')} →</span></a></div></section>
{voices_section()}
{cta(t('Tidak pasti pakej mana sesuai?','Belum yakin paket mana yang cocok?','Not sure which package fits?'), t('Ceritakan tarikh, bajet dan siapa yang akan pergi. Mutawwif kami bantu pilihkan.','Ceritakan tanggal, anggaran dan siapa yang berangkat. Muthawif kami bantu pilihkan.','Tell us your dates, budget and who is travelling. Our guides will help you choose.'))}'''
    return t('Umrah bersama orang yang anda kenal','Umroh bersama orang yang Anda kenal','Umrah with people you know'), t('Pengendali Umrah dan Haji sejak 2010.','Penyelenggara Umroh dan Haji sejak 2010.','Umrah and Hajj operator since 2010.'), body

def listing(title, lead, crumb, pkgs, extra=''):
    filters = f'''<div class="box" style="flex-direction:row;flex-wrap:wrap;align-items:flex-end;gap:16px;margin-bottom:28px">
<label style="flex:1 1 180px">{t('Jenis','Jenis','Type')}<select><option>{t('Semua','Semua','All')}</option><option>Umrah</option><option>Umrah Plus</option><option>{t('Haji Khusus','Haji Khusus','Hajj Khusus')}</option></select></label>
<label style="flex:1 1 180px">{t('Bulan','Bulan','Month')}<select><option>{t('Mana-mana','Kapan saja','Any')}</option><option>Rejab 1448</option><option>Syaaban 1448</option><option>Ramadan 1448</option></select></label>
<label style="flex:1 1 180px">{t('Berlepas dari','Berangkat dari','Depart from')}<select><option>KLIA</option><option>Jakarta</option></select></label>
<a class="btn btn-red" href="#" style="flex:0 0 auto">{t('Tapis','Filter','Filter')}</a></div>'''
    return page_hero(crumb, title, lead) + f'<section><div class="wrap">{filters}{extra}<div class="grid g3">{"".join(pkg_card(p) for p in pkgs)}</div></div></section>' + cta(t('Mahu pakej khas untuk kumpulan anda?','Ingin paket khusus untuk rombongan Anda?','Want a custom package for your group?'), t('Untuk 10 jemaah ke atas, kami susun tarikh dan hotel ikut keperluan anda.','Untuk 10 jamaah ke atas, kami atur tanggal dan hotel sesuai kebutuhan Anda.','For 10 or more jemaah, we arrange dates and hotels around you.'))

def p_packages():
    return t('Pakej','Paket','Packages'), '', listing(t('Pakej Umrah dan Haji','Paket Umroh dan Haji','Umrah and Hajj packages'), t('Setiap pakej menyatakan apa yang termasuk, siapa mutawwifnya dan jarak hotel ke Haram.','Setiap paket mencantumkan fasilitas, siapa muthawifnya dan jarak hotel ke Haram.','Every package shows what is included, who leads it and how far the hotel is from the Haram.'), t('Pakej','Paket','Packages'), PKGS(),
      f'<div class="chips" style="margin-bottom:24px"><a class="chip" href="{u("cat-umrah")}">Umrah</a><a class="chip" href="{u("cat-plus")}">Umrah Plus</a><a class="chip" href="{u("cat-haji")}">{t("Haji Khusus","Haji Khusus","Hajj Khusus")}</a></div>')

def cat_page(cat, title, lead, who):
    pk = [p for p in PKGS() if p['cat'] == cat]
    crumb = f'<a href="{u("packages")}">{t("Pakej","Paket","Packages")}</a> / {title}'
    return title, lead, listing(title, lead, crumb, pk, f'<p class="prose" style="margin-bottom:28px">{who}</p>')
def p_cat_umrah(): return cat_page('cat-umrah', 'Umrah', t('Pakej Umrah dari 9 hari, mendarat di Madinah atau Jeddah.','Paket Umroh mulai 9 hari, landing Madinah atau Jeddah.','Umrah packages from 9 days, landing in Madinah or Jeddah.'), t('Sesuai untuk jemaah kali pertama, keluarga dan warga emas. Lebih banyak pakej akan ditambah setiap musim.','Cocok untuk jamaah pertama kali, keluarga dan lansia. Paket baru ditambahkan setiap musim.','Suits first-timers, families and elderly jemaah. More packages are added each season.'))
def p_cat_plus(): return cat_page('cat-plus', 'Umrah Plus', t('Umrah bersama ziarah ke Al-Aqsa atau Turki.','Umroh dengan ziarah ke Al-Aqsa atau Turki.','Umrah with a visit to Al-Aqsa or Turkey.'), t('Untuk jemaah yang mahu menyambung ibadah dengan ziarah sejarah Islam.','Untuk jamaah yang ingin melanjutkan ibadah dengan ziarah sejarah Islam.','For jemaah who want to add a journey through Islamic history.'))
def p_cat_haji(): return cat_page('cat-haji', t('Haji Khusus','Haji Khusus','Hajj Khusus'), t('Program Haji Khusus dengan persediaan manasik penuh.','Program Haji Khusus dengan persiapan manasik lengkap.','Special Hajj programme with full manasik preparation.'), t('Tempat Haji Khusus terhad. Daftar minat dahulu, kami hubungi anda tentang kelayakan dan senarai menunggu.','Kuota Haji Khusus terbatas. Daftar minat dahulu, kami hubungi Anda soal syarat dan daftar tunggu.','Hajj Khusus places are limited. Register interest first and we will contact you about eligibility and the waiting list.'))

def detail(p, days, incl, excl):
    g = GUIDES()[0]
    tl = ''.join(f'<div><b>{d}</b><h3>{h}</h3><p>{b}</p></div>' for d, h, b in days)
    inc = ''.join(f'<div>{CHECK}<span>{i}</span></div>' for i in incl)
    faqs = faq_items()[:3]
    fq = ''.join(f'<details class="faq"><summary>{q}</summary><p>{a_}</p></details>' for q, a_ in faqs)
    crumb = f'<a href="{u("packages")}">{t("Pakej","Paket","Packages")}</a> / {p["name"]}'
    body = page_hero(crumb, p['name'], p['desc']) + f'''<section><div class="wrap detail">
<main>
<div style="border-radius:24px;overflow:hidden;aspect-ratio:16/8"><img src="{a(p['img'])}" alt="" style="width:100%;height:100%;object-fit:cover"></div>
<div class="chips">{''.join(f'<span class="chip">{c}</span>' for c in p['chips'])}<span class="chip">{t('Hotel ke Haram: [jarak]','Hotel ke Haram: [jarak]','Hotel to Haram: [distance]')}</span></div>
<div class="box" style="flex-direction:row;align-items:center;gap:16px"><img src="{a(g[0])}" alt="" style="width:72px;height:72px;border-radius:50%"><div style="flex:1"><span class="eyebrow">{t('Mutawwif anda','Muthawif Anda','Your guide')}</span><h3 style="font-size:20px;margin-top:4px">{g[1]}</h3><p class="muted">[N] {t('tahun membimbing jemaah · BM, ID, Arab','tahun membimbing jamaah · BM, ID, Arab','years guiding jemaah · BM, ID, Arabic')}</p></div><a class="btn btn-line" href="{u('guide')}">{t('Profil','Profil','Profile')}</a></div>
<div><h2 style="font-size:28px;margin-bottom:16px">{t('Apa yang termasuk','Fasilitas yang didapat','What is included')}</h2><div class="incl">{inc}</div><p class="muted" style="margin-top:12px">{excl}</p></div>
<div><h2 style="font-size:28px;margin-bottom:16px">{t('Jadual perjalanan','Itinerary','Itinerary')}</h2><div class="tl">{tl}</div></div>
<div><h2 style="font-size:28px;margin-bottom:16px">{t('Dari kumpulan lepas','Dari rombongan sebelumnya','From past groups')}</h2><div class="clips">{''.join(f'<a class="clip" href="{WA}"><img src="{a(i)}" alt="" loading="lazy">{PLAY}<b>{tt}</b></a>' for i, tt in CLIPS()[:3])}</div></div>
<div><h2 style="font-size:28px;margin-bottom:16px">{t('Soalan lazim','Tanya jawab','Common questions')}</h2><div style="display:flex;flex-direction:column;gap:10px">{fq}</div></div>
</main>
<aside>
<div class="box" style="box-shadow:0 12px 30px rgba(35,35,37,.08)">
<div><span class="muted" style="font-size:13px">{t('Dari, seorang','Mulai, per orang','From, per person')}</span><div style="font-size:32px;font-weight:900;color:#A6060F">[{t('HARGA','HARGA','PRICE')}]</div></div>
<div class="rooms"><span class="on">{t('Berempat','Quad','Quad')}<br>[{t('HARGA','HARGA','PRICE')}]</span><span>{t('Bertiga','Triple','Triple')}<br>[{t('HARGA','HARGA','PRICE')}]</span><span>{t('Berdua','Double','Double')}<br>[{t('HARGA','HARGA','PRICE')}]</span></div>
<label>{t('Tarikh berlepas','Tanggal keberangkatan','Departure date')}<select><option>[{t('Tarikh 1','Tanggal 1','Date 1')}] · [N] {t('tempat','kursi','seats')}</option><option>[{t('Tarikh 2','Tanggal 2','Date 2')}] · [N] {t('tempat','kursi','seats')}</option></select></label>
<p class="muted" style="font-size:14px;background:#F6F3EE;padding:12px;border-radius:12px">{t('Deposit [JUMLAH] untuk menjamin tempat. Baki dijelaskan [N] hari sebelum berlepas.','DP [JUMLAH] untuk mengamankan kursi. Pelunasan [N] hari sebelum berangkat.','Deposit [AMOUNT] secures your seat. Balance due [N] days before departure.')}</p>
<a class="btn btn-red" href="{u('register')}">{t('Tempah tempat saya','Pesan kursi saya','Reserve my seat')}</a>
<a class="btn btn-line" href="{WA}">{t('Tanya di WhatsApp','Tanya via WhatsApp','Ask on WhatsApp')}</a>
</div>
<div class="box box-dark"><b>{t('Semak sebelum membayar','Cek sebelum membayar','Check before you pay')}</b><p>{t('Lesen Kurnia: [No.]. Kami tidak pernah meminta bayaran ke akaun peribadi.','Izin Kurnia: [No.]. Kami tidak pernah meminta pembayaran ke rekening pribadi.','Kurnia licence: [No.]. We never ask for payment to a personal account.')}</p><a href="{u('licence')}" style="color:#FF5A5F;font-weight:800">{t('Cara semak lesen','Cara cek izin','How to verify')} →</a></div>
</aside></div></section>'''
    return p['name'], p['desc'], body

def p_pkg_madinah():
    p = PKGS()[0]
    days = [(t('Hari 1','Hari ke-1','Day 1'), t('Berlepas, transit, tiba di Madinah','Berangkat, transit, tiba di Madinah','Depart, transit, arrive in Madinah'), t('Berkumpul di lapangan terbang 4 jam sebelum berlepas. Kad ID, pasport dan pas masuk diedarkan.','Berkumpul di bandara 4 jam sebelum keberangkatan. Pembagian ID card, paspor dan boarding pass.','Meet at the airport 4 hours before departure. ID cards, passports and boarding passes handed out.')),
            (t('Hari 2','Hari ke-2','Day 2'), 'Masjid Nabawi', t('Solat lima waktu di Masjid Nabawi. Ziarah ke makam Rasulullah, Raudhah dan Baqi.','Shalat lima waktu di Masjid Nabawi. Ziarah ke makam Rasulullah SAW, Raudhah dan Baqi.','Pray all five prayers at Masjid Nabawi. Visit the Prophet’s resting place, Raudhah and Baqi.')),
            (t('Hari 3','Hari ke-3','Day 3'), t('Lawatan bandar Madinah','City tour Madinah','Madinah city tour'), t('[Lokasi ziarah: Quba, Uhud, Qiblatain. Sahkan dengan Kurnia.]','[Lokasi ziarah: Quba, Uhud, Qiblatain. Konfirmasi dengan Kurnia.]','[Stops: Quba, Uhud, Qiblatain. To confirm with Kurnia.]')),
            (t('Hari 4','Hari ke-4','Day 4'), t('Ke Makkah, tunaikan Umrah','Ke Makkah, melaksanakan Umroh','To Makkah, perform Umrah'), t('Miqat di Bir Ali, ke Makkah, kemudian Umrah bersama mutawwif.','Miqat di Bir Ali, menuju Makkah, lalu Umroh bersama muthawif.','Miqat at Bir Ali, travel to Makkah, then Umrah with your guide.')),
            (t('Hari 5 hingga 7','Hari ke-5 s/d 7','Days 5 to 7'), t('Ibadah di Makkah','Ibadah di Makkah','Worship in Makkah'), t('Masa bebas di Masjidil Haram. Lawatan bandar Makkah dan pilihan ke Thaif.','Waktu bebas di Masjidil Haram. City tour Makkah dan opsional ke Thaif.','Free time at Masjidil Haram. Makkah city tour and an optional trip to Thaif.')),
            (t('Hari 8','Hari ke-8','Day 8'), t('Tawaf Wada, ke Jeddah','Thawaf Wada, ke Jeddah','Farewell tawaf, to Jeddah'), t('Tawaf selamat tinggal, kemudian ke lapangan terbang Jeddah.','Thawaf perpisahan, lalu menuju bandara Jeddah.','Farewell tawaf, then to Jeddah airport.')),
            (t('Hari 9','Hari ke-9','Day 9'), t('Tiba di tanah air','Tiba di tanah air','Arrive home'), t('Mendarat di [KL / Jakarta].','Mendarat di [KL / Jakarta].','Land in [KL / Jakarta].'))]
    incl = [t('Tiket pergi balik, Oman Air mendarat di Madinah','Tiket pesawat PP, Oman Air landing Madinah','Return flights, Oman Air landing in Madinah'), t('Urusan visa Umrah','Pengurusan visa Umroh','Umrah visa processing'), t('Hotel 4 orang sebilik, setaraf 3 bintang','Hotel 1 kamar ber-4, setaraf bintang 3','Hotel, 4 to a room, 3-star equivalent'), t('Makan 3 kali sehari','Makan 3x sehari','Three meals a day'), t('Bas berhawa dingin','Bus AC','Air-conditioned bus'), t('Tiket masuk ziarah','Tiket masuk wisata','Visit entry tickets'), t('Mutawwif dan ketua rombongan','Muthawif dan tour leader','Guide and tour leader'), t('Kit Umrah dan kelas manasik','Perlengkapan Umroh dan manasik','Umrah kit and manasik class')]
    excl = t('Tidak termasuk: vaksin Meningitis ACWY, perbelanjaan peribadi, [lain-lain].','Tidak termasuk: vaksin Meningitis ACWY, pengeluaran pribadi, [lainnya].','Not included: Meningitis ACWY vaccine, personal spending, [other].')
    return detail(p, days, incl, excl)

def short_detail(p):
    days = [(t('Jadual penuh','Itinerary lengkap','Full itinerary'), t('[Jadual hari demi hari daripada Kurnia]','[Itinerary harian dari Kurnia]','[Day-by-day itinerary from Kurnia]'), t('Akan dilengkapkan apabila Kurnia berkongsi butiran pakej.','Akan dilengkapi setelah Kurnia membagikan detail paket.','To be completed once Kurnia shares the package details.'))]
    incl = [t('[Senarai termasuk daripada Kurnia]','[Daftar fasilitas dari Kurnia]','[Inclusions from Kurnia]')]
    return detail(p, days, incl, t('Tidak termasuk: [daripada Kurnia].','Tidak termasuk: [dari Kurnia].','Not included: [from Kurnia].'))
def p_pkg_aqsa(): return short_detail(PKGS()[1])
def p_pkg_haji(): return short_detail(PKGS()[2])

def p_guides():
    body = page_hero(t('Mutawwif Kami','Muthawif Kami','Our Guides'), t('Kenali mutawwif anda sebelum berlepas','Kenali muthawif Anda sebelum berangkat','Meet your guide before you fly'), t('Setiap kumpulan Kurnia dibimbing oleh mutawwif yang sama dari lapangan terbang hingga pulang.','Setiap rombongan Kurnia dibimbing oleh muthawif yang sama dari bandara hingga pulang.','Every Kurnia group has the same guide from the airport until you are home.')) + f'<section><div class="wrap"><div class="grid g3">{guide_cards()}</div></div></section>' + cta(t('Mahu bercakap dengan mutawwif dahulu?','Ingin bicara dengan muthawif dulu?','Want to talk to a guide first?'), t('Tanya apa sahaja tentang manasik, kesihatan atau pakej.','Tanya apa saja soal manasik, kesehatan atau paket.','Ask anything about manasik, health or packages.'))
    return t('Mutawwif Kami','Muthawif Kami','Our Guides'), '', body

def p_guide():
    g = GUIDES()[0]
    crumb = f'<a href="{u("guides")}">{t("Mutawwif Kami","Muthawif Kami","Our Guides")}</a> / {g[1]}'
    body = f'''<div class="phero"><div class="wrap" style="display:flex;flex-wrap:wrap;gap:32px;align-items:center"><img src="{a(g[0])}" alt="" style="width:160px;height:160px;border-radius:50%"><div style="flex:1 1 400px"><div class="crumb"><a href="{u("home") or "./"}">{t("Utama","Beranda","Home")}</a> / {crumb}</div><h1>{g[1]}</h1><p>[N] {t('tahun membimbing jemaah · BM, ID, Arab · [Kelayakan]','tahun membimbing jamaah · BM, ID, Arab · [Kualifikasi]','years guiding jemaah · BM, ID, Arabic · [Qualification]')}</p><div class="btn-row" style="margin-top:16px"><a class="btn btn-red" href="{WA}">{t('WhatsApp beliau','WhatsApp beliau','WhatsApp them')}</a></div></div></div></div>
<section><div class="wrap grid g2" style="align-items:start"><div class="prose"><h2>{t('Tentang beliau','Tentang beliau','About')}</h2><p>[{t('Biodata ringkas mutawwif, ditulis bersama beliau: latar belakang, pengajian, kenapa beliau membimbing jemaah.','Biodata singkat muthawif, ditulis bersama beliau: latar belakang, pendidikan, alasan membimbing jamaah.','A short bio written with the guide: background, studies, why they guide jemaah.')}]</p></div>
<div class="box"><b>{t('Kumpulan seterusnya bersama beliau','Rombongan berikutnya bersama beliau','Next groups with this guide')}</b>{''.join(f'<a href="{u(p["key"])}" style="display:flex;justify-content:space-between;border-top:1px solid #DEDCD8;padding-top:10px;color:#232325"><span>{p["name"]}</span><span class="muted">[{t("Tarikh","Tanggal","Date")}]</span></a>' for p in PKGS()[:2])}</div></div></section>
{clips_section()}{voices_section(False)}'''
    return g[1], '', body

def p_stories():
    body = page_hero(t('Kisah Jemaah','Kisah Jamaah','Stories'), t('Kisah jemaah Kurnia','Kisah jamaah Kurnia','Stories from Kurnia jemaah'), t('Video, gambar dan kata-kata jemaah dari setiap kumpulan.','Video, foto dan cerita jamaah dari setiap rombongan.','Videos, photos and words from every group.')) + clips_section() + voices_section(False) + f'<section class="sec-sand"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{t("Galeri kumpulan","Galeri rombongan","Group gallery")}</span><h2>{t("Mengikut bulan","Per bulan","By month")}</h2></div></div><div class="grid g4">{"".join(f"<div class=card><div class=img><img src={a(i)} alt=></div><div class=body><b>[{t(chr(66)+chr(117)+chr(108)+chr(97)+chr(110),chr(66)+chr(117)+chr(108)+chr(97)+chr(110),chr(77)+chr(111)+chr(110)+chr(116)+chr(104))}] 1447</b></div></div>" for i in ["ph-jemaah.jpg","ph-family.jpg","ill-umbrellas.jpg","ill-nabawi.jpg"])}</div></div></section>'
    return t('Kisah Jemaah','Kisah Jamaah','Stories'), '', body

def faq_items():
    return [(t('Bolehkah wanita pergi tanpa mahram?','Apakah wanita bisa berangkat tanpa mahram?','Can women travel without a mahram?'), t('Ya, wanita 18 tahun ke atas boleh menunaikan Umrah dengan e-visa Nusuk. [Kurnia sahkan cara kumpulan disusun.]','Ya, wanita usia 18 tahun ke atas dapat berumroh dengan e-visa Nusuk. [Kurnia konfirmasi pengaturan rombongan.]','Yes, women aged 18 and above can perform Umrah on a Nusuk e-visa. [Kurnia to confirm how groups are arranged.]')),
            (t('Vaksin apa yang diperlukan?','Vaksin apa yang diperlukan?','Which vaccines do I need?'), t('Meningitis ACWY wajib sebelum Umrah dan tidak termasuk dalam pakej.','Meningitis ACWY wajib sebelum Umroh dan tidak termasuk dalam paket.','Meningitis ACWY is required before Umrah and is not included in the package.')),
            (t('Boleh bayar secara ansuran?','Bisa bayar dicicil?','Can I pay in instalments?'), t('[Kurnia sahkan pilihan ansuran atau tabungan Umrah.]','[Kurnia konfirmasi opsi cicilan atau tabungan Umroh.]','[Kurnia to confirm instalment or savings options.]')),
            (t('Bagaimana jika saya perlu membatalkan?','Bagaimana jika saya harus membatalkan?','What if I need to cancel?'), t('Lihat dasar pembatalan. [Kurnia sahkan jadual bayaran balik.]','Lihat kebijakan pembatalan. [Kurnia konfirmasi ketentuan pengembalian dana.]','See the cancellation policy. [Kurnia to confirm the refund schedule.]')),
            (t('Adakah warga emas dibantu?','Apakah lansia dibantu?','Is help available for elderly jemaah?'), t('[Kurnia sahkan bantuan kerusi roda dan susunan bilik.]','[Kurnia konfirmasi bantuan kursi roda dan pembagian kamar.]','[Kurnia to confirm wheelchair help and room arrangements.]')),
            (t('Bagaimana saya tahu Kurnia sah?','Bagaimana saya tahu Kurnia resmi?','How do I know Kurnia is legitimate?'), t('Semak nombor lesen kami di halaman Lesen dan Bayaran, dan bayar hanya ke akaun syarikat.','Cek nomor izin kami di halaman Izin dan Pembayaran, dan bayar hanya ke rekening perusahaan.','Check our licence numbers on the Licence and Payments page, and pay only into company accounts.'))]

def p_faq():
    fq = ''.join(f'<details class="faq"><summary>{q}</summary><p>{a_}</p></details>' for q, a_ in faq_items())
    body = page_hero(t('Soalan Lazim','Tanya Jawab','FAQ'), t('Soalan lazim','Pertanyaan umum','Common questions'), t('Tidak jumpa jawapan? Tanya kami di WhatsApp.','Tidak menemukan jawaban? Tanya kami di WhatsApp.','Can’t find an answer? Ask us on WhatsApp.')) + f'<section><div class="wrap" style="max-width:860px;display:flex;flex-direction:column;gap:10px">{fq}</div></section>' + cta(t('Masih ada soalan?','Masih ada pertanyaan?','Still have a question?'), t('Mutawwif kami jawab sendiri.','Muthawif kami menjawab langsung.','Our guides answer personally.'))
    return t('Soalan Lazim','Tanya Jawab','FAQ'), '', body

def p_about():
    ms = [('2010', t('PT. Kurnia Jaya International ditubuhkan di Cianjur, 21 Mac.','PT. Kurnia Jaya International berdiri di Cianjur, 21 Maret.','PT. Kurnia Jaya International founded in Cianjur on 21 March.')), ('[' + t('Tahun','Tahun','Year') + ']', t('[Kumpulan Haji Khusus pertama.]','[Rombongan Haji Khusus pertama.]','[First Hajj Khusus group.]')), ('[' + t('Tahun','Tahun','Year') + ']', t('Cawangan Malaysia dibuka di Melaka.','Cabang Malaysia dibuka di Melaka.','Malaysia branch opens in Melaka.')), ('[' + t('Tahun','Tahun','Year') + ']', t('[Pencapaian lain.]','[Pencapaian lain.]','[Another milestone.]'))]
    body = page_hero(t('Tentang Kami','Tentang Kami','About'), t('Berkhidmat untuk tetamu Allah sejak 2010','Melayani tamu Allah sejak 2010','Serving the guests of Allah since 2010'), t('PT. Kurnia Jaya International, di bawah Alfaidah Grup. Bermula di Cianjur, kini dengan cawangan di Melaka.','PT. Kurnia Jaya International, di bawah Alfaidah Grup. Berawal dari Cianjur, kini dengan cabang di Melaka.','PT. Kurnia Jaya International, part of Alfaidah Grup. Started in Cianjur, now with a branch in Melaka.')) + f'''<section><div class="wrap grid g2" style="align-items:center"><div class="prose"><span class="eyebrow">{t('Pengasas','Pendiri','Founder')}</span><h2 style="font-size:32px">H. Andri Anggi Kurnia</h2><p>[{t('Pesanan ringkas pengasas, 2 hingga 3 ayat, dalam kata-kata beliau sendiri.','Pesan singkat pendiri, 2 sampai 3 kalimat, dengan kata-kata beliau sendiri.','A short founder message, 2 to 3 sentences, in his own words.')}]</p></div><div style="border-radius:24px;overflow:hidden"><img src="{a('ph-jemaah.jpg')}" alt=""></div></div></section>
<section class="sec-sand"><div class="wrap"><div class="sec-head"><h2>{t('Perjalanan kami','Perjalanan kami','Our story')}</h2></div><div class="grid g4">{''.join(f'<div class="box"><b style="font-size:28px;color:#A6060F">{y}</b><p>{x}</p></div>' for y, x in ms)}</div></div></section>''' + cta(t('Kunjungi kami di Cianjur atau Melaka','Kunjungi kami di Cianjur atau Melaka','Visit us in Cianjur or Melaka'), t('Atau mulakan di WhatsApp.','Atau mulai lewat WhatsApp.','Or start on WhatsApp.'))
    return t('Tentang Kami','Tentang Kami','About'), '', body

def p_licence():
    items = [(t('Indonesia: PPIU dan PIHK','Indonesia: PPIU dan PIHK','Indonesia: PPIU and PIHK'), t('Lesen Kementerian Agama no. [NO.] untuk Umrah dan Haji Khusus.','Izin Kementerian Agama no. [NO.] untuk Umroh dan Haji Khusus.','Ministry of Religious Affairs licence no. [NO.] for Umrah and Hajj Khusus.')),
             (t('Malaysia: MOTAC','Malaysia: MOTAC','Malaysia: MOTAC'), t('Lesen agensi pelancongan dengan endorsmen Umrah, no. [NO.].','Izin agen perjalanan dengan endorsemen Umroh, no. [NO.].','Travel agency licence with Umrah endorsement, no. [NO.].')),
             (t('Akaun bank rasmi','Rekening resmi','Official bank accounts'), t('Bayar hanya ke akaun atas nama syarikat: [Bank, no. akaun]. Kami tidak pernah meminta bayaran ke akaun peribadi.','Bayar hanya ke rekening atas nama perusahaan: [Bank, no. rekening]. Kami tidak pernah meminta pembayaran ke rekening pribadi.','Pay only into accounts in the company’s name: [Bank, account no.]. We never ask for payment to a personal account.'))]
    body = page_hero(t('Lesen dan Bayaran','Izin dan Pembayaran','Licence and Payments'), t('Semak sebelum anda membayar','Cek sebelum Anda membayar','Check before you pay'), t('Penipuan Umrah memang berlaku. Ini cara anda pastikan Kurnia sah dan wang anda selamat.','Penipuan Umroh memang terjadi. Ini cara memastikan Kurnia resmi dan dana Anda aman.','Umrah fraud does happen. Here is how to make sure Kurnia is licensed and your money is safe.')) + f'<section><div class="wrap grid g3">{"".join(f"<div class=box>{CHECK}<h3 style=font-size:20px>{h}</h3><p>{b}</p></div>" for h, b in items)}</div></section><section class="sec-sand"><div class="wrap prose"><h2>{t("Cara menyemak","Cara mengecek","How to verify")}</h2><p>[{t("Langkah menyemak lesen di laman rasmi MOTAC dan Kementerian Agama, dengan pautan. Kurnia sahkan.","Langkah mengecek izin di situs resmi Kementerian Agama dan MOTAC, dengan tautan. Kurnia konfirmasi.","Steps to check the licence on the official MOTAC and Ministry sites, with links. To confirm with Kurnia.")}]</p></div></section>'
    return t('Lesen dan Bayaran','Izin dan Pembayaran','Licence and Payments'), '', body

def form_fields():
    return f'''<div class="grid g2"><label>{t('Nama penuh','Nama lengkap','Full name')}<input type="text" placeholder="{t('Seperti dalam pasport','Sesuai paspor','As in passport')}"></label><label>{t('Nombor WhatsApp','Nomor WhatsApp','WhatsApp number')}<input type="tel" placeholder="+60"></label></div>
<div class="grid g2"><label>{t('Pakej','Paket','Package')}<select>{''.join(f'<option>{p["name"]}</option>' for p in PKGS())}</select></label><label>{t('Bulan pilihan','Bulan pilihan','Preferred month')}<select><option>{t('Fleksibel','Fleksibel','Flexible')}</option><option>Rejab 1448</option><option>Syaaban 1448</option><option>Ramadan 1448</option></select></label></div>'''

def p_contact():
    body = page_hero(t('Hubungi','Kontak','Contact'), t('Mari rancang Umrah anda bersama','Mari rencanakan Umroh Anda bersama','Let’s plan your Umrah together'), t('Penasihat kami membalas dalam [N] jam bekerja.','Konsultan kami membalas dalam [N] jam kerja.','Our team replies within [N] working hours.')) + f'''<section><div class="wrap grid g2" style="align-items:start">
<div style="display:flex;flex-direction:column;gap:16px"><a class="btn btn-red" href="{WA}" style="justify-content:flex-start;min-height:64px">{WAICON} WhatsApp Malaysia · +60 17-611 2236</a><a class="btn btn-line" href="{WA}" style="justify-content:flex-start;min-height:64px">WhatsApp Indonesia · +62 857-2266-6585</a>
<div class="grid g2"><div class="box"><b>{t('Pejabat Malaysia','Kantor Malaysia','Malaysia office')}</b><p>[{t('No. unit','No. unit','Unit no.')}], Taman Tanjong Minyak Ria, Melaka</p><p class="muted">[{t('Waktu operasi','Jam operasional','Opening hours')}]</p></div><div class="box"><b>{t('Ibu pejabat Indonesia','Kantor pusat Indonesia','Indonesia head office')}</b><p>Jl. Raya Gading Asri No. 8, Cianjur</p><p class="muted">[{t('Waktu operasi','Jam operasional','Opening hours')}]</p></div></div></div>
<form class="box" onsubmit="return false"><h2 style="font-size:24px">{t('Pertanyaan','Pertanyaan','Enquiry')}</h2>{form_fields()}<label>{t('Mesej','Pesan','Message')}<textarea placeholder="{t('Bajet, tarikh atau soalan','Anggaran, tanggal atau pertanyaan','Budget, dates or questions')}"></textarea></label><label class="check"><input type="checkbox"> {t('Saya bersetuju Kurnia menghubungi saya tentang pertanyaan ini.','Saya setuju Kurnia menghubungi saya terkait pertanyaan ini.','I agree that Kurnia may contact me about this enquiry.')}</label><a class="btn btn-red" href="{u('thanks')}">{t('Hantar pertanyaan','Kirim pertanyaan','Send enquiry')}</a></form>
</div></section>'''
    return t('Hubungi','Kontak','Contact'), '', body

def p_register():
    body = page_hero(t('Daftar','Daftar','Register'), t('Daftar untuk tempat anda','Daftar untuk kursi Anda','Register for your seat'), t('Tiga langkah. Kami sahkan tempat anda melalui WhatsApp.','Tiga langkah. Kami konfirmasi kursi Anda lewat WhatsApp.','Three steps. We confirm your seat on WhatsApp.')) + f'''<section><div class="wrap" style="max-width:860px"><form class="box" onsubmit="return false">
<div class="steps"><span class="on">1. {t('Pakej','Paket','Package')}</span><span>2. {t('Maklumat jemaah','Data jamaah','Jemaah details')}</span><span>3. {t('Dokumen dan deposit','Dokumen dan DP','Documents and deposit')}</span></div>
{form_fields()}
<div class="grid g2"><label>{t('Bilangan dewasa','Jumlah dewasa','Adults')}<input type="number" value="2"></label><label>{t('Bilangan kanak-kanak','Jumlah anak','Children')}<input type="number" value="0"></label></div>
<label class="check"><input type="checkbox"> {t('Saya telah membaca Terma dan Dasar Pembatalan.','Saya telah membaca Syarat dan Kebijakan Pembatalan.','I have read the Terms and the Cancellation Policy.')}</label>
<a class="btn btn-red" href="{u('thanks')}">{t('Teruskan','Lanjutkan','Continue')}</a>
<p class="muted" style="font-size:13px">{t('Fasa 2: bayaran deposit dalam talian.','Fase 2: pembayaran DP online.','Phase 2: online deposit payment.')}</p></form></div></section>'''
    return t('Daftar','Daftar','Register'), '', body

def p_thanks():
    body = page_hero(t('Terima Kasih','Terima Kasih','Thank you'), t('Terima kasih, kami akan hubungi anda','Terima kasih, kami akan menghubungi Anda','Thank you, we will be in touch'), t('Mutawwif atau penasihat kami akan menghubungi anda melalui WhatsApp dalam [N] jam bekerja.','Muthawif atau konsultan kami akan menghubungi Anda via WhatsApp dalam [N] jam kerja.','A guide or advisor will contact you on WhatsApp within [N] working hours.')) + f'<section><div class="wrap btn-row"><a class="btn btn-red" href="{WA}">{t("WhatsApp kami sekarang","WhatsApp kami sekarang","WhatsApp us now")}</a><a class="btn btn-line" href="{u("stories")}">{t("Tengok kisah jemaah","Lihat kisah jamaah","Watch jemaah stories")}</a></div></section>'
    return t('Terima Kasih','Terima Kasih','Thank you'), '', body

def legal(title, note):
    body = page_hero(title, title, t('Draf. Teks muktamad daripada Kurnia dan penasihat undang-undang mereka.','Draf. Teks final dari Kurnia dan penasihat hukumnya.','Draft. Final wording to come from Kurnia and their legal adviser.')) + f'<section><div class="wrap prose"><p>[{note}]</p></div></section>'
    return title, '', body
def p_terms(): return legal(t('Terma dan Syarat','Syarat dan Ketentuan','Terms and Conditions'), t('Terma tempahan, bayaran, perubahan jadual dan tanggungjawab.','Ketentuan pemesanan, pembayaran, perubahan jadwal dan tanggung jawab.','Booking terms, payments, schedule changes and liability.'))
def p_privacy(): return legal(t('Dasar Privasi','Kebijakan Privasi','Privacy Policy'), t('Notis privasi selaras PDPA Malaysia dan UU PDP Indonesia.','Pemberitahuan privasi sesuai UU PDP Indonesia dan PDPA Malaysia.','Privacy notice in line with Malaysia’s PDPA and Indonesia’s PDP Law.'))
def p_cancel(): return legal(t('Pembatalan dan Bayaran Balik','Pembatalan dan Pengembalian Dana','Cancellation and Refunds'), t('Jadual bayaran balik mengikut tempoh sebelum berlepas.','Ketentuan pengembalian dana menurut waktu sebelum keberangkatan.','Refund schedule by time before departure.'))


def safar_url(lang_ar=False):
    return rel('safar-gifts/' + ('ar/' if lang_ar else ''))

def p_gifts():
    tiers = [('safar-sar3.jpg','SAR 3',t('Asas: Zamzam*, kurma','Dasar: Zamzam*, kurma','Basic: Zamzam*, dates')),('safar-sar10.jpg','SAR 10',t('Lengkap: Zamzam*, kurma, manisan, tasbih, kad doa','Lengkap: Zamzam*, kurma, manisan, tasbih, kartu doa','Complete: Zamzam*, dates, sweets, tasbih, dua card')),('safar-sar20.jpg','SAR 20',t('Premium: Zamzam* lebih besar dan tasbih premium','Premium: Zamzam* lebih besar dan tasbih premium','Premium: larger Zamzam* and premium tasbih'))]
    cards = ''.join(f'<div class="card"><div class="img"><img src="{a(i)}" alt="" loading="lazy"><span class="tag">{p_}</span></div><div class="body"><p>{d}</p></div></div>' for i, p_, d in tiers)
    body = page_hero(t('Hadiah Umrah','Oleh-oleh Umroh','Umrah Gifts'), t('Bawa pulang hadiah yang bermakna','Bawa pulang oleh-oleh yang bermakna','Bring home gifts that mean something'), t('Safar Gifts ialah jenama hadiah Umrah dan Haji daripada pasukan Kurnia. Pek kecil, mudah dibawa, siap untuk diberi.','Safar Gifts adalah merek oleh-oleh Umroh dan Haji dari tim Kurnia. Kemasan ringkas, mudah dibawa, siap dibagikan.','Safar Gifts is the Umrah and Hajj gift brand from the Kurnia team. Compact, easy to carry, ready to give.')) + f"""<section><div class="wrap grid g2" style="align-items:center"><div style="display:flex;flex-direction:column;gap:18px"><img src="{a('safar-logo.svg')}" alt="Safar Gifts by Kurnia Tour and Travel" style="height:64px;width:auto;align-self:flex-start"><h2 style="font-size:34px">{t('Hadiah untuk keluarga, rakan dan jiran','Oleh-oleh untuk keluarga, teman dan tetangga','Gifts for family, friends and neighbours')}</h2><p style="color:#48484C;font-size:17px">{t('Pilih dari SAR 3 hingga SAR 20 sebiji, dalam pek 10 atau 20. Boleh diambil di hotel anda di Makkah atau Madinah, atau dihantar sebelum berlepas.','Pilih mulai SAR 3 hingga SAR 20 per buah, dalam paket isi 10 atau 20. Bisa diambil di hotel Anda di Makkah atau Madinah, atau dikirim sebelum berangkat.','Choose from SAR 3 to SAR 20 per gift, in packs of 10 or 20. Collect at your hotel in Makkah or Madinah, or have them delivered before you fly.')}</p><div class="btn-row"><a class="btn btn-red" href="{safar_url()}">{t('Lawati kedai Safar Gifts','Kunjungi toko Safar Gifts','Visit the Safar Gifts shop')}</a><a class="btn btn-line" href="{safar_url()}bulk-orders/">{t('Tempahan kumpulan','Pesanan rombongan','Group orders')}</a></div></div><div style="border-radius:24px;overflow:hidden;border:1px solid #DEDCD8"><img src="{a('safar-hero.jpg')}" alt="{t('Pek hadiah Safar dalam empat kategori','Paket oleh-oleh Safar dalam empat kategori','Safar gift packs in four tiers')}"></div></div></section>
<section class="sec-sand"><div class="wrap"><div class="sec-head"><div><span class="eyebrow">{t('Kategori','Kategori','Tiers')}</span><h2>{t('Dari SAR 3 hingga SAR 20 sebiji','Mulai SAR 3 hingga SAR 20 per buah','From SAR 3 to SAR 20 per gift')}</h2></div></div><div class="grid g3">{cards}</div><p class="muted" style="margin-top:16px;font-size:14px">{t('*Zamzam tertakluk kepada kebenaran peraturan Arab Saudi. Kandungan dan harga ialah konsep awal.','*Zamzam tergantung izin regulasi Arab Saudi. Isi dan harga masih konsep awal.','*Zamzam is subject to Saudi regulatory approval. Contents and prices are initial concepts.')}</p></div></section>
<section style="padding-bottom:0"><div class="wrap"><div class="box" style="flex-direction:row;flex-wrap:wrap;align-items:center;gap:24px"><img src="{a('safar-gifts-qr.png')}" alt="{t('Kod QR ke kedai Safar Gifts','Kode QR ke toko Safar Gifts','QR code to the Safar Gifts shop')}" style="width:160px;height:160px;border-radius:12px"><div style="flex:1 1 280px"><h2 style="font-size:26px">{t('Imbas untuk membeli-belah','Pindai untuk berbelanja','Scan to shop')}</h2><p style="color:#48484C;margin-top:6px">{t('Kongsi dengan keluarga atau kumpulan anda, atau buka terus:','Bagikan ke keluarga atau rombongan Anda, atau buka langsung:','Share it with your family or group, or open it directly:')} <a href="{safar_url()}">mohd-suffian.github.io/kurnia-concept/safar-gifts</a></p></div></div></div></section>
<section><div class="wrap"><div class="cta" style="background:#1F4D3A"><div><h2>{t('Jemaah kumpulan Kurnia?','Jamaah rombongan Kurnia?','Travelling with a Kurnia group?')}</h2><p style="color:#D7E3DC">{t('Tanya mutawwif anda tentang tempahan hadiah untuk dihantar terus ke hotel kumpulan.','Tanyakan muthawif Anda soal pesanan oleh-oleh yang diantar langsung ke hotel rombongan.','Ask your guide about gift orders delivered straight to the group hotel.')}</p></div><a class="btn btn-white" style="color:#1F4D3A" href="{safar_url()}">{t('Lihat pek hadiah','Lihat paket oleh-oleh','See gift packs')}</a></div></div></section>"""
    return t('Hadiah Umrah','Oleh-oleh Umroh','Umrah Gifts'), '', body

PAGES = {'home': p_home, 'gifts': p_gifts, 'packages': p_packages, 'cat-umrah': p_cat_umrah, 'cat-plus': p_cat_plus, 'cat-haji': p_cat_haji,
         'pkg-madinah': p_pkg_madinah, 'pkg-aqsa': p_pkg_aqsa, 'pkg-haji': p_pkg_haji, 'guides': p_guides, 'guide': p_guide,
         'stories': p_stories, 'faq': p_faq, 'about': p_about, 'licence': p_licence, 'contact': p_contact, 'register': p_register,
         'thanks': p_thanks, 'terms': p_terms, 'privacy': p_privacy, 'cancel': p_cancel}

count = 0
for lang in LANGS:
    L = lang
    for key, fn in PAGES.items():
        CUR = path_of(key, lang)
        title, desc, body = fn()
        doc = head(key, title, desc or title) + header(key) + body + footer()
        d = os.path.join(OUT, CUR)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(doc)
        count += 1
# 404
L = 'bm'; CUR = ''
nf = head('home', '404', '404') + header('home') + page_hero('404', t('Halaman tidak dijumpai','',''), 'Page not found · Halaman tidak ditemukan') + f'<section><div class="wrap btn-row"><a class="btn btn-red" href="./">BM</a><a class="btn btn-line" href="id/">ID</a><a class="btn btn-line" href="en/">EN</a></div></section>' + footer()
open(os.path.join(OUT, '404.html'), 'w').write(nf)
open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
open(os.path.join(OUT, '.nojekyll'), 'w').write('')
print('pages', count)
