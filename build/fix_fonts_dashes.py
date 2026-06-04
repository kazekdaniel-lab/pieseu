# -*- coding: utf-8 -*-
"""Zamiana czcionek bez polskich znakow na 1:1 z latin-ext oraz dlugich pauz na '-'.
Fredoka -> Baloo 2 (naglowki), Space Mono -> JetBrains Mono (mono).
Em dash (U+2014) i en dash (U+2013) -> hyphen-minus (U+002D).
Uruchom z katalogu pieseu/: python3 build/fix_fonts_dashes.py
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SELF = os.path.abspath(__file__)
EXTS = (".html", ".css", ".js", ".py")

SUBS = [
    ("family=Fredoka:wght@400;500;600;700", "family=Baloo+2:wght@400;500;600;700;800"),
    ("family=Space+Mono:wght@700", "family=JetBrains+Mono:wght@700"),
    ("Fredoka,sans-serif", "'Baloo 2',sans-serif"),
    ("'Fredoka'", "'Baloo 2'"),
    ("'Space Mono'", "'JetBrains Mono'"),
    ("—", "-"),  # em dash
    ("–", "-"),  # en dash
]

changed = 0
for dp, _, fs in os.walk(ROOT):
    for fn in fs:
        if not fn.endswith(EXTS):
            continue
        p = os.path.join(dp, fn)
        if os.path.abspath(p) == SELF:
            continue
        s = open(p, encoding="utf-8").read()
        o = s
        for a, b in SUBS:
            s = s.replace(a, b)
        if s != o:
            open(p, "w", encoding="utf-8").write(s)
            changed += 1
            print("fixed", os.path.relpath(p, ROOT))
print("plikow zmienionych:", changed)
