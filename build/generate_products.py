# -*- coding: utf-8 -*-
"""Generator podstron produktowych pieseu + katalogu.
Uruchom: python3 build/generate_products.py  (z katalogu pieseu/)
Dane firmy to PLACEHOLDERY do podmiany.
"""
import os, json

SITE = "https://pieseu.pl"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # pieseu/

# ---- wspólne dane firmy (PLACEHOLDERY) ----
COMPANY = "pieseu sp. z o.o."
EMAIL = "kontakt@pieseu.pl"

WEIGHT_TIERS = ["do 5 kg", "5-10 kg", "10-15 kg", "15-25 kg", "25-30 kg", "30-40 kg", "powyżej 40 kg"]

DOSE_ROWS = [
    ("do 5 kg", "1/2 miarki (≈1,5 g)"),
    ("5-10 kg", "1 miarka (≈3 g)"),
    ("10-20 kg", "1,5 miarki (≈4,5 g)"),
    ("20-30 kg", "2 miarki (≈6 g)"),
    ("30-40 kg", "2,5 miarki (≈7,5 g)"),
    ("powyżej 40 kg", "3 miarki (≈9 g)"),
]

# kolory wg palety :root
PRODUCTS = [
    {
        "slug": "trawienie-i-jelita", "name": "Psi Brzuch", "concern": "Trawienie i jelita",
        "panel": "var(--lav-soft)", "acc": "var(--lav)",
        "price": "69",
        "default_tier": "do 5 kg",
        "tagline": "Zdrowe trawienie i równowaga jelit",
        "lead": "Spersonalizowana mieszanka, która wspiera mikroflorę jelit, łagodzi wzdęcia i pomaga uregulować wypróżnienia. Dosypujesz jedną miarkę do karmy - smakuje jak nagroda.",
        "bullets": ["Zdrowe, regularne trawienie", "Równowaga mikroflory jelit", "Redukcja wzdęć i dyskomfortu"],
        "tldr": ["Probiotyk + prebiotyk + enzymy w jednej miarce", "Dla psów z wrażliwym brzuchem i po antybiotykoterapii", "30 porcji · proszek · od 69 zł/mies."],
        "ingredients": [
            ("Probiotyk (5 mld CFU)", "100 mg", "Odbudowa i równowaga mikroflory jelitowej."),
            ("Inulina (prebiotyk)", "300 mg", "Pożywka dla dobrych bakterii - wspiera florę jelit."),
            ("Enzymy trawienne", "80 mg", "Lepsze wykorzystanie składników z karmy."),
            ("Siemię lniane", "250 mg", "Błonnik i śluzy łagodzące ścianę jelit."),
            ("Dynia (błonnik)", "200 mg", "Reguluje konsystencję stolca."),
            ("Imbir", "40 mg", "Wspomaga trawienie i łagodzi mdłości."),
        ],
        "signs": ["wrażliwy brzuch", "wzdęcia i gazy", "luźne stolce", "po antybiotyku", "zmiana karmy", "częste przekąski"],
        "med": False,
        "faq": [
            ("Po jakim czasie zobaczę poprawę trawienia?", "Część psów reaguje już po 1-2 tygodniach (mniej gazów, bardziej regularne wypróżnienia). Pełna odbudowa mikroflory zwykle zajmuje 4-8 tygodni regularnego stosowania."),
            ("Czy mogę podawać przy biegunce?", "Tak, probiotyk i błonnik pomagają ustabilizować pracę jelit. Jeśli biegunka trwa dłużej niż 48 h, jest krwista lub towarzyszą jej wymioty, skontaktuj się z weterynarzem."),
            ("Czy łączy się z karmą na wrażliwy żołądek?", "Tak. To dodatek do karmy (meal topper), nie zastępuje diety. Można podawać razem z karmą weterynaryjną."),
        ],
    },
    {
        "slug": "spokoj-i-wyciszenie", "name": "Psi Spokój", "concern": "Spokój i wyciszenie",
        "panel": "#F6E9DC", "acc": "#E0A878",
        "price": "69",
        "default_tier": "5-10 kg",
        "tagline": "Wsparcie w stresie i codzienny spokój",
        "lead": "Naturalna mieszanka, która pomaga psu wyciszyć się bez otępienia - przy lęku separacyjnym, hałasach, podróżach i nadpobudliwości. Spokojniejsze spacery i lepszy sen.",
        "bullets": ["Wsparcie w stresie i lęku", "Spokojniejsze spacery", "Codzienny komfort i lepszy sen"],
        "tldr": ["L-tryptofan + melisa + L-teanina - wyciszenie bez otępienia", "Na burze, fajerwerki, podróże i lęk separacyjny", "30 porcji · proszek · od 69 zł/mies."],
        "ingredients": [
            ("L-tryptofan", "120 mg", "Prekursor serotoniny - wspiera spokój i nastrój."),
            ("Melisa lekarska", "150 mg", "Łagodzi napięcie i ułatwia wyciszenie."),
            ("L-teanina", "60 mg", "Relaks bez senności i otępienia."),
            ("Rumianek", "100 mg", "Działanie kojące na układ nerwowy i trawienie."),
            ("Magnez", "40 mg", "Wspiera pracę układu nerwowego i mięśni."),
            ("Witaminy z grupy B", "15 mg", "Wsparcie układu nerwowego pod obciążeniem stresem."),
        ],
        "signs": ["lęk separacyjny", "burze i fajerwerki", "nadpobudliwość", "podróże autem", "wizyty u weterynarza", "problemy ze snem"],
        "med": True,
        "faq": [
            ("Czy mój pies będzie osowiały?", "Nie. Składniki wspierają naturalne wyciszenie, nie usypiają i nie otępiają. Pies pozostaje aktywny, ale spokojniejszy."),
            ("Kiedy podać przed stresującym wydarzeniem?", "Najlepsze efekty daje regularne stosowanie. Przed jednorazowym wydarzeniem (np. fajerwerki) zacznij 5-7 dni wcześniej."),
            ("Czy to bezpieczne na co dzień?", "Tak, mieszanka jest pomyślana do codziennego stosowania. Przy silnym lęku lub agresji skonsultuj się z weterynarzem lub behawiorystą - suplement wspiera, ale nie zastępuje terapii."),
        ],
    },
    {
        "slug": "siersc-i-skora", "name": "Psia Sierść", "concern": "Sierść i skóra",
        "panel": "var(--pink-soft)", "acc": "var(--pink)",
        "price": "69",
        "default_tier": "10-15 kg",
        "tagline": "Zdrowa skóra i lśniąca sierść",
        "lead": "Omega-3, biotyna i cynk w skutecznych dawkach - na matową sierść, świąd, suchą skórę i nadmierne linienie. Efekt na sierści widać zwykle po 6-8 tygodniach.",
        "bullets": ["Zdrowa, nawilżona skóra", "Lśniąca, mocna sierść", "Mniejsze linienie"],
        "tldr": ["Omega-3 + biotyna + cynk - fundament zdrowej sierści", "Na świąd, łupież, matową sierść i linienie", "30 porcji · proszek · od 69 zł/mies."],
        "ingredients": [
            ("Omega-3 (olej z łososia)", "600 mg", "EPA i DHA - nawilżenie skóry i połysk sierści."),
            ("Biotyna", "0,2 mg", "Buduje keratynę - mocniejsza sierść i pazury."),
            ("Cynk chelatowany", "15 mg", "Regeneracja skóry i bariery naskórkowej."),
            ("Witamina E", "30 mg", "Antyoksydant chroniący komórki skóry."),
            ("Kwas linolowy (GLA)", "120 mg", "Wspiera elastyczność i nawilżenie skóry."),
            ("Drożdże piwne", "150 mg", "Naturalne źródło witamin z grupy B dla sierści."),
        ],
        "signs": ["matowa sierść", "nadmierne linienie", "świąd i drapanie", "sucha skóra / łupież", "łamliwe pazury", "po zmianie sezonu"],
        "med": False,
        "faq": [
            ("Kiedy zobaczę różnicę na sierści?", "Sierść rośnie powoli - pierwsze efekty (mniej drapania, lepsze nawilżenie skóry) bywają widoczne po 3-4 tygodniach, a wyraźny połysk i mniejsze linienie zwykle po 6-8 tygodniach."),
            ("Czy pomaga przy alergii skórnej?", "Omega-3 wspiera barierę skórną i działa przeciwzapalnie, co łagodzi objawy. Przy zdiagnozowanej alergii suplement jest uzupełnieniem leczenia weterynaryjnego, nie jego zamiennikiem."),
            ("Czy nie zaszkodzi przy zdrowej sierści?", "Nie - to profilaktyka. Składniki wspierają kondycję skóry i sierści także u zdrowych psów, zwłaszcza w okresie linienia."),
        ],
    },
    {
        "slug": "odpornosc", "name": "Psia Odporność", "concern": "Odporność",
        "panel": "var(--mint-soft)", "acc": "var(--mint)",
        "price": "69",
        "default_tier": "15-25 kg",
        "tagline": "Silny układ odpornościowy i witalność",
        "lead": "Beta-glukany, witaminy i przeciwutleniacze wspierające naturalną odporność psa - w sezonie infekcji, w rekonwalescencji i u seniorów. Ochrona komórek i codzienna energia.",
        "bullets": ["Silniejszy układ odpornościowy", "Ochrona komórek przed stresem oksydacyjnym", "Witalność i energia"],
        "tldr": ["Beta-glukany + wit. C/E + cynk i selen", "Na sezon infekcji, rekonwalescencję i seniorów", "30 porcji · proszek · od 69 zł/mies."],
        "ingredients": [
            ("Beta-glukany", "150 mg", "Aktywują naturalne mechanizmy odpornościowe."),
            ("Witamina C", "80 mg", "Wspiera komórki odpornościowe i regenerację."),
            ("Witamina E", "30 mg", "Antyoksydant chroniący błony komórkowe."),
            ("Cynk + selen", "16 mg", "Minerały kluczowe dla odporności."),
            ("Jeżówka (echinacea)", "100 mg", "Tradycyjne wsparcie odporności sezonowej."),
            ("Probiotyk", "100 mg", "70% odporności mieszka w jelitach - wspieramy florę."),
        ],
        "signs": ["sezon jesienno-zimowy", "częste infekcje", "rekonwalescencja", "pies senior", "spadek formy", "okres szczepień"],
        "med": False,
        "faq": [
            ("Kiedy najlepiej zacząć?", "Profilaktycznie przed sezonem infekcji (jesień) lub w okresach większego obciążenia: rekonwalescencja, stres, podróże. Działanie immunomodulujące buduje się stopniowo, w ciągu kilku tygodni."),
            ("Czy podawać przez cały rok?", "Można. Beta-glukany i probiotyk są bezpieczne do długotrwałego stosowania. U seniorów i psów osłabionych zalecamy podawanie ciągłe."),
            ("Czy zastąpi szczepienia?", "Nie. Suplement wspiera naturalną odporność, ale nie zastępuje szczepień ani opieki weterynaryjnej."),
        ],
    },
    {
        "slug": "stawy-i-mobilnosc", "name": "Psi Ruch", "concern": "Stawy i mobilność",
        "panel": "#F1E7D6", "acc": "#C9A05B",
        "price": "79",
        "default_tier": "25-30 kg",
        "tagline": "Wsparcie stawów i swoboda ruchu",
        "lead": "Pełen kompleks na stawy: glukozamina, chondroityna, MSM, kolagen i kurkumina. Dla dużych ras, psów aktywnych, sportowych i seniorów - mniej sztywności, więcej radości z ruchu.",
        "bullets": ["Wsparcie stawów i chrząstki", "Lepsza ruchomość i elastyczność", "Komfort po wysiłku i u seniora"],
        "tldr": ["Glukozamina + chondroityna + MSM + kolagen", "Dla dużych ras, psów aktywnych i seniorów", "30 porcji · proszek · od 79 zł/mies."],
        "ingredients": [
            ("Glukozamina", "500 mg", "Budulec chrząstki stawowej."),
            ("Chondroityna", "300 mg", "Wspiera elastyczność i amortyzację stawu."),
            ("MSM", "250 mg", "Siarka organiczna - komfort i mniejsze napięcie."),
            ("Kolagen morski", "350 mg", "Elastyczność ścięgien i więzadeł."),
            ("Kurkumina", "120 mg", "Naturalne wsparcie przeciwzapalne."),
            ("Omega-3 + kwas hialuronowy", "400 mg", "Nawilżenie stawu i działanie kojące."),
        ],
        "signs": ["sztywność po odpoczynku", "niechęć do skoków i schodów", "duże rasy", "psy sportowe i aktywne", "pies senior", "po kontuzji"],
        "med": True,
        "faq": [
            ("Jak szybko działa na stawy?", "Stawy regenerują się powoli - pierwsze sygnały (chętniejsze wstawanie, mniej sztywności rano) zwykle po 3-4 tygodniach, a pełny efekt budulcowy po ok. 90 dniach regularnego stosowania."),
            ("Dla seniora czy dla młodego, aktywnego psa?", "Dla obu. U seniorów łagodzi sztywność, u psów aktywnych i sportowych działa profilaktycznie, chroniąc chrząstkę przed przeciążeniem."),
            ("Czy zastąpi leczenie przy zwyrodnieniu stawów?", "Nie. Przy zdiagnozowanej chorobie zwyrodnieniowej lub dysplazji suplement jest wsparciem terapii ustalonej przez weterynarza, nie jej zamiennikiem."),
        ],
    },
    {
        "slug": "psi-balans", "name": "Psi Balans", "concern": "Codzienna równowaga",
        "panel": "var(--blue-soft)", "acc": "#5BA8E0",
        "price": "79",
        "default_tier": "10-15 kg",
        "tagline": "Codzienna równowaga i dobra forma",
        "lead": "Wszechstronne wsparcie na każdy dzień - równowaga odporności, trawienia i układu nerwowego w jednej miarce. Dla psów, które potrzebują ogólnego wzmocnienia i stabilnej formy przez cały rok.",
        "bullets": ["Codzienna równowaga organizmu", "Wsparcie odporności i trawienia", "Stabilna forma i samopoczucie"],
        "tldr": ["Witaminy + probiotyk + omega-3 + adaptogeny", "Ogólne wsparcie na co dzień, dla każdego psa", "30 porcji · proszek · od 79 zł/mies."],
        "ingredients": [
            ("Kompleks witamin (A, D, E, B)", "25 mg", "Pokrywa codzienne potrzeby i uzupełnia dietę."),
            ("Probiotyk (3 mld CFU)", "100 mg", "Równowaga jelit i wsparcie odporności."),
            ("Omega-3 (olej z łososia)", "400 mg", "Skóra, sierść, stawy i serce - wszechstronnie."),
            ("Magnez", "40 mg", "Spokojny układ nerwowy i praca mięśni."),
            ("Ashwagandha (adaptogen)", "80 mg", "Pomaga organizmowi radzić sobie ze stresem."),
            ("Mikroelementy (cynk, selen)", "16 mg", "Wsparcie odporności i regeneracji."),
        ],
        "signs": ["ogólne wzmocnienie", "pies w słabszej formie", "rekonwalescencja", "zmiana sezonu", "wsparcie na co dzień", "młode i seniory"],
        "med": False,
        "faq": [
            ("Czym różni się Psi Balans od pozostałych formuł?", "To wszechstronne wsparcie ogólne - łączy podstawy odporności, trawienia i kondycji w jednej miarce. Gdy pies nie ma jednego konkretnego problemu, a chcesz po prostu wzmocnić go na co dzień, to dobry wybór."),
            ("Dla jakiego psa się nadaje?", "Dla każdego - młodego, dorosłego i seniora. To bezpieczna, codzienna baza; przy konkretnym wyzwaniu (np. stawy, skóra) warto wybrać formułę dedykowaną albo dobrać skład w quizie."),
            ("Czy mogę podawać przez cały rok?", "Tak, Psi Balans jest pomyślany do codziennego, całorocznego stosowania jako ogólne wsparcie."),
        ],
    },
]


def crumbs(base, name):
    return (f'<nav class="crumbs wrap" aria-label="Okruszki">'
            f'<a href="{base}index.html">Start</a><span>›</span>'
            f'<a href="{base}sklep.html">Sklep</a><span>›</span><b>{name}</b></nav>')


def header(base):
    return f'''<header>
  <div class="wrap nav">
    <a class="logo" href="{base}index.html" aria-label="pieseu - strona główna">
      <span class="brand-word">pieseu<svg class="paw" viewBox="0 0 24 24"><circle cx="6" cy="9" r="2.3"/><circle cx="11.5" cy="6.4" r="2.3"/><circle cx="17" cy="9" r="2.3"/><ellipse cx="11.5" cy="15.5" rx="5" ry="4.3"/></svg></span>
    </a>
    <nav class="navlinks">
      <a href="{base}index.html#jak">Jak to działa</a>
      <a href="{base}sklep.html">Sklep</a>
      <a href="{base}index.html#sklad">Skład</a>
      <a href="{base}index.html#opinie">Opinie</a>
      <a href="{base}index.html#cennik">Subskrypcja</a>
    </nav>
    <div class="navcta">
      <a class="btn btn-ghost" href="{base}sklep.html" style="padding:11px 22px">Sklep</a>
      <a class="btn btn-primary" href="{base}index.html#quiz" style="padding:11px 24px">Stwórz mieszankę</a>
    </div>
  </div>
</header>'''


def footer(base):
    return f'''<section class="partner-foot">
  <div class="wrap partner-foot-in">
    <div><b>Pracujesz z psami albo masz zasięgi?</b><span>Polecaj pieseu i zarabiaj do 20% prowizji - w gotówce lub Łapkach do wydania w sklepie.</span></div>
    <a class="btn btn-ghost" href="{base}index.html#kontakt">Program partnerski →</a>
  </div>
</section>
<footer id="kontakt">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-logo"><span class="brand-word">pieseu<svg class="paw" viewBox="0 0 24 24"><circle cx="6" cy="9" r="2.3"/><circle cx="11.5" cy="6.4" r="2.3"/><circle cx="17" cy="9" r="2.3"/><ellipse cx="11.5" cy="15.5" rx="5" ry="4.3"/></svg></span></div>
        <p style="font-size:14px;opacity:.8;line-height:1.6;max-width:260px;font-weight:600">Personalizowane suplementy dopasowane do potrzeb Twojego psa.</p>
      </div>
      <div><h5>Sklep</h5>
        <a href="{base}sklep.html">Wszystkie produkty</a>
        <a href="{base}produkty/stawy-i-mobilnosc.html">Psi Ruch</a>
        <a href="{base}produkty/trawienie-i-jelita.html">Psi Brzuch</a>
        <a href="{base}produkty/siersc-i-skora.html">Psia Sierść</a>
      </div>
      <div><h5>Pomoc</h5>
        <a href="{base}dostawa-i-zwroty.html">Dostawa i zwroty</a>
        <a href="{base}index.html#kontakt">Kontakt</a>
        <a href="{base}regulamin.html">Regulamin</a>
        <a href="{base}polityka-prywatnosci.html">Polityka prywatności</a>
        <a href="{base}polityka-cookies.html">Polityka cookies</a>
      </div>
      <div class="foot-news"><h5>Newsletter - 10% na start</h5><input type="email" placeholder="Twój e-mail" aria-label="Twój e-mail"><button class="btn btn-primary" style="width:100%">Odbierz rabat</button></div>
    </div>
    <div class="foot-bottom"><span>© 2026 {COMPANY} · pieseu.pl</span><span>* dane firmy do uzupełnienia · <a href="{base}regulamin.html" style="color:inherit">Regulamin</a> · <a href="{base}polityka-prywatnosci.html" style="color:inherit">Polityka prywatności</a></span></div>
  </div>
</footer>
{cookie_banner(base)}
<script src="{base}assets/js/pieseu.js" defer></script>'''


def cookie_banner(base):
    return f'''<div class="ckb" id="ckb" role="dialog" aria-live="polite" aria-label="Zgoda na pliki cookies">
  <div class="ckb-txt">Używamy plików cookies, aby strona działała poprawnie, analizować ruch i personalizować treści. Szczegóły w <a href="{base}polityka-cookies.html">Polityce cookies</a>.</div>
  <div class="ckb-btns">
    <button class="btn ckb-min" id="ckbSettings">Ustawienia</button>
    <button class="btn ckb-min" id="ckbReject">Odrzuć</button>
    <button class="btn btn-primary" id="ckbAccept">Akceptuję wszystkie</button>
  </div>
</div>
<div class="ck-modal" id="ckModal" role="dialog" aria-modal="true" aria-label="Ustawienia cookies">
  <div class="ck-card">
    <h3>Ustawienia prywatności</h3>
    <p class="intro">Zarządzaj zgodami. Cookies niezbędne są zawsze aktywne, bo bez nich strona nie działa.</p>
    <div class="ck-row"><div class="ci"><b>Niezbędne</b><p>Konieczne do działania sklepu, koszyka i bezpieczeństwa.</p></div><label class="ck-sw"><input type="checkbox" checked disabled><span class="sl"></span></label></div>
    <div class="ck-row"><div class="ci"><b>Analityczne</b><p>Statystyki ruchu (np. Google Analytics) - pomagają ulepszać stronę.</p></div><label class="ck-sw"><input type="checkbox" id="ckAnalytics"><span class="sl"></span></label></div>
    <div class="ck-row"><div class="ci"><b>Marketingowe</b><p>Remarketing i dopasowane reklamy (np. Meta, Google Ads).</p></div><label class="ck-sw"><input type="checkbox" id="ckMarketing"><span class="sl"></span></label></div>
    <div class="ck-acts">
      <button class="btn btn-ghost" id="ckSave">Zapisz wybór</button>
      <button class="btn btn-primary" id="ckAcceptAll">Akceptuję wszystkie</button>
    </div>
  </div>
</div>'''


def head(title, desc, canonical, og_img):
    return f'''<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#FDF9FF">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="pieseu">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_img}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;500;600;700;800&family=Nunito:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@700&display=swap" rel="stylesheet">'''


def build_product(p):
    base = "../"
    slug = p["slug"]
    url = f"{SITE}/produkty/{slug}.html"
    img = f"{SITE}/assets/img/{slug}.png"
    title = f"{p['name']} - suplement dla psa | pieseu"
    desc = (p["lead"][:155]).rsplit(" ", 1)[0] + "…"

    # bullets
    bul = "".join(
        f'<div class="b"><span class="bi"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg></span>{b}</div>'
        for b in p["bullets"]
    )
    tldr = "".join(f"<li>{t}</li>" for t in p["tldr"])
    # weight selector
    wsel = "".join(
        f'<button type="button" class="{"on" if t==p["default_tier"] else ""}" data-tier="{t}">{t}</button>'
        for t in WEIGHT_TIERS
    )
    # ingredients
    ingr = "".join(
        f'<div class="row"><div class="t"><b>{n}</b><span class="d">{d}</span></div><p>{desc_}</p></div>'
        for (n, d, desc_) in p["ingredients"]
    )
    signs = "".join(f'<span class="s">{s}</span>' for s in p["signs"])
    dose = "".join(f"<tr><td><b>{w}</b></td><td>{d}</td></tr>" for (w, d) in DOSE_ROWS)
    faq_html = "".join(
        f'<div class="faq-item{" open" if i==0 else ""}"><div class="faq-q">{q}<span class="ic">+</span></div><div class="faq-a"><p>{a}</p></div></div>'
        for i, (q, a) in enumerate(p["faq"])
    )

    med = ""
    if p["med"]:
        med = '''<div class="mednote" style="margin-top:22px"><svg viewBox="0 0 24 24"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg><div><b>Ważne:</b> Suplement diety dla psów. Nie zastępuje zbilansowanej diety ani leczenia weterynaryjnego. Przy objawach chorobowych lub przyjmowaniu leków skonsultuj się z lekarzem weterynarii.</div></div>'''

    # related (other products)
    rel_cards = ""
    for r in PRODUCTS:
        if r["slug"] == slug:
            continue
        rel_cards += (
            f'<div class="pcard" style="--panel:{r["panel"]};--acc:{r["acc"]}">'
            f'<a class="pcard-link" href="{r["slug"]}.html">'
            f'<div class="pcard-top" style="background:#F3EDF1;padding:0;min-height:0"><img src="../assets/img/{r["slug"]}.png" alt="Opakowanie pieseu {r["name"]}" style="width:100%;height:auto;display:block"></div>'
            f'<div class="pcard-body"><h4>{r["name"]}</h4><div class="pcard-foot"><span class="pr">od {r["price"]} zł <small>/ mies.</small></span><span class="pcard-btn">Zobacz →</span></div></div>'
            f'</a></div>'
        )
        if rel_cards.count("pcard-link") >= 4:
            break

    # JSON-LD
    ld_product = {
        "@context": "https://schema.org/",
        "@type": "Product",
        "name": f"pieseu {p['name']} - suplement dla psa",
        "image": [img],
        "description": p["lead"],
        "brand": {"@type": "Brand", "name": "pieseu"},
        "category": "Suplementy i karma dla psów",
        "audience": {"@type": "Audience", "audienceType": "Opiekunowie psów"},
        # aggregateRating / review CELOWO pominięte - dodać po zebraniu realnych opinii
        "offers": {
            "@type": "Offer",
            "url": url,
            "priceCurrency": "PLN",
            "price": p["price"],
            "priceValidUntil": "2026-12-31",
            "availability": "https://schema.org/InStock",
            "seller": {"@type": "Organization", "name": "pieseu"},
        },
    }
    ld_faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for (q, a) in p["faq"]
        ],
    }
    ld_bc = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Sklep", "item": f"{SITE}/sklep.html"},
            {"@type": "ListItem", "position": 3, "name": p["name"], "item": url},
        ],
    }
    ld = "\n".join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
        for x in (ld_product, ld_faq, ld_bc)
    )

    html = f'''{head(title, desc, url, img)}
{ld}
<link rel="stylesheet" href="../assets/css/pieseu.css">
<style>:root{{--acc:{p['acc']};--panel:{p['panel']}}}</style>
</head>
<body>
{header(base)}
{crumbs(base, p['name'])}

<section class="pdp-hero">
  <div class="wrap pdp-grid">
    <div class="pdp-media" style="background:{p['panel']}">
      <img src="../assets/img/{slug}.png" alt="Opakowanie pieseu {p['name']} - spersonalizowana mieszanka dla psa, 30 porcji, proszek" width="360" height="450">
    </div>
    <div>
      <div class="eyebrow pdp-eyebrow">{p['concern']} · suplement dla psa</div>
      <h1>{p['name']}</h1>
      <p class="pdp-lead">{p['lead']}</p>
      <div class="pdp-tldr">
        <h2>Najważniejsze w skrócie</h2>
        <ul>{tldr}</ul>
      </div>
      <div class="pdp-bul">{bul}</div>

      <div class="pdp-buy">
        <div class="pdp-price"><span class="now">od {p['price']} zł</span><span class="per">/ miesiąc · 30 porcji</span><span class="tag">Subskrypcja −20%</span></div>
        <div class="pdp-meta">Proszek · 1 miarka dziennie do karmy · anulujesz kiedy chcesz</div>
        <div class="pdp-sel-lab">Waga psa (dawkowanie)</div>
        <div class="wsel" id="wsel">{wsel}</div>
        <a class="btn btn-flow" href="{base}index.html#quiz">Dobierz w quizie - 2 min →</a>
        <a class="btn btn-ghost" href="{base}index.html#cennik">Kup jako gotowiec →</a>
        <div class="pdp-trust"><span>90 dni gwarancji</span><span>Darmowa dostawa od 149 zł</span><span>Polska produkcja</span><span>Bez GMO</span></div>
      </div>
    </div>
  </div>
</section>

<section class="pdp-sec sec-lav" style="--panel:{p['panel']}">
  <div class="wrap">
    <h2>Co dokładnie jest w jednej miarce?</h2>
    <p class="sub">Pełna transparentność - każdy składnik i jego dawka. Przykładowy skład formuły „{p['name']}”; ostateczne ilości dobieramy pod wagę i potrzeby Twojego psa w quizie.</p>
    <div class="ingr-table">{ingr}</div>
    {med}
  </div>
</section>

<section class="pdp-sec">
  <div class="wrap">
    <h2>Dla jakiego psa?</h2>
    <p class="sub">Formułę „{p['name']}” warto rozważyć, gdy widzisz u psa m.in.:</p>
    <div class="signs">{signs}</div>
  </div>
</section>

<section class="pdp-sec sec-mint">
  <div class="wrap">
    <h2>Jak dawkować</h2>
    <p class="sub">Jedna miarka dziennie, dosypana do karmy. Dawkę dobieramy do masy ciała psa:</p>
    <table class="dose-table">
      <thead><tr><th>Masa ciała psa</th><th>Dawka dzienna</th></tr></thead>
      <tbody>{dose}</tbody>
    </table>
    <p class="note" style="margin-top:14px">Wartości orientacyjne. Dokładną dawkę i skład ustalamy indywidualnie w quizie - pod wiek, wagę, rasę i wyzwania Twojego psa.</p>
  </div>
</section>

<section class="pdp-sec">
  <div class="wrap" style="max-width:820px">
    <h2>Najczęstsze pytania</h2>
    <div class="faq" style="margin-top:20px">{faq_html}</div>
  </div>
</section>

<section class="pdp-sec sec-pink">
  <div class="wrap">
    <h2>Inne formuły pieseu</h2>
    <p class="sub">Twój pies ma więcej niż jedną potrzebę? W quizie łączymy obszary w jednej miarce.</p>
    <div class="rel-grid">{rel_cards}</div>
  </div>
</section>

{footer(base)}
</body>
</html>'''

    path = os.path.join(OUT, "produkty", f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


def build_catalog():
    base = ""
    cards = ""
    for p in PRODUCTS:
        cards += (
            f'<div class="pcard" style="--panel:{p["panel"]};--acc:{p["acc"]}">'
            f'<a class="pcard-link" href="produkty/{p["slug"]}.html">'
            f'<div class="pcard-top" style="background:#F3EDF1;padding:0;min-height:0"><img src="assets/img/{p["slug"]}.png" alt="Opakowanie pieseu {p["name"]} - suplement dla psa, 30 porcji" style="width:100%;height:auto;display:block"></div>'
            f'<div class="pcard-body"><h4>{p["name"]}</h4><p>{p["tagline"]}.</p>'
            f'<div class="pcard-feat"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>30 porcji · proszek</div>'
            f'<div class="pcard-foot"><span class="pr">od {p["price"]} zł <small>/ mies.</small></span><span class="pcard-btn">Zobacz →</span></div>'
            f'</div></a></div>'
        )

    url = f"{SITE}/sklep.html"
    title = "Sklep - suplementy dla psa skrojone na miarę | pieseu"
    desc = "Gotowe formuły pieseu na konkretne potrzeby psa: stawy, trawienie, sierść, odporność, spokój, energia i serce. Albo stwórz mieszankę uszytą na miarę w 2-minutowym quizie."
    img = f"{SITE}/assets/img/stawy-i-mobilnosc.png"

    ld_items = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Suplementy pieseu dla psów",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "url": f"{SITE}/produkty/{p['slug']}.html", "name": p["name"]}
            for i, p in enumerate(PRODUCTS)
        ],
    }
    ld_bc = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Start", "item": f"{SITE}/"},
            {"@type": "ListItem", "position": 2, "name": "Sklep", "item": url},
        ],
    }
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in (ld_items, ld_bc))

    html = f'''{head(title, desc, url, img)}
{ld}
<link rel="stylesheet" href="assets/css/pieseu.css">
</head>
<body>
{header(base)}
<section class="cat-hero">
  <div class="wrap">
    <div class="eyebrow" style="justify-content:center">Sklep pieseu</div>
    <h1>Czego potrzebuje Twój pies?</h1>
    <p>Najlepszy efekt daje mieszanka skrojona na miarę w quizie - to nasz bestseller. Wolisz gotowca? Wybierz formułę na konkretną potrzebę.</p>
    <div style="margin-top:24px"><a class="btn btn-flow" href="index.html#quiz">Stwórz mieszankę - 2 min →</a></div>
  </div>
</section>
<nav class="crumbs wrap" aria-label="Okruszki"><a href="index.html">Start</a><span>›</span><b>Sklep</b></nav>
<section style="padding-bottom:40px">
  <div class="wrap">
    <div class="cat-list">{cards}</div>
    <p class="note" style="text-align:center">Ceny „od” - ostateczna kwota zależy od składu i wagi psa. Bez ukrytych opłat, anulujesz w dowolnym momencie. 90 dni gwarancji.</p>
  </div>
</section>
{footer(base)}
</body>
</html>'''
    path = os.path.join(OUT, "sklep.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


if __name__ == "__main__":
    paths = [build_product(p) for p in PRODUCTS]
    paths.append(build_catalog())
    for p in paths:
        print("OK", os.path.relpath(p, OUT))
