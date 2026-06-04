# -*- coding: utf-8 -*-
"""Patchuje pieseu/index.html: SEO head + JSON-LD, naprawia martwe linki,
podpina karty sklepu do podstron produktowych, dodaje baner cookies."""
import os, re

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(OUT, "index.html")
html = open(F, encoding="utf-8").read()

# ---------- 1. SEO head po <title> ----------
seo = '''
<meta name="description" content="pieseu - personalizowane suplementy dla psa w jednej miarce. Quiz dobiera skład pod wiek, wagę, rasę i potrzeby Twojego psa: stawy, trawienie, sierść, odporność, spokój, energia i serce. Polska produkcja, 90 dni gwarancji.">
<link rel="canonical" href="https://pieseu.pl/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#FDF9FF">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="pieseu">
<meta property="og:title" content="pieseu - Zdrowie psa, skrojone na miarę">
<meta property="og:description" content="Personalizowane suplementy dla psa w jednej miarce. Skład dobrany w 2-minutowym quizie pod Twojego psa.">
<meta property="og:url" content="https://pieseu.pl/">
<meta property="og:image" content="https://pieseu.pl/assets/img/odpornosc.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="pieseu - Zdrowie psa, skrojone na miarę">
<meta name="twitter:description" content="Personalizowane suplementy dla psa w jednej miarce.">
<meta name="twitter:image" content="https://pieseu.pl/assets/img/odpornosc.png">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"pieseu","url":"https://pieseu.pl/","email":"kontakt@pieseu.pl","description":"Personalizowane suplementy dla psów, dobierane indywidualnie pod wiek, wagę, rasę i potrzeby zwierzęcia.","areaServed":"PL","sameAs":["[FACEBOOK]","[INSTAGRAM]","[TIKTOK]"]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"pieseu","url":"https://pieseu.pl/","inLanguage":"pl-PL"}</script>'''
html = html.replace("<title>pieseu - Zdrowie psa, skrojone na miarę</title>",
                    "<title>pieseu - Zdrowie psa, skrojone na miarę</title>" + seo, 1)

# ---------- 2. nav: Sklep -> sklep.html ----------
html = html.replace('<nav class="navlinks"><a href="#jak">Jak to działa</a><a href="#sklep">Sklep</a>',
                    '<nav class="navlinks"><a href="#jak">Jak to działa</a><a href="sklep.html">Sklep</a>', 1)
html = html.replace('<a class="btn btn-ghost" href="#sklep" style="padding:11px 22px">Sklep</a>',
                    '<a class="btn btn-ghost" href="sklep.html" style="padding:11px 22px">Sklep</a>', 1)

# ---------- 3. karty gotowców -> podstrony produktowe (kolejno) ----------
targets = ["produkty/stawy-i-mobilnosc.html", "produkty/spokoj-i-wyciszenie.html", "produkty/trawienie-i-jelita.html"]
for t in targets:
    html = html.replace('<a class="pcard-btn" href="#produkt">Zobacz →</a>',
                        f'<a class="pcard-btn" href="{t}">Zobacz →</a>', 1)

# dodaj przycisk "wszystkie produkty" w bloku shop-divider
html = html.replace(
    '<p>Gotowe formuły na najczęstsze problemy - bez personalizacji, od ręki.</p>',
    '<p>Gotowe formuły na najczęstsze problemy - bez personalizacji, od ręki.</p>'
    '<a class="btn btn-dark" href="sklep.html" style="margin-top:14px">Zobacz wszystkie 7 formuł →</a>', 1)

# ---------- 4. footer: linki pomocnicze + prawne ----------
html = html.replace(
    '<div><h5>Pomoc</h5><a href="#">Kontakt</a><a href="#">FAQ</a><a href="#">Jak działa subskrypcja</a></div>',
    '<div><h5>Pomoc</h5><a href="#kontakt">Kontakt</a><a href="dostawa-i-zwroty.html">Dostawa i zwroty</a><a href="#cennik">Jak działa subskrypcja</a><a href="regulamin.html">Regulamin</a><a href="polityka-prywatnosci.html">Polityka prywatności</a><a href="polityka-cookies.html">Polityka cookies</a></div>', 1)
html = html.replace(
    '<div><h5>pieseu</h5><a href="#">Poznaj nas</a><a href="#">Opinie</a><a href="#">Program partnerski</a><a href="#">Program lojalnościowy</a></div>',
    '<div><h5>pieseu</h5><a href="#historia">Poznaj nas</a><a href="#opinie">Opinie</a><a href="sklep.html">Sklep</a><a href="#kontakt">Program partnerski</a></div>', 1)
html = html.replace(
    '<span>* na podstawie ankiet opiekunów (2025) · Regulamin · Polityka prywatności</span>',
    '<span>* dane poglądowe do uzupełnienia · <a href="regulamin.html" style="color:inherit">Regulamin</a> · <a href="polityka-prywatnosci.html" style="color:inherit">Polityka prywatności</a> · <a href="#" data-cookie-settings style="color:inherit">Ustawienia cookies</a></span>', 1)

# partner link (martwy plik) -> sekcja kontakt
html = html.replace('href="pieseu-partner.html"', 'href="#kontakt"')

# ---------- 5. baner cookies + wspólny JS przed </body> ----------
cookie = '''
<div class="ckb" id="ckb" role="dialog" aria-live="polite" aria-label="Zgoda na pliki cookies">
  <div class="ckb-txt">Używamy plików cookies, aby strona działała poprawnie, analizować ruch i personalizować treści. Szczegóły w <a href="polityka-cookies.html">Polityce cookies</a>.</div>
  <div class="ckb-btns"><button class="btn ckb-min" id="ckbSettings">Ustawienia</button><button class="btn ckb-min" id="ckbReject">Odrzuć</button><button class="btn btn-primary" id="ckbAccept">Akceptuję wszystkie</button></div>
</div>
<div class="ck-modal" id="ckModal" role="dialog" aria-modal="true" aria-label="Ustawienia cookies">
  <div class="ck-card">
    <h3>Ustawienia prywatności</h3>
    <p class="intro">Zarządzaj zgodami. Cookies niezbędne są zawsze aktywne, bo bez nich strona nie działa.</p>
    <div class="ck-row"><div class="ci"><b>Niezbędne</b><p>Konieczne do działania sklepu, koszyka i bezpieczeństwa.</p></div><label class="ck-sw"><input type="checkbox" checked disabled><span class="sl"></span></label></div>
    <div class="ck-row"><div class="ci"><b>Analityczne</b><p>Statystyki ruchu (np. Google Analytics) - pomagają ulepszać stronę.</p></div><label class="ck-sw"><input type="checkbox" id="ckAnalytics"><span class="sl"></span></label></div>
    <div class="ck-row"><div class="ci"><b>Marketingowe</b><p>Remarketing i dopasowane reklamy (np. Meta, Google Ads).</p></div><label class="ck-sw"><input type="checkbox" id="ckMarketing"><span class="sl"></span></label></div>
    <div class="ck-acts"><button class="btn btn-ghost" id="ckSave">Zapisz wybór</button><button class="btn btn-primary" id="ckAcceptAll">Akceptuję wszystkie</button></div>
  </div>
</div>
<link rel="stylesheet" href="assets/css/pieseu.css">
<script src="assets/js/pieseu.js" defer></script>
</body>'''
html = html.replace("</body>", cookie, 1)

open(F, "w", encoding="utf-8").write(html)
print("patched index.html; remaining #produkt:", html.count('href="#produkt"'))
print("cookie banner present:", 'id="ckb"' in html)
print("ld+json blocks:", html.count("application/ld+json"))
