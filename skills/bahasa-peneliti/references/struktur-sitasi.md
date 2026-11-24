# Struktur Naskah & Protokol Sitasi

## Anatomi artikel jurnal (IMRaD Indonesia)

| Bagian | Isi wajib | Kesalahan tersering |
|---|---|---|
| Judul | Variabel/fokus + konteks; ±12–15 kata; tanpa singkatan tak umum | Judul setengah kalimat promosi |
| Abstrak | 150–250 kata; lima unsur berurutan (lihat templat) | Tanpa angka hasil; berisi sitasi |
| Kata kunci | 3–5; spesifik topik; alfabetis bila diminta | Kata generik ("analisis", "penelitian") |
| Pendahuluan | Fenomena berdata → riset terdahulu → kesenjangan → tujuan | Pembuka globalisasi; tinjauan pustaka jadi daftar tanpa sintesis |
| Metode | Desain; populasi-sampel + teknik; instrumen + validitas; prosedur; analisis | Terlalu ringkas untuk direplikasi |
| Hasil | Temuan + tabel/gambar; tanpa tafsir | Mengulang seluruh tabel dalam prosa |
| Pembahasan | Makna temuan; dialog dengan riset terdahulu (sepakat/bertentangan + dugaan sebab); keterbatasan | Mengulang hasil tanpa menafsir |
| Kesimpulan | Jawaban rumusan masalah + implikasi + saran spesifik | Merangkum semua bab; saran generik ("perlu penelitian lebih lanjut" tanpa arah) |
| Daftar pustaka | Hanya yang disitasi di teks; gaya konsisten | Sumber tak tersitasi ikut masuk; gaya campur |

Skripsi/tesis memakai bab (Pendahuluan berisi latar belakang, rumusan, tujuan, manfaat; Tinjauan Pustaka terpisah). Struktur mengikuti pedoman kampus; kaidah bahasa tetap sama. Penelitian kualitatif dan humaniora sering tidak memakai pola IMRaD; naskah sejarah bisa kronologis atau tematis. Uraian per bagian ada di [bagian-naskah.md](bagian-naskah.md).

**Tinjauan pustaka = sintesis, bukan daftar.** ❌ "Menurut A (2020)…. Menurut B (2021)…. Menurut C (2022)…." ✅ Kelompokkan per temuan/aliran: "Studi pada UMKM perkotaan konsisten menemukan X (A, 2020; B, 2021), tetapi dua studi di wilayah timur menunjukkan pola sebaliknya (C, 2022)."

## Templat abstrak (150–250 kata)

> [Latar, 1–2 kalimat: fenomena + kesenjangan]. Penelitian ini bertujuan [tujuan]. [Metode: desain, sampel + jumlah, instrumen, analisis]. Hasil menunjukkan [temuan utama dengan angka; 2–3 kalimat]. [Simpulan + implikasi, 1–2 kalimat].

Uji abstrak: pembaca yang hanya membaca abstrak tahu persis apa yang diteliti, bagaimana, apa hasilnya (berapa), dan kenapa penting. Abstrak tidak memuat sitasi dan singkatan yang belum dijelaskan. Abstrak bahasa Inggris adalah terjemahan setara, bukan ringkasan lain; koma desimal Indonesia menjadi titik di versi Inggris. Jangan membuka abstrak dengan pembuka kosmik ([pola-ai.md](pola-ai.md), AI-01).

## Protokol sitasi anti-halusinasi

Referensi fiktif buatan AI punya semua ciri visual referensi asli (nama penulis nyata, jurnal nyata, DOI terformat rapi), tetapi dokumennya tidak ada. Kasus di kampus Indonesia: nama penulis dan jurnal valid, isi kutipan tidak pernah ditulis penulis itu. Karena itu:

1. **Sumber sitasi hanya dua:** diberikan pengguna, atau dibuka-dan-diverifikasi langsung (judul-penulis-tahun-DOI dicek di halaman sumber/basis data). Ingatan model bukan sumber.
2. Klaim yang butuh rujukan tapi belum ada sumber → tulis `[PERLU RUJUKAN: <klaim>; cari di <arah pencarian>]`. Naskah dengan penanda jujur lebih berharga daripada naskah dengan rujukan palsu.
3. Verifikasi per item sebelum masuk daftar pustaka: penulis, tahun, judul, jurnal/penerbit, volume-halaman, DOI aktif. DOI dicek dengan membukanya, bukan dengan menilai formatnya.
4. Kutip hanya yang teksnya benar-benar dibaca (minimal bagian yang dikutip); jangan mengutip abstrak seolah membaca naskah penuh, apalagi mengutip dari sitasi orang lain tanpa membuka sumber aslinya (kalau terpaksa: "A (2019) dalam B (2023)").
5. Angka/statistik selalu dengan tahun data dan lembaga: "(BPS, 2025)", dan diverifikasi sama ketatnya.
6. Saat menyunting, sitasi yang sudah ada tidak diubah, dipindah ke klaim lain, atau dihapus. Bila tampak keliru (tahun tidak cocok, DOI rusak), tanyakan kepada pengguna.

Daftar pustaka tidak pernah disusun dari ingatan. Judul, penulis, tahun, volume, halaman, dan DOI diambil dari metadata, bukan ditebak.

## Mencari dan mengecek rujukan

| Kebutuhan | Alat |
| --- | --- |
| Sintesis temuan: "apa kata riset tentang X" | Consensus |
| Metadata, abstrak, entri APA/IEEE/BibTeX, cek keberadaan, siapa yang mengutip | OpenAlex dan Crossref: `python3 scripts/openalex.py` (cari, doi, rujukan, bib, cek, daftar, dikutip) |
| Kesehatan dan biomedis | PubMed |
| Praterbit | arXiv, alphaXiv |
| Cek DOI | `openalex.py doi` (otomatis ke Crossref), `doi.org` |
| Jurnal Indonesia | Garuda (garuda.kemdiktisaintek.go.id), SINTA, laman OJS jurnalnya |

Cara mengecek satu rujukan:

1. Jalankan `python3 scripts/openalex.py cek "judul" --penulis "…" --tahun …`. Untuk seluruh daftar pustaka sekaligus: `python3 scripts/openalex.py daftar pustaka.txt`.
2. Cocokkan nama jurnal, volume, dan halaman dengan metadata yang dicetak.
3. Baca abstraknya. Pastikan klaim di naskah memang ada di sumber, bukan hanya topiknya mirip.
4. Bila tidak ditemukan di mana pun, anggap rujukan itu tidak ada dan beri penanda.

Banyak jurnal Indonesia tidak memiliki DOI atau belum terindeks OpenAlex. Untuk jurnal seperti itu, cek di laman OJS jurnalnya atau di Garuda. Tidak terindeks tidak sama dengan tidak ada, tetapi rujukan yang tidak bisa ditemukan di mana pun tetap diberi penanda. Entri daftar pustaka disusun dari keluaran `rujukan`, bukan diketik ulang; bila muncul `PERINGATAN: metadata penulis`, salin nama penulis dari PDF artikelnya.

## Gaya sitasi

Ikuti gaya selingkung jurnal/kampus target. Tanpa informasi itu: **APA edisi terbaru**, sebutkan asumsinya. Yang paling sering dipakai di Indonesia:

| Gaya | Bidang yang lazim | Dalam teks | Daftar pustaka |
| --- | --- | --- | --- |
| APA 7 | sosial, pendidikan, psikologi, kesehatan masyarakat | (Santoso, 2021); Santoso (2021) | Santoso, B. (2021). Judul artikel. *Nama Jurnal*, *12*(2), 45–60. https://doi.org/… |
| IEEE | teknik, informatika | [1], [2]–[4] | [1] B. Santoso, "Judul artikel," *Nama Jurnal*, vol. 12, no. 2, hlm. 45–60, 2021. |
| Vancouver | kedokteran, keperawatan | angka superskrip atau (1) | 1. Santoso B. Judul artikel. Nama Jurnal. 2021;12(2):45–60. |
| Chicago (catatan kaki) | sejarah, filsafat, kajian agama | catatan kaki bernomor | sesuai panduan jurnal |

Contoh di atas fiktif dan hanya menunjukkan format.

Yang paling sering salah di APA Indonesia: "dkk." vs "et al." (ikuti pedoman target; APA asli memakai et al.), tanda "&" vs "dan" (dalam kurung: &; dalam kalimat: dan), urutan alfabetis daftar pustaka, kapitalisasi judul artikel di daftar pustaka (gaya APA: hanya kata pertama + nama diri; ini aturan gaya sitasi, berbeda dari judul naskah yang mengikuti EYD V atau gaya selingkung jurnal). Dalam naskah berbahasa Indonesia, "dkk." dipakai untuk *et al.*, dan "hlm." untuk halaman, kecuali templat jurnal memakai bentuk Inggris.

Konsistensi total: satu gaya untuk semua entri. Sarankan Mendeley/Zotero; banyak jurnal Indonesia mewajibkannya. Sitasi dalam teks harus 1:1 dengan daftar pustaka: semua yang dikutip ada di daftar; semua di daftar dikutip.

## Menyitir dalam kalimat

- Jadikan sumber subjek bila klaimnya khas sumber itu: "Wibowo dkk. [3] mengukur …".
- Untuk fakta yang sudah mapan, cukup cantumkan rujukan di akhir kalimat.
- Pakai verba pelapor yang sesuai: *mengukur, menemukan, mengusulkan, membantah, memperluas, mengkritik, merangkum*. "Mengatakan" dan "menyatakan" untuk semua sumber terasa datar.
- Hindari deretan sumber yang masing-masing satu kalimat. Kelompokkan menurut temuan, lalu tunjukkan perbedaannya. Lihat contoh di [`contoh/`](../contoh/).
- Jangan menulis "Menurut X mengatakan". Pilih salah satu: "Menurut X, …" atau "X mengatakan …".

## Kutipan langsung

Kutipan langsung di bawah empat baris ditulis di dalam teks dengan tanda petik dan nomor halaman. Kutipan yang lebih panjang ditulis sebagai blok terpisah tanpa tanda petik. Ikuti batas yang ditetapkan gaya sitasi sasaran. Kutipan tidak pernah disunting.

## Bagian pendukung

- **Ucapan terima kasih/pendanaan**: sebut hibah + nomor kontrak bila ada.
- **Pernyataan etik**: penelitian dengan subjek manusia menyebut persetujuan etik + *informed consent*. Nomor persetujuan etik berasal dari pengguna; bila belum ada, tulis `[PERLU DATA: nomor persetujuan etik]`.
- **Keterbukaan AI**: bila jurnal target punya kebijakan pemakaian AI, patuhi. Umumnya AI tidak boleh jadi penulis, dan pemakaiannya dinyatakan di bagian metode/acknowledgment. Templat pernyataan ada di [KONTRAK.md](../KONTRAK.md).

## Judul

- Memuat variabel atau fokus utama, subjek, dan konteks. Hindari kata "Studi tentang", "Analisis terhadap", dan pembuka sejenis bila tidak perlu.
- Ikuti batas kata jurnal sasaran. Banyak jurnal meminta judul di bawah 15 kata.