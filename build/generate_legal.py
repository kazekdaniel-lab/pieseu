# -*- coding: utf-8 -*-
"""Generuje strony prawne (poza polityka-prywatnosci.html, którą napisano ręcznie):
cookies, regulamin, dostawa-i-zwroty. Współdzieli header/footer/baner z generate_products.
"""
import os, json
from generate_products import head, header, footer, OUT, SITE


def page(slug, title, desc, h1, upd, toc, body, ld_extra=None):
    base = ""
    url = f"{SITE}/{slug}.html"
    ld = {"@context": "https://schema.org", "@type": "WebPage", "name": h1,
          "url": url, "inLanguage": "pl-PL",
          "isPartOf": {"@type": "WebSite", "name": "pieseu", "url": f"{SITE}/"}}
    blocks = [ld] + (ld_extra or [])
    ldjson = "\n".join(f'<script type="application/ld+json">{json.dumps(b, ensure_ascii=False)}</script>' for b in blocks)
    crumb = f'<nav class="crumbs wrap" aria-label="Okruszki"><a href="index.html">Start</a><span>›</span><b>{h1}</b></nav>'
    toc_html = ""
    if toc:
        items = "".join(f'<li><a href="#{i}">{t}</a></li>' for (i, t) in toc)
        toc_html = f'<div class="toc"><b>Spis treści</b><ol>{items}</ol></div>'
    html = f'''{head(title, desc, url, f"{SITE}/assets/img/odpornosc.png")}
{ldjson}
<link rel="stylesheet" href="assets/css/pieseu.css">
</head>
<body>
{header(base)}
{crumb}
<main class="wrap legal">
  <h1>{h1}</h1>
  <p class="upd">{upd}</p>
  {toc_html}
  {body}
  <p style="margin-top:30px;font-size:13px;color:var(--ink-2)"><b>Uwaga:</b> Pola w <span class="ph">[nawiasach]</span> to placeholdery - uzupełnij realnymi danymi firmy przed publikacją. Dokument ma charakter wzorcowy; zweryfikuj go z prawnikiem.</p>
</main>
{footer(base)}
</body>
</html>'''
    path = os.path.join(OUT, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    return path


# =================== COOKIES ===================
cookies_body = '''
<p>Niniejsza Polityka cookies wyjaśnia, czym są pliki cookies, jakich używamy w serwisie pieseu.pl oraz jak możesz zarządzać swoimi zgodami. Polityka stanowi uzupełnienie <a href="polityka-prywatnosci.html">Polityki prywatności</a>.</p>

<h2 id="czym">1. Czym są pliki cookies</h2>
<p>Cookies to małe pliki tekstowe zapisywane na Twoim urządzeniu podczas korzystania ze strony. Pozwalają m.in. zapamiętać Twoje preferencje, utrzymać sesję koszyka oraz prowadzić statystyki ruchu.</p>

<h2 id="rodzaje">2. Rodzaje cookies, których używamy</h2>
<table>
  <thead><tr><th>Kategoria</th><th>Cel</th><th>Wymaga zgody</th></tr></thead>
  <tbody>
    <tr><td><b>Niezbędne</b></td><td>Działanie sklepu, koszyk, logowanie, bezpieczeństwo i zapamiętanie zgody cookies.</td><td>Nie (podstawa: prawnie uzasadniony interes)</td></tr>
    <tr><td><b>Analityczne</b></td><td>Statystyki odwiedzin i zachowań (np. <span class="ph">[Google Analytics]</span>) - pomagają ulepszać stronę.</td><td>Tak</td></tr>
    <tr><td><b>Marketingowe</b></td><td>Remarketing i dopasowane reklamy (np. <span class="ph">[Meta Pixel, Google Ads]</span>).</td><td>Tak</td></tr>
  </tbody>
</table>

<h2 id="podmioty">3. Cookies podmiotów trzecich</h2>
<p>Część cookies może pochodzić od naszych dostawców narzędzi analitycznych i reklamowych. Lista przykładowych dostawców: <span class="ph">[Google, Meta, …]</span>. Zasady przetwarzania danych przez te podmioty określają ich własne polityki prywatności.</p>

<h2 id="zarzadzanie">4. Jak zarządzać zgodami</h2>
<p>Przy pierwszej wizycie wyświetlamy baner, w którym możesz zaakceptować wszystkie cookies, odrzucić opcjonalne lub wybrać kategorie w „Ustawieniach”. Swój wybór możesz zmienić w każdej chwili:</p>
<p><a class="btn btn-primary" href="#" data-cookie-settings>Otwórz ustawienia cookies</a></p>
<p>Cookies możesz też usunąć lub zablokować w ustawieniach przeglądarki. Ograniczenie cookies niezbędnych może wpłynąć na działanie sklepu.</p>

<h2 id="okres-c">5. Jak długo przechowujemy cookies</h2>
<p>Cookies sesyjne są usuwane po zamknięciu przeglądarki. Cookies trwałe przechowujemy przez okres do <span class="ph">[np. 12 miesięcy]</span> lub do czasu wycofania zgody.</p>
'''

# =================== REGULAMIN ===================
regulamin_body = '''
<p>Regulamin określa zasady korzystania ze sklepu internetowego pieseu.pl, składania zamówień, zawierania umów sprzedaży i subskrypcji, dostawy, płatności, prawa odstąpienia oraz reklamacji.</p>

<h2 id="def">1. Definicje</h2>
<ul>
  <li><b>Sprzedawca</b> - <span class="ph">[NAZWA FIRMY]</span>, <span class="ph">[ADRES]</span>, NIP <span class="ph">[NIP]</span>, REGON <span class="ph">[REGON]</span>, KRS <span class="ph">[KRS]</span>.</li>
  <li><b>Sklep</b> - serwis internetowy dostępny pod adresem pieseu.pl.</li>
  <li><b>Klient / Konsument</b> - osoba korzystająca ze Sklepu i zawierająca umowę.</li>
  <li><b>Produkt</b> - suplement diety dla psów (w tym mieszanka personalizowana dobrana w quizie).</li>
  <li><b>Subskrypcja</b> - usługa cyklicznej dostawy Produktu w wybranym interwale.</li>
</ul>

<h2 id="ogolne">2. Postanowienia ogólne</h2>
<p>Do korzystania ze Sklepu potrzebne jest urządzenie z dostępem do internetu i aktualna przeglądarka. Ceny podane są w złotych (PLN) i zawierają podatek VAT. Ceny „od” oznaczają cenę wyjściową - ostateczna kwota zależy od składu i wagi psa.</p>

<h2 id="zamowienia">3. Składanie zamówień</h2>
<p>Zamówienie składasz, dodając Produkt do koszyka i potwierdzając zakup przyciskiem oznaczającym obowiązek zapłaty. Umowa zostaje zawarta z chwilą potwierdzenia przyjęcia zamówienia przez Sprzedawcę. Produkty personalizowane są przygotowywane na podstawie informacji podanych w quizie.</p>

<h2 id="platnosci">4. Płatności</h2>
<p>Dostępne metody płatności: <span class="ph">[BLIK, Przelewy24, karta płatnicza]</span>. Operatorem płatności jest <span class="ph">[NAZWA OPERATORA]</span>. Sprzedawca nie przechowuje danych kart płatniczych.</p>

<h2 id="subskrypcja">5. Subskrypcja</h2>
<p>Subskrypcja oznacza cykliczne dostawy i automatyczne płatności w wybranym interwale. Możesz w dowolnym momencie i bez dodatkowych kosztów wstrzymać, zmienić skład, zmienić częstotliwość lub anulować subskrypcję w panelu klienta lub kontaktując się z obsługą. Anulowanie odnosi skutek wobec kolejnych, jeszcze nieprzygotowanych dostaw.</p>

<h2 id="dostawa">6. Dostawa</h2>
<p>Szczegóły dostawy, koszty i terminy opisaliśmy na stronie <a href="dostawa-i-zwroty.html">Dostawa i zwroty</a>. Darmowa dostawa obowiązuje od kwoty <span class="ph">[149 zł]</span>.</p>

<h2 id="odstapienie">7. Prawo odstąpienia od umowy</h2>
<p>Konsument może odstąpić od umowy zawartej na odległość w terminie 14 dni bez podania przyczyny, składając oświadczenie (np. mailem na <span class="ph">[ADRES E-MAIL]</span>). Zwracamy płatność w ciągu 14 dni.</p>
<p><b>Wyjątek:</b> prawo odstąpienia nie przysługuje m.in. dla produktów przygotowanych na specjalne zamówienie i dopasowanych do indywidualnych potrzeb (mieszanka personalizowana) oraz dla produktów w zapieczętowanym opakowaniu, których po otwarciu nie można zwrócić ze względów higienicznych, jeżeli opakowanie zostało otwarte (art. 38 ustawy o prawach konsumenta). Niezależnie od tego oferujemy <b>90-dniową gwarancję satysfakcji</b> - patrz <a href="dostawa-i-zwroty.html">Dostawa i zwroty</a>.</p>

<h2 id="reklamacje">8. Reklamacje i rękojmia</h2>
<p>Sprzedawca odpowiada za zgodność Produktu z umową na zasadach określonych w przepisach o prawach konsumenta. Reklamacje zgłaszaj na <span class="ph">[ADRES E-MAIL]</span>; rozpatrzymy je w terminie 14 dni.</p>

<h2 id="spory">9. Pozasądowe rozwiązywanie sporów</h2>
<p>Konsument może skorzystać z pozasądowych sposobów rozpatrywania reklamacji i dochodzenia roszczeń, w tym z platformy ODR Komisji Europejskiej (ec.europa.eu/consumers/odr).</p>

<h2 id="koncowe">10. Postanowienia końcowe</h2>
<p>W sprawach nieuregulowanych stosuje się przepisy prawa polskiego. Regulamin może ulec zmianie; do zamówień złożonych przed zmianą stosuje się wersję obowiązującą w chwili złożenia zamówienia.</p>
'''

# =================== DOSTAWA I ZWROTY ===================
dostawa_body = '''
<p>Wszystko o tym, jak i kiedy dotrze paczka, ile kosztuje dostawa oraz jak działa nasza 90-dniowa gwarancja satysfakcji.</p>

<h2 id="czas">1. Czas realizacji i wysyłki</h2>
<p>Produkty warzymy świeżo, na zamówienie. Standardowy czas przygotowania i wysyłki to <span class="ph">[1-3 dni robocze]</span>. O nadaniu paczki informujemy mailem z numerem do śledzenia.</p>

<h2 id="koszty">2. Koszty i metody dostawy</h2>
<table>
  <thead><tr><th>Metoda</th><th>Czas</th><th>Koszt</th></tr></thead>
  <tbody>
    <tr><td>Kurier <span class="ph">[nazwa]</span></td><td><span class="ph">[1-2 dni]</span></td><td><span class="ph">[od 12,99 zł]</span></td></tr>
    <tr><td>Paczkomat <span class="ph">[nazwa]</span></td><td><span class="ph">[1-2 dni]</span></td><td><span class="ph">[od 9,99 zł]</span></td></tr>
    <tr><td>Dostawa darmowa</td><td>jak wyżej</td><td>0 zł od <span class="ph">[149 zł]</span> i dla subskrypcji</td></tr>
  </tbody>
</table>

<h2 id="subskrypcja-d">3. Dostawy w subskrypcji</h2>
<p>W subskrypcji kolejne paczki wysyłamy automatycznie w wybranym interwale, z darmową dostawą. Termin kolejnej dostawy zmienisz lub wstrzymasz w panelu klienta.</p>

<h2 id="gwarancja">4. 90 dni gwarancji satysfakcji</h2>
<p>Daj pieseu 90 dni. Jeśli Ty albo Twój pies nie zobaczycie różnicy, zwrócimy pełną kwotę za pierwsze opakowanie - bez drobnego druczku. Aby skorzystać, napisz na <span class="ph">[ADRES E-MAIL]</span> w ciągu 90 dni od pierwszego zamówienia.</p>

<h2 id="zwroty">5. Zwroty i odstąpienie</h2>
<p>Zasady odstąpienia od umowy (14 dni) oraz wyjątki dla produktów personalizowanych i zapieczętowanych opisuje <a href="regulamin.html#odstapienie">Regulamin</a>. Niezależnie od ustawowego prawa odstąpienia obowiązuje nasza 90-dniowa gwarancja satysfakcji.</p>

<h2 id="reklamacje-d">6. Uszkodzona lub błędna paczka</h2>
<p>Jeśli paczka dotarła uszkodzona lub niezgodna z zamówieniem, napisz na <span class="ph">[ADRES E-MAIL]</span> (najlepiej ze zdjęciem) - wyślemy nową lub zwrócimy pieniądze.</p>
'''


def faqpage(qa):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qa]}


if __name__ == "__main__":
    out = []
    out.append(page(
        "polityka-cookies", "Polityka cookies | pieseu",
        "Polityka cookies pieseu - jakich plików cookies używamy, w jakim celu i jak zarządzać zgodami na cookies analityczne i marketingowe.",
        "Polityka cookies",
        'Ostatnia aktualizacja: <span class="ph">[DATA]</span>',
        [("czym", "Czym są cookies"), ("rodzaje", "Rodzaje cookies"), ("podmioty", "Cookies podmiotów trzecich"),
         ("zarzadzanie", "Zarządzanie zgodami"), ("okres-c", "Okres przechowywania")],
        cookies_body))
    out.append(page(
        "regulamin", "Regulamin sklepu | pieseu",
        "Regulamin sklepu pieseu.pl - zasady zamówień, płatności, subskrypcji, dostawy, prawa odstąpienia i reklamacji suplementów dla psów.",
        "Regulamin sklepu",
        'Obowiązuje od: <span class="ph">[DATA]</span>',
        [("def", "Definicje"), ("ogolne", "Postanowienia ogólne"), ("zamowienia", "Składanie zamówień"),
         ("platnosci", "Płatności"), ("subskrypcja", "Subskrypcja"), ("dostawa", "Dostawa"),
         ("odstapienie", "Prawo odstąpienia"), ("reklamacje", "Reklamacje"), ("spory", "Spory"), ("koncowe", "Końcowe")],
        regulamin_body))
    out.append(page(
        "dostawa-i-zwroty", "Dostawa i zwroty | pieseu",
        "Dostawa i zwroty pieseu - czas wysyłki, koszty dostawy, dostawy w subskrypcji oraz 90-dniowa gwarancja satysfakcji.",
        "Dostawa i zwroty",
        'Ostatnia aktualizacja: <span class="ph">[DATA]</span>',
        [("czas", "Czas realizacji"), ("koszty", "Koszty dostawy"), ("subskrypcja-d", "Dostawy w subskrypcji"),
         ("gwarancja", "90 dni gwarancji"), ("zwroty", "Zwroty"), ("reklamacje-d", "Uszkodzona paczka")],
        dostawa_body,
        ld_extra=[faqpage([
            ("Ile kosztuje dostawa?", "Dostawa kurierem lub do paczkomatu jest płatna zgodnie z cennikiem, a od kwoty 149 zł oraz w subskrypcji jest darmowa."),
            ("Jak działa 90-dniowa gwarancja?", "Jeśli w ciągu 90 dni nie zobaczysz różnicy u psa, zwracamy pełną kwotę za pierwsze opakowanie - wystarczy napisać do obsługi."),
            ("Czy mogę zwrócić personalizowaną mieszankę?", "Produkty personalizowane są wyłączone z ustawowego prawa odstąpienia, ale obejmuje je nasza 90-dniowa gwarancja satysfakcji."),
        ])]))
    for p in out:
        print("OK", os.path.relpath(p, OUT))
