# pieseu — strona + podstrony produktowe

Personalizowane suplementy dla psów (proszek / meal topper). Strona statyczna, gotowa do hostowania.

## Struktura

```
pieseu/
├─ index.html                  # strona główna (z NEWPIESEU.html + SEO + JSON-LD + baner cookies)
├─ sklep.html                  # katalog 7 produktów (ItemList JSON-LD)
├─ produkty/                   # 7 podstron produktowych (Product + FAQPage + BreadcrumbList)
│  ├─ trawienie-i-jelita.html
│  ├─ spokoj-i-wyciszenie.html
│  ├─ siersc-i-skora.html
│  ├─ odpornosc.html
│  ├─ stawy-i-mobilnosc.html
│  ├─ energia-i-witalnosc.html
│  └─ serce-i-krazenie.html
├─ regulamin.html              # strony prawne
├─ polityka-prywatnosci.html   # (RODO)
├─ polityka-cookies.html
├─ dostawa-i-zwroty.html       # + FAQPage JSON-LD
├─ sitemap.xml
├─ robots.txt                  # dopuszcza też boty AI/LLM (GPTBot, ClaudeBot, PerplexityBot…)
├─ assets/
│  ├─ css/pieseu.css           # wspólny arkusz (wyodrębniony z homepage + dodatki)
│  ├─ js/pieseu.js             # zgoda cookies, FAQ, selektor wagi
│  └─ img/*.png                # 7 doypacków (wzory — do podmiany)
└─ build/                      # generatory (źródło prawdy podstron)
   ├─ generate_products.py     # produkty + katalog  → uruchom: python3 build/generate_products.py
   ├─ generate_legal.py        # cookies/regulamin/dostawa
   └─ patch_home.py            # patch index.html (SEO, linki, baner)
```

Edytujesz treść produktów w `build/generate_products.py` (dane w `PRODUCTS`) i regenerujesz — nie ręcznie w HTML.

## DO UZUPEŁNIENIA przed publikacją (placeholdery)

1. **Dane firmy** — wszystkie `[NAZWA FIRMY]`, `[NIP]`, `[REGON]`, `[KRS]`, `[ADRES]`, `[E-MAIL]`, `[TELEFON]`, `[DATA]` w stronach prawnych. Stała `COMPANY`/`EMAIL` w `generate_products.py`.
2. **Domena** — wszędzie `https://pieseu.pl` (canonical, OG, sitemap, JSON-LD). Zmień, jeśli inna.
3. **Social media** — `[FACEBOOK]/[INSTAGRAM]/[TIKTOK]` w `Organization` (index.html).
4. **Operatorzy** — `[Przelewy24/BLIK]`, kurierzy, narzędzia analityczne w regulaminie/cookies.
5. **Tagi analityczne** — podłącz GA/Meta w `assets/js/pieseu.js` (funkcja `apply()`, miejsca `TODO`); ładują się TYLKO po zgodzie.

## Świadome decyzje / ryzyka

- **Brak `aggregateRating`/`review` w JSON-LD** — celowo. Homepage podaje „4,9/5 · 1 870 opinii”, „89% w 30 dni”, „6 000 psów”, listę polecających weterynarzy. Jeśli to nie są realne dane, nie wolno ich publikować (UOKiK, wytyczne Google). Dodaj rating do schematu dopiero po zebraniu prawdziwych opinii.
- **Kotwica `#quiz` nie ma strony** — quiz to rdzeń lejka, ale nie był w zakresie. Wszystkie CTA „Stwórz mieszankę” prowadzą do `#quiz` (martwa kotwica). Do zbudowania osobno.
- **Obrazy w base64** na homepage (waga ~630 KB) — pod Core Web Vitals warto wyciąć do plików.
- **Model produktu:** obszar = produkt, waga = wariant (selektor dawkowania). 7 doypacków = 7 obszarów.

## Podgląd lokalny

```
python3 -m http.server 8099 --directory pieseu
# http://localhost:8099/
```
