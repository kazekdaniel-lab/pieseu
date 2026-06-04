# -*- coding: utf-8 -*-
"""Podmienia 3 placeholderowe karty (rysowane słoiki STAWY/RELAKS/JELITA)
w sekcji #sklep na homepage na 7 realnych doypacków (zdjęcia + linki)."""
import os
from generate_products import PRODUCTS

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(OUT, "index.html")
html = open(F, encoding="utf-8").read()

START = '      <div class="pcard reveal" style="--panel:var(--pink-soft);--acc:var(--pink)">'
END = '\n    </div>\n  </div>\n</section>\n\n<!-- RESULTS -->'

i = html.index(START)
j = html.index(END)
assert i < j, "nie znaleziono granic sekcji sklepu"

cards = []
for p in PRODUCTS:
    cards.append(f'''      <div class="pcard reveal" style="--panel:{p['panel']};--acc:{p['acc']}">
        <a class="pcard-link" href="produkty/{p['slug']}.html">
          <div class="pcard-top" style="background:var(--panel);padding:20px"><img src="assets/img/{p['slug']}.png" alt="Opakowanie pieseu {p['name']} - suplement dla psa, 30 porcji" loading="lazy" style="width:100%;height:auto;display:block;border-radius:14px"></div>
          <div class="pcard-body"><h4>{p['name']}</h4><p>{p['tagline']}.</p>
            <div class="pcard-feat"><svg viewBox="0 0 24 24"><path d="M5 13l4 4L19 7"/></svg>30 porcji · proszek</div>
            <div class="pcard-foot"><span class="pr">od {p['price']} zł <small>/ mies.</small></span><span class="pcard-btn">Zobacz →</span></div>
          </div>
        </a>
      </div>''')

new_block = "\n".join(cards)
html = html[:i] + new_block + html[j:]
open(F, "w", encoding="utf-8").write(html)
print("OK - kart w sklepie homepage:", html.count('class="pcard reveal"'))
print("placeholder SVG (MEAL TOPPER) pozostałe:", html.count("MEAL TOPPER"))
