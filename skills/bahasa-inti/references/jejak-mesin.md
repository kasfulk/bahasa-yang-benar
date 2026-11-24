# Jejak Mesin: Irama dan Struktur yang Membuat Teks Terbaca AI

Berkas ini mengurus satu hal yang tidak diperiksa [periksa.py](../scripts/periksa.py):
**struktur dan irama**, bukan kosakata. Daftar frasa terlarang ada di
[frasa-terlarang.md](frasa-terlarang.md); pemeriksa kata ada di `periksa.py`. Yang di sini
adalah pola yang baru kelihatan saat seluruh teks dibaca: variasi panjang kalimat, pembuka
kalimat yang berulang, paragraf yang bergerak dengan kata penghubung, penutup ritual, dan daftar
tiga serangkai.

Pemeriksa otomatisnya: [../scripts/ritme.py](../scripts/ritme.py).

## Posisi

Detektor AI bekerja dari dua hal: seberapa mudah kata berikutnya ditebak (perplexity), dan
seberapa seragam panjang serta bentuk kalimat (burstiness). Dua-duanya konsekuensi dari tulisan
yang datar, bukan bukti pemakaian alat. Maka:

- **Yang diperbaiki adalah tulisannya.** Naikkan spesifisitas, variasikan irama, buang kalimat
  kosong. Skor detektor ikut turun karena teksnya memang lebih baik.
- **Yang tidak dilakukan:** memutar sinonim, menyisipkan salah tulis, memecah kalimat secara
  acak, atau memakai alat "humanizer". Itu merusak teks tanpa memperbaiki apa pun, dan tetap
  terdeteksi karena polanya cuma bergeser.
- **Detektor bisa salah menuduh tulisan manusia**, terutama penulis yang bahasa ibunya bukan
  Inggris atau yang menulis dengan struktur formulaik karena disiplin ilmunya. Skor detektor
  bukan ukuran mutu dan bukan bukti pelanggaran.
- **Keterbukaan tetap wajib** bila kebijakan jurnal atau kampus memintanya. Lihat
  [../../bahasa-peneliti/KONTRAK.md](../../bahasa-peneliti/KONTRAK.md).

## 1. Irama: panjang kalimat yang seragam

Tanda terkuat dan paling mudah diukur. Tulis 20 kalimat yang panjangnya 18–22 kata, dan teksnya
terbaca mesin walau setiap kalimat benar.

Ukur dengan **koefisien variasi** (simpangan baku dibagi rata-rata) panjang kalimat:

| Nilai | Tafsiran |
|---|---|
| ≥ 0,55 | Wajar untuk prosa manusia |
| 0,40–0,55 | Agak rata; periksa beberapa kalimat |
| < 0,40 pada 8 kalimat atau lebih | Terlalu seragam; hampir pasti terbaca mesin |

Cara memperbaiki bukan dengan memotong kalimat secara acak, melainkan dengan **menulis sesuai
gagasan**: gagasan utama dalam kalimat pendek, penjelasannya dalam kalimat panjang, dan
sebaliknya. Satu kalimat pendek berdiri sendiri setelah tiga kalimat panjang adalah irama, bukan
kesalahan.

## 2. Pembuka kalimat yang berulang

Bila empat kalimat beruntun dibuka kata yang sama ("Sistem ini… Sistem ini… Sistem ini…"), atau
satu kata pembuka dipakai lebih dari seperempat kalimat, itu pola. Perbaiki dengan menyebut
subjek yang berbeda, membalik susunan, atau menggabungkan dua kalimat.

Pengecualian sah: dokumen prosedur yang setiap langkahnya dibuka verba perintah ("Buka… Pilih…
Simpan…"), dan daftar bernomor. Jangan dipaksakan variasinya.

## 3. Paragraf yang bergerak dengan kata penghubung

Tiga paragraf beruntun dibuka `Namun,` / `Selain itu,` / `Oleh karena itu,` berarti paragrafnya
tidak bergerak karena isi, melainkan karena rambu. Perbaiki dengan kalimat topik yang menyebut
bendanya: bukan "Selain itu, biaya juga turun", melainkan "Biaya per transaksi turun 40%".

Kata penghubung tetap sah sekali-sekali, terutama saat arah argumen benar-benar berbalik.

## 4. Penutup ritual dan pengulangan pembuka

Dua pola yang sering berpasangan:

- **Coda:** paragraf terakhir yang membuka dengan `Kesimpulannya,` / `Dengan demikian,` /
  `Secara keseluruhan,` / `Jadi,` lalu merangkum ulang pendahuluan. Ganti dengan satu fakta atau
  keputusan konkret yang menjadi ujung tulisan.
- **Bingkai ulang:** paragraf terakhir mengulang dua bigram isi dari paragraf pertama. Itu tanda
  teks disusun dari templat "katakan apa yang akan dikatakan, katakan, katakan apa yang sudah
  dikatakan".

Pengecualian: abstrak, ringkasan eksekutif, dan laporan resmi memang meringkas. Nilai genre
sebelum mengubahnya.

## 5. Staccato

Enam paragraf atau lebih yang isinya satu kalimat pendek (di bawah 12 kata) berturut-turut.
Terbaca seperti slide, bukan tulisan. Gabungkan yang bergagasan sama.

Caption media sosial dan naskah iklan kadang memang begini; itu sah bila mediumnya menuntut.

## 6. Tanda baca dan format yang tampil sebagai gaya

Lima hal diukur di sini, semuanya soal tampilan, bukan isi.

Tanda pisah yang menumpuk: satu per seribu kata sudah mencolok, dan sebaiknya diganti koma,
kurung, atau titik. Bentuk larangannya ada di `L10` pada [frasa-terlarang.md](frasa-terlarang.md).

Titik dua berlabel tebal, seperti `**Label:** penjelasan`, yang muncul tiga kali atau lebih dalam
satu bagian. Ubah jadi prosa atau butir biasa.

Tanda seru lebih dari satu per 500 kata; sisakan paling banyak satu per bagian.

Emoji sebagai penanda butir di teks yang bukan media sosial.

Kapital tiap kata di badan teks. EYD V hanya mengatur judul; badan teks memakai kapital di awal
kalimat dan nama diri.

## 7. Daftar tiga serangkai dan paralelisme negatif

Dua pola paling khas, keduanya sudah dilarang di [frasa-terlarang.md](frasa-terlarang.md) (L3,
L4). Yang perlu diukur di sini adalah **kepadatan**-nya:

- Tiga kata sifat berderet (`L4` di daftar terlarang) lebih dari sekali per 500 kata.
- `bukan hanya X, tetapi juga Y` / `bukan X, melainkan Y` lebih dari sekali.
- `tidak hanya … tetapi` di awal dan akhir paragraf yang sama.

Satu kali masih bisa jadi pilihan retoris. Tiga kali adalah templat.

## 8. Nominalisasi beruntun

Tiga nomina tindakan dalam satu paragraf ("pengumpulan, pengolahan, dan penyajian data") wajar
bila memang membahas prosedur. Yang jadi jejak mesin adalah campuran acak: verba, nomina, lalu
verba lagi dalam satu rincian. Rincian harus sejajar bentuknya.

## 9. Klaim lebih kabur daripada datanya

Ini paling merusak di naskah ilmiah, dan paling sering lolos dari pemeriksa kata:

| Terbaca mesin | Yang seharusnya |
|---|---|
| "berdampak signifikan terhadap kinerja" | "menaikkan throughput 12% (p = 0,003)" |
| "responden memberikan tanggapan positif" | "18 dari 24 responden memilih opsi pertama" |
| "hasil penelitian ini sangat menjanjikan" | sebut angkanya, lalu hentikan kalimat |
| "berbagai faktor memengaruhi hasil" | sebut faktor yang diukur dan yang tidak |
| "perlu penelitian lebih lanjut" | sebut pertanyaan persis yang belum terjawab |

Aturannya: **kalau ada angkanya, tulis angkanya.** Kalau tidak ada, jangan menulis kalimat yang
mengaburkan ketiadaan itu.

## 10. Jangan diperbaiki berlebihan

Beberapa hal yang tampak seperti jejak mesin, padahal bukan:

- **Kata teknis yang berulang.** Menyebut *responden* sepuluh kali itu benar. Menggantinya
  bergantian dengan *partisipan*, *subjek*, dan *informan* (elegant variation) justru membuat
  naskah ambigu dan terbaca disusun mesin.
- **Pasif di bagian Metode.** "Sampel diambil dengan…" adalah konvensi, bukan kelemahan.
- **Kalimat pendek yang tegas** setelah kalimat panjang. Itu irama yang baik.
- **Kutipan langsung, judul karya, nama diri, dan istilah asing bercetak miring.**
- **Pengulangan sengaja** untuk penegasan dalam teks lisan atau motivasi.
- **Penghubung yang memang menandai hubungan logis** yang tidak bisa dinyatakan cara lain.

## 11. Mengukur

```bash
python3 scripts/ritme.py draf.md
python3 scripts/ritme.py --genre sosial caption.txt
python3 scripts/ritme.py --json draf.md
```

Skrip mencetak **skor jejak mesin 0–100** (makin tinggi makin datar) beserta temuan per metrik.
Ambang batas: `< 15` bersih, `15–35` ada beberapa pola, `35–60` banyak, `> 60` parah. Dengan
`--ketat`, kode keluar 1 bila skor ≥ 35 (untuk CI).

Skor itu petunjuk, bukan putusan, dan tidak mengukur apakah teks ditulis mesin. Yang diukur hanya
kereguleran bentuk. Spesifitas dan dasar klaim tetap harus dibaca.