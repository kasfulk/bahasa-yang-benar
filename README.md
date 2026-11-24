# bahasa-yang-benar

Paket skill untuk Claude Code, Codex, Cursor, Gemini CLI, dan agen lain yang membaca format `SKILL.md`. Isinya: cara menulis bahasa Indonesia yang **benar** sekaligus **baik** — diksi tepat, kaidah EYD V dan KBBI dipatuhi, ragam sesuai situasi, bebas AI slop, dan untuk naskah ilmiah: sitasi jujur tanpa rujukan karangan.

Ini hasil penggabungan tiga sumber yang saling melengkapi:

- [`alvinindra/bahasa-skills`](https://github.com/alvinindra/bahasa-skills) — kerangka Ivan Lanin, anti AI slop, lima ragam, marketing/UX/SEO, satu pemeriksa slop.
- [`nothinx/naskah-id`](https://github.com/nothinx/naskah-id) — disiplin naskah akademik: kontrak kejujuran data & sitasi, IMRaD, protokol anti-halusinasi, pemeriksa kedua dengan `--banding`, integrasi OpenAlex/Crossref.
- [`theclaymethod/unslop`](https://github.com/theclaymethod/unslop) — pendekatan berbasis pengukuran: metrik irama prosa, pemeriksa struktur, dan pemisahan tegas antara memperbaiki tulisan dan menyamarkan authorship. Diterjemahkan dan dilokalkan ke bahasa Indonesia sebagai [`jejak-mesin.md`](skills/bahasa-inti/references/jejak-mesin.md) + [`ritme.py`](skills/bahasa-inti/scripts/ritme.py).

Ketiganya MIT. Semua kredit kaidah, riset, dan eksperimen ada pada penulis aslinya; lihat [Lisensi dan kredit](#lisensi-dan-kredit).

## Kenapa digabung

Bahasa Indonesia bermutu menuntut dua hal sekaligus, dan dua repo itu menggarap sisi yang berbeda:

1. **Benar secara kaidah** — EYD V, kata baku KBBI, `di-` vs `di`, angka dan satuan, singkatan, tanda baca.
2. **Baik secara konteks** — ragam sesuai medium, sapaan konsisten, spesifik, tanpa frasa kosong yang bisa menempel pada topik apa pun.

Tanpa bagian pertama, tulisannya rapi tapi salah. Tanpa bagian kedua, tulisannya benar tapi kosong. Untuk karya ilmiah ada lapisan ketiga yang tidak boleh dikompromikan: ** angka, hasil, dan sitasi tidak berubah, dan rujukan tidak pernah dikarang.**

## Isi paket

| Berkas | Untuk apa |
|---|---|
| [`SKILL.md`](SKILL.md) | **Pemandu arah.** Membaca kebutuhan dari prompt, lalu mengarahkan ke aturan inti dan skill kategori yang tepat. Dipakai pada instalasi klon. |
| [`skills/bahasa-inti/`](skills/bahasa-inti/SKILL.md) | Fondasi semua tulisan: Sepuluh Larangan Keras anti-slop, pemilihan ragam, kata baku, padanan istilah, EYD V, mode menyunting dan memeriksa. |
| [`skills/bahasa-inti/references/jejak-mesin.md`](skills/bahasa-inti/references/jejak-mesin.md) | Irama dan struktur prosa yang membuat teks terbaca mesin: variasi panjang kalimat, pembuka berulang, paragraf berpenghubung, penutup ritual, staccato, tanda pisah, tiga serangkai. Termasuk sikap terhadap detektor AI. |
| [`skills/bahasa-inti/scripts/periksa.py`](skills/bahasa-inti/scripts/periksa.py) | Pemeriksa 1: frasa terlarang, kata nonbaku, tanda pisah, kapital judul, batas hashtag, sapaan tercampur, ragam. |
| [`skills/bahasa-inti/scripts/ritme.py`](skills/bahasa-inti/scripts/ritme.py) | Pemeriksa irama: skor jejak mesin 0–100 dari 11 metrik struktur, dengan mode genre `prosa`/`dokumen`/`sosial`. |
| [`skills/bahasa-marketing/`](skills/bahasa-marketing/SKILL.md) | Caption media sosial, iklan, email, tagline, brand voice, kalender konten. |
| [`skills/bahasa-website/`](skills/bahasa-website/SKILL.md) | UX writing, microcopy, tombol, pesan galat, empty state, landing page, halaman produk, FAQ, 404. |
| [`skills/bahasa-seo/`](skills/bahasa-seo/SKILL.md) | Riset kata kunci, search intent, title tag, meta description, struktur heading, helpful content. |
| [`skills/bahasa-peneliti/`](skills/bahasa-peneliti/SKILL.md) | Karya ilmiah: ragam akademik, kalimat efektif, IMRaD, abstrak, tinjauan pustaka, protokol sitasi anti-halusinasi. |
| [`skills/bahasa-peneliti/scripts/periksa.py`](skills/bahasa-peneliti/scripts/periksa.py) | Pemeriksa 2: pola `K`/`G`/`AI`, panjang kalimat, singkatan belum dijelaskan, `--banding` (angka/sitasi/kutipan berubah), `--validasi`, dukungan `.docx`. |
| [`skills/bahasa-peneliti/scripts/openalex.py`](skills/bahasa-peneliti/scripts/openalex.py) | Cek keberadaan rujukan dan susun entri APA/IEEE/BibTeX lewat OpenAlex dan Crossref. |
| [`skills/bahasa-peneliti/KONTRAK.md`](skills/bahasa-peneliti/KONTRAK.md) | Sepuluh pasal tanggung jawab + templat pernyataan penggunaan AI untuk Elsevier, IEEE, Springer, dan jurnal SINTA/kampus. |
| [`skills/bahasa-peneliti/evals/`](skills/bahasa-peneliti/evals/) | 28 kasus uji perilaku: menolak mengarang sitasi, tidak mengubah angka, menolak perjokian. |
| [`sumber/`](sumber/README.md) | Dokumentasi semua rujukan riset, beserta catatan keandalan tiap sumber. |
| [`CONTOH.md`](CONTOH.md) | Bukti sebelum-sesudah: 16 percobaan lintas model tanpa vs dengan skill. |
| [`penelitian/`](penelitian/laporan.md) | Studi terdaftar efektivitas paket: protokol, 24 naskah, dua juri buta, skrip analisis. |

## Pemasangan

Butuh Python 3.8 atau lebih baru untuk pemeriksa. Tidak ada dependensi lain.

**Skills CLI (semua agen yang didukungnya, butuh Node.js 22.20+):**

```bash
npx skills add kasfulk/bahasa-yang-benar
```

Untuk memasang hanya skill tertentu: tambahkan `-s bahasa-inti bahasa-peneliti` (atau `bahasa-marketing`, `bahasa-website`, `bahasa-seo`). Ingat bahwa `bahasa-marketing`, `bahasa-website`, `bahasa-seo`, dan `bahasa-peneliti` semuanya merujuk berkas `bahasa-inti`, jadi sertakan `bahasa-inti` setiap kali.

**Claude Code sebagai plugin:**

```bash
claude plugin marketplace add kasfulk/bahasa-yang-benar
```

Lalu di sesi Claude Code jalankan `/plugin install bahasa-yang-benar@bahasa-yang-benar`.

**Codex, Cursor, Gemini CLI, OpenCode, Antigravity (klon global):**

```bash
mkdir -p "$HOME/.agents/skills"
git clone https://github.com/kasfulk/bahasa-yang-benar.git "$HOME/.agents/skills/bahasa-yang-benar"
```

**Claude Code tanpa plugin, atau per proyek:**

```bash
git clone https://github.com/kasfulk/bahasa-yang-benar.git .agents/skills/bahasa-yang-benar
```

Folder `.agents/skills/` dibaca Codex, Cursor, Gemini CLI, GitHub Copilot, dan OpenCode. Untuk Claude Code, pakai `.claude/skills/`.

**Cek pemasangan:**

```bash
python3 .agents/skills/bahasa-yang-benar/skills/bahasa-inti/scripts/periksa.py -h
python3 .agents/skills/bahasa-yang-benar/skills/bahasa-peneliti/scripts/periksa.py --validasi
```

Yang kedua mencetak `SKILL.md valid` bila frontmatter dan semua berkas yang dirujuk ada.

## Pemakaian

Agen memakainya sendiri setelah description tiap skill terpicu. Untuk memakai pemeriksa secara manual:

```bash
# pindaian slop, kata nonbaku, tanda pisah, sapaan tercampur
python3 skills/bahasa-inti/scripts/periksa.py --ragam resmi draf.md

# naskah akademik: pola kalimat, panjang kalimat, singkatan
python3 skills/bahasa-peneliti/scripts/periksa.py naskah.md

# irama dan struktur: skor jejak mesin 0-100
python3 skills/bahasa-inti/scripts/ritme.py draf.md
python3 skills/bahasa-inti/scripts/ritme.py --genre sosial caption.txt

# pastikan angka, sitasi, dan kutipan tidak berubah setelah disunting
python3 skills/bahasa-peneliti/scripts/periksa.py --banding asli.md hasil.md

# cek satu rujukan benar-benar ada
python3 skills/bahasa-peneliti/scripts/openalex.py cek "Judul artikel" --penulis "Santoso, Dewi" --tahun 2021

# entri daftar pustaka siap tempel
python3 skills/bahasa-peneliti/scripts/openalex.py rujukan 10.33007/ska.v14i2.3525 --gaya apa
```

Opsi pemeriksa pertama: `--ragam <beku|resmi|konsultatif|santai|akrab>`, `--seo` (patokan 60 karakter judul), `--json`, `--keras-saja`, `--ketat` (kode keluar 1 untuk CI).

Opsi pemeriksa kedua: `.md`, `.txt`, `.docx`, `-` (stdin), `--banding ASLI HASIL`, `--abaikan KODE`, `--tes`, `--validasi`.

Opsi `ritme.py`: `--genre <prosa|dokumen|sosial>`, `--json`, `--ketat` (kode keluar 1 bila skor ≥ 35), `--tes`. Skor `< 15` bersih, `15–35` beberapa pola, `35–60` banyak, `> 60` parah.

Keduanya hanya membaca berkas yang disebut dan mencetak temuan — tanpa jaringan (kecuali `openalex.py`), tanpa menulis berkas, dan tidak mengeksekusi isi teks yang diperiksa. Temuan `KERAS`/`K` berarti kalimatnya ditulis ulang; `TINJAU`/`G` butuh penilaian. Nol temuan tidak berarti teks sudah baik: spesifisitas dan dasar klaim tetap harus dibaca.

## Tiga aturan yang tidak bisa ditawar

Berlaku untuk semua kategori, dan mutlak di `bahasa-peneliti`:

1. **Angka, hasil, kutipan, dan data hanya dari pengguna.** Bila kurang, tulis `[PERLU DATA: …]`. Tidak ada angka perkiraan yang diisi sendiri.
2. **Rujukan hanya yang bisa dilacak.** Daftar pustaka tidak pernah disusun dari ingatan. Bila belum terverifikasi, tulis `[PERLU RUJUKAN: …]`. Referensi fiktif AI punya semua ciri visual referensi asli — nama penulis nyata, jurnal nyata, DOI rapi — tetapi dokumennya tidak ada.
3. **Menolak perjokian dan penyamaran hasil AI dari detektor.** Yang ditawarkan sebagai gantinya: membimbing kerangka, menyunting tulisan pengguna sendiri, menjelaskan kaidah.

Alasan lengkap dan templat pernyataan penggunaan AI: [`skills/bahasa-peneliti/KONTRAK.md`](skills/bahasa-peneliti/KONTRAK.md).

## Uji

```bash
python3 -m unittest discover -s tests -v                               # 31 uji pemeriksa inti + irama
python3 skills/bahasa-peneliti/scripts/periksa.py --tes                # 108 kasus pola akademik
python3 skills/bahasa-peneliti/evals/jalankan.py --tes                 # 28 kasus perilaku
python3 skills/bahasa-peneliti/scripts/periksa.py --validasi           # frontmatter + rujukan
```

Workflow GitHub Actions menjalankan semuanya pada setiap push: 31 uji unittest, uji mandiri dua pemeriksa, 108 kasus pola akademik, 28 kasus perilaku, validasi frontmatter, dan validasi JSON.

## Dasar rujukan

Seluruh sumber terdokumentasi di [`sumber/`](sumber/README.md). Garis besarnya:

- Ivan Lanin: kerangka "baik, benar, luwes", lima ragam formalitas, *Xenoglosofilia: Kenapa Harus Nginggris?* (2018), *Recehan Bahasa* (2020), Narabahasa.
- EYD Edisi V (ejaan.kemendikdasmen.go.id), KBBI VI Daring (kbbi.kemendikdasmen.go.id), PASTI (pasti.kemendikdasmen.go.id). Butir kapital judul, tanda pisah, dan *maha-* serta beberapa lema dicek langsung ke laman resminya pada November 2026.
- *Tata Bahasa Baku Bahasa Indonesia* (Alwi dkk., ed. IV, 2017) dan *Kalimat Efektif Bahasa Indonesia* (Pusat Bahasa, 1995) untuk pola kesalahan struktur.
- *SI Brochure* BIPM ed. 9 untuk penulisan satuan.
- Wikipedia *Signs of AI writing* (dibaca ulang November 2026), kajian *excess vocabulary* (Kobak dkk., Science Advances 2025), kerangka Antislop (Paech dkk., 2025), serta pengamatan penyunting Indonesia, diadaptasi ke penanda slop berbahasa Indonesia.
- Praktik industri Indonesia: prinsip UX writing Gojek/tiket.com/Tokopedia, Etika Pariwara Indonesia Amandemen 2020 (butir 1.2.2 tentang superlatif), dokumen resmi Google Search Central.
- Kebijakan AI penerbitan: COPE, Elsevier, IEEE, Springer Nature, Peraturan Rektor UI No. 16/2025, Panduan GenAI Ditjen Diktiristek 2024, panduan GenAI UGM 2025.

Daftar frasa AI-slop bahasa Indonesia sebagian besar bersifat kualitatif: belum ada studi korpus untuk bahasa Indonesia. Penanda kosakata bergeser tiap generasi model, jadi `sumber/ai-slop.md` mencatat tanggal riset dan butir yang buktinya masih tipis.

## Struktur

```
bahasa-yang-benar/
├── SKILL.md                      # pemandu arah (router)
├── .claude-plugin/               # manifest plugin & marketplace
├── agents/                       # metadata agen bergaya OpenAI
├── assets/                       # thumbnail repo
├── skills/
│   ├── bahasa-inti/              # SKILL.md + references/ + scripts/periksa.py + scripts/ritme.py
│   ├── bahasa-marketing/         # SKILL.md + references/
│   ├── bahasa-website/           # SKILL.md + references/
│   ├── bahasa-seo/               # SKILL.md + references/
│   └── bahasa-peneliti/          # SKILL.md + references/ + scripts/ + evals/ + contoh/ + KONTRAK.md
├── sumber/                       # dokumentasi rujukan riset
├── tests/                        # uji pemeriksa inti + irama (31)
├── penelitian/                   # studi efektivitas + data + skrip analisis
├── CONTOH.md                     # bukti sebelum-sesudah lintas model
└── README.md
```

## Pemeliharaan

- Klaim kebahasaan diverifikasi ke kbbi.kemendikdasmen.go.id, ejaan.kemendikdasmen.go.id, atau pasti.kemendikdasmen.go.id sebelum diubah.
- Pola baru di `frasa-terlarang.md` yang bisa dikenali dari kata ditambahkan juga ke `skills/bahasa-inti/scripts/periksa.py` beserta satu kasus uji di `tests/test_periksa.py`.
- Daftar kata baku harus sinkron dengan `NONBAKU`/`NONBAKU_UTUH` di pemeriksa inti dan `KATA_BAKU` di pemeriksa akademik; `tests/test_periksa.py` menegakkan yang pertama.
- Jangan hapus catatan keandalan sumber di `sumber/`; perbarui bila ada bukti baru.

## Lisensi dan kredit

MIT. Lihat [`LICENSE`](LICENSE).

Karya turunan dari tiga repo MIT:

- **bahasa-skills** © 2026 Alvin Indra — <https://github.com/alvinindra/bahasa-skills>
- **naskah-id** © 2026 nothinx — <https://github.com/nothinx/naskah-id>
- **unslop** © 2026 claytonkim — <https://github.com/theclaymethod/unslop>

Skill `bahasa-inti`, `bahasa-marketing`, `bahasa-website`, `bahasa-seo`, `sumber/`, `tests/test_periksa.py`, `penelitian/`, dan `CONTOH.md` berasal dari bahasa-skills. `references/jejak-mesin.md` dan `scripts/ritme.py` adalah adaptasi bahasa Indonesia dari pendekatan unslop (metrik irama, pemeriksa struktur), bukan terjemahan berkasnya: daftar frasanya sudah ada di `frasa-terlarang.md`, dan aturan Inggris yang tidak berlaku di bahasa Indonesia (Flesch-Kincaid, partisipial *-ing*, Title Case) dibuang. Isi `skills/bahasa-peneliti/` berasal dari naskah-id, digabung dengan `bahasa-peneliti` versi bahasa-skills. Perubahan penggabungan: satu daftar kata baku (dua daftar lama digabung), satu ringkasan EYD (dua ringkasan lama digabung), satu referensi kalimat akademik (dua referensi lama digabung), dan protokol sitasi dari naskah-id ikut berlaku untuk seluruh kategori yang menyitir sumber.

Folder `skills/bahasa-peneliti/contoh/korpus/` memuat kutipan artikel berlisensi **CC BY-SA 4.0**; lisensi folder itu tercantum di dalamnya dan tidak mengubah lisensi bagian repo yang lain.