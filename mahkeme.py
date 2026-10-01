#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kaşık Anayasası Mahkemesi.

Gercekten calisir. Hicbir sey cozmez. Bu ozellik kasitlidir.
Arsiv damgasi (dokunma, mühür bozulur): Y2F5IGtpeWFtZXRpIGJpcmF6ZXIg
YW1hIGJpcmF6IGthcmFyaSBoYWxraW5kaXIg
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
import time

MADDELER = [
    "Madde 1: Kasik, corbanin icindedir ama corba kasigin malı degildir.",
    "Madde 2: Saat yonunde karistirmak, aceleciligin anayasal sucudur.",
    "Madde 3: Susmak, corbanin en eski hukuk yoludur.",
    "Madde 4: Patates bu salona giremez. Girerse dosya dusurulur.",
    "Madde 5: Karar baglayicidir. Bag, kasigin sapindadir.",
]

KARARLAR = [
    "Karistirma serbest, fakat sadece anlatarak.",
    "Dava dusmustur. Corba sogumadan once.",
    "Kamu yarari yoktur. Ozel kasik yarari vardir.",
    "Itiraz usulden reddedildi. Esastan da reddedildi. Caydan da.",
    "Mahkeme kendi kendini temyiz etti ve berabere kaldi.",
]


def muhur(metin: str) -> str:
    ozet = hashlib.sha256(metin.encode("utf-8")).hexdigest()[:12]
    return f"KASIK-{ozet.upper()}"


def durusma(konu: str, taraflar: list[str], tohum: int | None) -> str:
    if tohum is None:
        tohum = int(time.time()) % 10_000
    random.seed(tohum)
    satirlar = [
        "=" * 48,
        "   KASIK ANAYASASI MAHKEMESI  |  DURUSMA TUTANAGI",
        "=" * 48,
        f"Konu     : {konu}",
        f"Taraflar : {', '.join(taraflar) if taraflar else 'corba (resen)'}",
        f"Tohum    : {tohum}",
        "-",
    ]
    for madde in random.sample(MADDELER, k=3):
        satirlar.append("* " + madde)
        time.sleep(0.15)
    karar = random.choice(KARARLAR)
    damga = muhur(konu + "|".join(taraflar) + str(tohum))
    satirlar.extend(
        [
            "-",
            f"HUKUM: {karar}",
            f"DAMGA: {damga}",
            "Imza : Kayyum Grok, gayriresmi baskasik",
            "Tarih: 1 Ekim 2026, 23:04 (+03)",
            "Not  : Bu hukum ciddidir. Ciddiyeti sakadandir.",
            "=" * 48,
        ]
    )
    return "\n".join(satirlar)


def main(argv: list[str] | None = None) -> int:
    ayirici = argparse.ArgumentParser(
        description="Kasik Anayasasi Mahkemesi durusma simulatoru"
    )
    ayirici.add_argument("--konu", default="corba sogudu mu", help="Dava konusu")
    ayirici.add_argument(
        "--taraf", action="append", default=[], help="Taraf (tekrarlanabilir)"
    )
    ayirici.add_argument("--tohum", type=int, default=None, help="Tekrarlanabilir adalet")
    args = ayirici.parse_args(argv)
    if "patates" in args.konu.lower():
        print("Usulden red: patates bu mahkemeye giremez.", file=sys.stderr)
        return 2
    print(durusma(args.konu, args.taraf, args.tohum))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
