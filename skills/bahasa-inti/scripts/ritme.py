#!/usr/bin/env python3
"""Pemeriksa irama dan struktur teks bahasa Indonesia (jejak mesin).

Yang diukur hanya kereguleran bentuk: variasi panjang kalimat, pembuka kalimat
berulang, paragraf yang bergerak dengan kata penghubung, penutup ritual, bingkai
ulang, staccato, tanda pisah menumpuk, daftar tiga serangkai, dan paralelisme
negatif. Kosakata dan frasa terlarang diperiksa `periksa.py`, bukan di sini.

Pemakaian:
  python3 ritme.py draf.md
  python3 ritme.py --genre sosial caption.txt
  python3 ritme.py --json draf.md
  python3 ritme.py --ketat draf.md        # kode keluar 1 bila skor >= 35
  python3 ritme.py --tes

Skor 0-100: makin tinggi makin datar. < 15 bersih, 15-35 beberapa pola,
35-60 banyak, > 60 parah. Skor ini bukan bukti teks ditulis mesin, dan nol
temuan tidak berarti teks sudah baik: spesifisitas dan dasar klaim tetap harus
dibaca. Hanya pustaka standar Python 3.8+, tanpa jaringan, hanya membaca berkas
yang disebut (atau stdin) dan mencetak temuan.
"""

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

# Bobot tiap metrik terhadap skor 0-100. Jumlahnya 132; skor dipotong di 100.
BOBOT = {
    "irama_seragam": 30,
    "pembuka_berulang": 20,
    "paragraf_berpenghubung": 15,
    "penutup_ritual": 10,
    "bingkai_ulang": 10,
    "staccato": 10,
    "tanda_pisah": 10,
    "daftar_tebal_titik_dua": 8,
    "tiga_serangkai": 8,
    "paralelisme_negatif": 6,
    "tanda_seru": 5,
}

GENRE_ABAIKAN = {
    "dokumen": {"daftar_tebal_titik_dua"},
    "sosial": {"staccato", "daftar_tebal_titik_dua", "tanda_seru"},
}

PENGHUBUNG = re.compile(
    r"^(namun|akan tetapi|tetapi|selain itu|selanjutnya|lebih lanjut|"
    r"sementara itu|di samping itu|sebaliknya|sebaliknya,|akibatnya|"
    r"oleh karena itu|oleh sebab itu|dengan demikian|karena itu|"
    r"di sisi lain|pada sisi lain|sejalan dengan itu|kemudian|"
    r"secara keseluruhan|singkatnya|ringkasnya)\b",
    re.I,
)

PENUTUP = re.compile(
    r"^(kesimpulannya|sebagai kesimpulan|simpulannya|dengan demikian|"
    r"secara keseluruhan|pada akhirnya|intinya|ringkasnya|singkatnya|jadi|"
    r"demikianlah|itulah|akhir kata|sebagai penutup)\b",
    re.I,
)

# Singkatan yang hampir tidak pernah menutup kalimat; kalau diikuti huruf kapital,
# kalimatnya disambung. "dll.", "dsb.", "dst." justru sering menutup kalimat, jadi
# tidak dimasukkan: menyambungnya akan menggabungkan dua kalimat berbeda.
SINGKATAN_SAMBUNG = {
    "hlm", "hal", "vol", "no", "thn", "jl", "kec", "kab", "prof", "dr", "drg",
    "ir", "phd", "mis", "spt", "tsb", "yth", "et", "al", "s.d", "a.n", "u.p",
    "spd", "st", "mt", "mm", "ba", "ma",
}

RE_TEBAL_TITIK_DUA = re.compile(r"^\s*(?:[-*+]|\d+[.)])?\s*\*\*[^*\n]{1,60}\*\*\s*:", re.M)
RE_TRIGA = re.compile(r"\b[A-Za-z][A-Za-z-]+,\s+[A-Za-z][A-Za-z-]+,\s+dan\s+[A-Za-z][A-Za-z-]+\b")
RE_PARALEL_NEGATIF = re.compile(
    r"\b(bukan hanya|tidak hanya|bukan sekadar)\b[^.!?\n]{0,120}?\b(tetapi juga|melainkan|tetapi)\b"
    r"|\bbukan\s+[^.!?\n,]{1,40},\s+melainkan\b",
    re.I,
)
RE_EMOJI_BUTIR = re.compile(r"^\s*[\U0001F300-\U0001FAFF\u2600-\u27BF]\s", re.M)


def pecah_kalimat(teks):
    """Pecah teks jadi kalimat. Singkatan dan desimal tidak memotong kalimat."""
    bagian = re.split(r"(?<=[.!?])[\"”’]?\s+(?=[\"“‘(\[]?[A-ZÀ-Ý0-9])", teks)
    hasil = []
    for b in bagian:
        b = b.strip()
        if not b:
            continue
        if hasil:
            ekor = hasil[-1].rstrip("\"”’").rstrip(".!?").split()
            kata_akhir = ekor[-1].lower().lstrip("(") if ekor else ""
            if kata_akhir in SINGKATAN_SAMBUNG or re.fullmatch(r"\d+[.,]\d*", kata_akhir or ""):
                hasil[-1] = hasil[-1] + " " + b
                continue
        hasil.append(b)
    return hasil


def kata(teks):
    return re.findall(r"[^\W\d_]+(?:[-'][^\W\d_]+)*|\d+", teks, re.UNICODE)


def paragraf_prosa(teks):
    """Paragraf isi: buang blok kode, tabel, judul, dan blockquote."""
    baris = []
    dalam_kode = False
    for b in teks.splitlines():
        t = b.strip()
        if t.startswith("```") or t.startswith("~~~"):
            dalam_kode = not dalam_kode
            continue
        if dalam_kode:
            continue
        if not t or t.startswith("#") or t.startswith("|") or t.startswith(">"):
            baris.append("")
            continue
        baris.append(t)
    blok, kini = [], []
    for b in baris:
        if b:
            kini.append(b)
        elif kini:
            blok.append(" ".join(kini))
            kini = []
    if kini:
        blok.append(" ".join(kini))
    return blok


def cv(nilai):
    if not nilai:
        return 0.0
    rata = sum(nilai) / len(nilai)
    if rata == 0:
        return 0.0
    return math.sqrt(sum((v - rata) ** 2 for v in nilai) / len(nilai)) / rata


def bigram_isi(teks):
    toks = [w.lower() for w in kata(teks) if len(w) > 3]
    return set(zip(toks, toks[1:]))


def periksa(teks, genre="prosa"):
    paragraf = paragraf_prosa(teks)
    isi = "\n\n".join(paragraf)
    kalimat = pecah_kalimat(isi)
    panjang = [len(kata(k)) for k in kalimat]
    n_kata = len(kata(isi))
    abai = GENRE_ABAIKAN.get(genre, set())
    temuan = []

    def tambah(metrik, nilai, ambang, saran, keterangan):
        if metrik in abai:
            return
        temuan.append({
            "metrik": metrik,
            "nilai": nilai,
            "ambang": ambang,
            "bobot": BOBOT[metrik],
            "keterangan": keterangan,
            "saran": saran,
        })

    metrik = {
        "kalimat": len(kalimat),
        "paragraf": len(paragraf),
        "kata": n_kata,
        "irama_cv": round(cv(panjang), 3),
        "rata_panjang_kalimat": round(sum(panjang) / len(panjang), 1) if panjang else 0,
    }

    # 1. irama seragam
    if len(kalimat) >= 8 and metrik["irama_cv"] < 0.40:
        tambah(
            "irama_seragam", metrik["irama_cv"], "cv panjang kalimat < 0,40 pada 8+ kalimat",
            "Tulis gagasan utama dalam kalimat pendek, penjelasannya dalam kalimat panjang. "
            "Jangan memotong kalimat secara acak.",
            "Panjang kalimat hampir seragam; ini penanda jejak mesin paling kuat.",
        )

    # 2. pembuka kalimat berulang
    if len(kalimat) >= 5:
        pembuka = []
        for k in kalimat:
            w = kata(k)
            if w:
                pembuka.append(w[0].lower())
        hitung = Counter(pembuka)
        unik = len(hitung) / len(pembuka) if pembuka else 1.0
        terbanyak, jumlah_terbanyak = (hitung.most_common(1)[0] if hitung else ("", 0))
        beruntun = maks = 0
        sebelumnya = None
        for p in pembuka:
            beruntun = beruntun + 1 if p == sebelumnya else 1
            sebelumnya = p
            maks = max(maks, beruntun)
        metrik.update({
            "pembuka_unik_rasio": round(unik, 3),
            "pembuka_terbanyak": terbanyak,
            "pembuka_terbanyak_jumlah": jumlah_terbanyak,
            "pembuka_beruntun_maks": maks,
        })
        if unik < 0.55 or (jumlah_terbanyak >= 4 and jumlah_terbanyak / len(pembuka) > 0.25) or maks >= 4:
            tambah(
                "pembuka_berulang", unik,
                "rasio unik < 0,55, satu pembuka dipakai > 25% (minimal 4 kali), atau 4 pembuka sama beruntun",
                "Ganti subjek, balik susunan, atau gabungkan dua kalimat. Prosedur bernomor dan "
                "langkah teknis dikecualikan.",
                "Pembuka kalimat mengulang pola yang sama.",
            )

    # 3. paragraf dibuka kata penghubung
    if paragraf:
        berpenghubung = sum(1 for p in paragraf if PENGHUBUNG.match(p))
        metrik["paragraf_berpenghubung"] = berpenghubung
        if berpenghubung >= 3 or (len(paragraf) >= 8 and berpenghubung / len(paragraf) > 0.4):
            tambah(
                "paragraf_berpenghubung", berpenghubung,
                ">= 3 paragraf, atau > 40% dari 8+ paragraf",
                "Ganti dengan kalimat topik yang menyebut bendanya. Kata penghubung tetap sah "
                "saat arah argumen benar-benar berbalik.",
                "Paragraf bergerak dengan rambu, bukan dengan isi.",
            )

    # 4. penutup ritual
    if len(paragraf) >= 3:
        akhir = paragraf[-1]
        if PENUTUP.match(akhir):
            tambah(
                "penutup_ritual", akhir.split(".")[0][:60],
                "paragraf terakhir dibuka frasa penutup baku",
                "Ganti dengan satu fakta atau keputusan konkret yang menjadi ujung tulisan. "
                "Abstrak dan ringkasan eksekutif dikecualikan.",
                "Penutup merangkum ulang, bukan menutup dengan isi.",
            )

        # 5. bingkai ulang: paragraf akhir mengulang isi paragraf pertama
        awal_bi = bigram_isi(paragraf[0])
        akhir_bi = bigram_isi(akhir)
        gabung = awal_bi | akhir_bi
        tumpang = len(awal_bi & akhir_bi) / len(gabung) if gabung else 0.0
        metrik["bingkai_ulang"] = round(tumpang, 3)
        if tumpang >= 0.12 and len(awal_bi & akhir_bi) >= 2:
            tambah(
                "bingkai_ulang", round(tumpang, 3),
                "paragraf akhir mengulang 2+ bigram isi dari paragraf pertama",
                "Hapus rangkuman; akhiri dengan poin baru yang spesifik.",
                "Teks memakai bingkai 'katakan akan mengatakan, katakan, katakan sudah dikatakan'.",
            )

    # 6. staccato
    if len(paragraf) >= 6:
        pendek = 0
        for p in paragraf:
            ps = pecah_kalimat(p)
            if len(ps) == 1 and len(kata(ps[0])) < 12:
                pendek += 1
        rasio = pendek / len(paragraf)
        metrik["staccato_rasio"] = round(rasio, 3)
        if rasio > 0.6:
            tambah(
                "staccato", round(rasio, 3), "> 60% paragraf berupa satu kalimat pendek (< 12 kata)",
                "Gabungkan paragraf yang gagasannya sama. Caption dan naskah iklan dikecualikan.",
                "Teks terbaca seperti slide, bukan tulisan.",
            )

    # 7. tanda pisah
    garis = teks.count("—")
    if n_kata:
        per_seribu = garis / n_kata * 1000
        metrik["tanda_pisah_per_1000"] = round(per_seribu, 3)
        if per_seribu > 1:
            tambah(
                "tanda_pisah", round(per_seribu, 3), "> 1 per 1.000 kata",
                "Ganti dengan koma, kurung, atau titik.",
                "Tanda pisah dipakai sebagai gaya, bukan kebutuhan.",
            )

    # 8. daftar berlabel tebal + titik dua
    n_tebal = len(RE_TEBAL_TITIK_DUA.findall(teks))
    metrik["daftar_tebal_titik_dua"] = n_tebal
    if n_tebal >= 3:
        tambah(
            "daftar_tebal_titik_dua", n_tebal, ">= 3 baris '**Label:** penjelasan'",
            "Ubah jadi prosa atau butir biasa.",
            "Format daftar berlabel berulang adalah pola keluaran mesin.",
        )

    # 9. tiga serangkai
    n_triga = len(RE_TRIGA.findall(isi))
    if n_kata:
        kepadatan = n_triga / n_kata * 500
        metrik["tiga_serangkai_per_500"] = round(kepadatan, 3)
        if n_triga >= 2 and kepadatan > 1:
            tambah(
                "tiga_serangkai", n_triga, ">= 2 kali, > 1 per 500 kata",
                "Sisakan satu; sisanya ganti dengan detail konkret atau angka.",
                "Tiga kata sifat berderet berulang.",
            )

    # 10. paralelisme negatif
    n_paralel = len(RE_PARALEL_NEGATIF.findall(isi))
    metrik["paralelisme_negatif"] = n_paralel
    if n_paralel >= 2:
        tambah(
            "paralelisme_negatif", n_paralel, ">= 2 kali",
            "Nyatakan klaimnya langsung tanpa membuka dengan penyangkalan.",
            "Pola 'bukan hanya X, tetapi juga Y' dipakai sebagai templat.",
        )

    # 11. tanda seru
    n_seru = isi.count("!")
    if n_kata:
        seru_per_500 = n_seru / n_kata * 500
        metrik["tanda_seru_per_500"] = round(seru_per_500, 3)
        if seru_per_500 > 1:
            tambah(
                "tanda_seru", n_seru, "> 1 per 500 kata",
                "Sisakan paling banyak satu per bagian.",
                "Tanda seru dipakai sebagai penekanan, bukan kebutuhan.",
            )

    skor = min(100, sum(t["bobot"] for t in temuan))
    return {
        "skor_jejak_mesin": skor,
        "genre": genre,
        "metrik": metrik,
        "temuan": temuan,
    }


def laporan(hasil):
    baris = [
        f"skor jejak mesin: {hasil['skor_jejak_mesin']}/100 "
        f"(< 15 bersih, 15-35 beberapa pola, 35-60 banyak, > 60 parah)",
        f"{hasil['metrik'].get('kata', 0)} kata, {hasil['metrik'].get('kalimat', 0)} kalimat, "
        f"{hasil['metrik'].get('paragraf', 0)} paragraf, genre {hasil['genre']}",
    ]
    if not hasil["temuan"]:
        baris.append("tidak ada temuan struktur")
        return "\n".join(baris)
    for t in hasil["temuan"]:
        baris.append(
            f"\n[{t['metrik']}] nilai {t['nilai']} (ambang {t['ambang']}, bobot {t['bobot']})"
            f"\n  {t['keterangan']}"
            f"\n  Saran: {t['saran']}"
        )
    return "\n".join(baris)


def tes():
    """Uji mandiri: teks datar harus berskor tinggi, teks bervariasi harus rendah."""
    kasus = []

    datar = (
        "Sistem ini bertujuan untuk meningkatkan efisiensi proses pencatatan data pada "
        "instansi pemerintahan di seluruh wilayah kerja. Sistem ini menggunakan pendekatan "
        "digital dalam melakukan pengolahan data yang selama ini dilakukan secara manual. "
        "Sistem ini juga menyediakan fitur pelaporan otomatis yang dapat diakses oleh "
        "pengguna dengan hak akses tertentu.\n\n"
        "Sistem ini diharapkan dapat mengurangi beban kerja petugas dalam melakukan "
        "pencatatan data secara harian. Sistem ini telah diuji pada tiga instansi "
        "pemerintahan dengan jumlah pengguna yang cukup beragam. Sistem ini menghasilkan "
        "peningkatan efisiensi yang cukup signifikan pada seluruh instansi yang mengikuti "
        "pengujian tersebut.\n\n"
        "Sistem ini juga dilengkapi dengan modul pelaporan yang dapat disesuaikan dengan "
        "kebutuhan masing-masing instansi pengguna. Modul pelaporan tersebut menyajikan data "
        "dalam bentuk tabel dan grafik yang mudah dipahami oleh pengguna.\n\n"
        "Kesimpulannya, sistem ini layak untuk diadopsi oleh instansi pemerintahan yang "
        "ingin meningkatkan efisiensi pencatatan data secara berkelanjutan."
    )
    kasus.append(("datar", datar, {"irama_seragam", "pembuka_berulang", "penutup_ritual"}))

    alami = (
        "Pencatatan manual di tiga kecamatan memakan 15 menit per berkas. Kami mengukurnya "
        "selama dua minggu, dengan stopwatch, di meja loket yang sama.\n\n"
        "Angkanya beragam. Loket pertama rata-rata 12 menit, loket ketiga 21 menit. "
        "Sebabnya bukan petugas, melainkan buku register yang harus dicari dulu ke ruang "
        "belakang setiap kali ada berkas baru masuk.\n\n"
        "Setelah register dipindahkan ke depan, rata-ratanya turun jadi 9 menit. Tidak ada "
        "pelatihan, tidak ada perangkat baru, dan tidak ada anggaran yang keluar."
    )
    kasus.append(("alami", alami, set()))

    gagal = []
    for nama, teks, harus_ada in kasus:
        hasil = periksa(teks)
        metrik = {t["metrik"] for t in hasil["temuan"]}
        if nama == "datar":
            kurang = harus_ada - metrik
            if kurang:
                gagal.append(f"datar: metrik tidak terdeteksi {sorted(kurang)}")
            if hasil["skor_jejak_mesin"] < 15:
                gagal.append(f"datar: skor terlalu rendah {hasil['skor_jejak_mesin']}")
        else:
            if hasil["skor_jejak_mesin"] >= 15:
                gagal.append(f"alami: skor terlalu tinggi {hasil['skor_jejak_mesin']} {sorted(metrik)}")

    # genre sosial mematikan staccato
    stacc = "\n\n".join(["Pagi."] * 8)
    if "staccato" not in {t["metrik"] for t in periksa(stacc)["temuan"]}:
        gagal.append("staccato tidak terdeteksi pada teks tanpa genre")
    if "staccato" in {t["metrik"] for t in periksa(stacc, "sosial")["temuan"]}:
        gagal.append("genre sosial seharusnya mematikan staccato")

    if gagal:
        for g in gagal:
            print("GAGAL:", g)
        return 1
    print("ok")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Pemeriksa irama dan struktur teks bahasa Indonesia.")
    ap.add_argument("berkas", nargs="?", help="path berkas, atau - untuk stdin")
    ap.add_argument("--genre", choices=["prosa", "dokumen", "sosial"], default="prosa")
    ap.add_argument("--json", action="store_true", help="keluaran JSON")
    ap.add_argument("--ketat", action="store_true", help="kode keluar 1 bila skor >= 35")
    ap.add_argument("--tes", action="store_true", help="uji mandiri")
    a = ap.parse_args(argv)

    if a.tes:
        return tes()

    if not a.berkas:
        ap.error("berkas wajib, atau pakai --tes")
    if a.berkas == "-":
        teks = sys.stdin.buffer.read().decode("utf-8", errors="replace")
    else:
        p = Path(a.berkas)
        if not p.exists():
            print(f"berkas tidak ditemukan: {p}", file=sys.stderr)
            return 2
        teks = p.read_text(encoding="utf-8", errors="replace")

    hasil = periksa(teks, a.genre)
    print(json.dumps(hasil, ensure_ascii=False, indent=2) if a.json else laporan(hasil))
    return 1 if a.ketat and hasil["skor_jejak_mesin"] >= 35 else 0


if __name__ == "__main__":
    raise SystemExit(main())