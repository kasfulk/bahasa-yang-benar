# Kalimat Akademik: Pola Kesalahan dan Perbaikan

Urutan prioritas mengikuti data kesalahan skripsi: struktur kalimat dulu, lalu ejaan, lalu diksi.
Rujukan utama: *Tata Bahasa Baku Bahasa Indonesia* (Alwi dkk., ed. IV, 2017) dan
*Kalimat Efektif Bahasa Indonesia* (Pusat Bahasa, 1995). Kode KE-xx, NM-01, KL-01, dan KK-01
sama dengan keluaran `scripts/periksa.py`.

## 1. Struktur (kesalahan terbesar: 34%)

### KE-01 · Subjek berkata depan (K)

Kata depan mengubah calon subjek menjadi keterangan sehingga kalimat tidak bersubjek. Buang kata
depannya, atau pertahankan kata depan dan ubah verbanya menjadi pasif.

| Salah | Benar |
|---|---|
| Dalam penelitian ini menunjukkan bahwa … | Penelitian ini menunjukkan bahwa … *Atau:* Dalam penelitian ini ditunjukkan bahwa … |
| Berdasarkan hasil analisis menyatakan … | Hasil analisis menyatakan … / Berdasarkan hasil analisis, … |
| Dari data tersebut membuktikan … | Data tersebut membuktikan … |
| Menurut Sugiyono (2019) mengatakan bahwa … | Menurut Sugiyono (2019), … / Sugiyono (2019) mengatakan bahwa … |
| Untuk mengetahui pengaruh X maka dilakukan uji t | Untuk mengetahui pengaruh X, peneliti melakukan uji t / …, uji t dilakukan |
| Pada Gambar 3 memperlihatkan … | Gambar 3 memperlihatkan … |
| Bagi peserta yang … | Peserta yang … |

### Kalimat tanpa pelaku dan tanpa pasif (K)

- **Sebelum:** Untuk mengukur tekanan darah menggunakan tensimeter digital.
- **Sesudah:** Tekanan darah diukur dengan tensimeter digital.

### Pasif bertumpuk (G)

- **Sebelum:** Pengujian dilakukan oleh peneliti terhadap instrumen yang telah disusun oleh tim yang dibentuk oleh jurusan.
- **Sesudah:** Tim jurusan menyusun instrumen, lalu peneliti mengujinya.

### Pembuka "Adapun" (G)

- **Sebelum:** Adapun tujuan penelitian ini adalah untuk mengetahui pengaruh …
- **Sesudah:** Penelitian ini bertujuan mengukur pengaruh …

### Kalimat beranak-cucu

Dipecah per gagasan. Kalimat di atas 35 kata ditandai `KL-01 (G)` oleh `periksa.py`.

> ❌ "Media sosial yang saat ini berkembang sangat pesat di kalangan remaja yang mana penggunaannya tidak terkontrol sehingga dapat menimbulkan berbagai dampak negatif yang tentunya sangat merugikan bagi perkembangan psikologis remaja itu sendiri."
> ✅ "Penggunaan media sosial pada remaja meningkat pesat dan sering tidak terkontrol. Kondisi ini berisiko mengganggu perkembangan psikologis mereka."

**Konjungsi ganda:** *meskipun … tetapi* (KE-14), *karena … maka* (KE-15), *walaupun … namun* → pakai satu.

**"di mana / yang mana" sebagai penghubung** (AI-13, AI-14) → *yang, tempat, saat, sehingga*, atau pecah kalimat. Ini kesalahan paling sering pada parafrase dari sumber berbahasa Inggris.

## 2. Perangkai

| Kode | Kaku atau salah | Baku | Label |
|---|---|---|---|
| KE-10 | `berdasarkan pada hasil uji` | berdasarkan hasil uji | K |
| | `terdiri dari tiga bab` | terdiri atas tiga bab (anjuran Badan Bahasa) | G |
| KE-11 | `antara A dengan B` | antara A dan B | K |
| KE-12 | `baik A ataupun B`, `baik A dan B` | baik A maupun B | K |
| KE-13 | `bukan A, tetapi B` | bukan A, melainkan B; tidak A, tetapi B | K |
| KE-14 | `Meskipun mahal, tetapi awet.` | Meskipun mahal, alat ini awet. | K |
| KE-15 | `Karena hujan, maka panen gagal.`, `Berdasarkan uraian di atas, maka …` | Karena hujan, panen gagal. Berdasarkan uraian di atas, … | K |
| | `Jika …, maka …` | "maka" boleh, tetapi biasanya mubazir | G |
| KE-16 | `Sehingga …` / `Sedangkan …` di awal kalimat | gabungkan dengan kalimat sebelumnya, atau pakai Akibatnya / Adapun | K |
| KE-17 | `lebih baik dari` | lebih baik daripada | K |
| | `Daripada itu, …` | Selain itu, … | K |
| | `Namun demikian, …` | Namun, … / Meskipun demikian, … | G |
| | `Dikarenakan …` | Karena … | G |
| | `dalam rangka meningkatkan` | untuk meningkatkan | G |

### "sehingga" tanpa koma

"Sehingga" adalah konjungsi intrakalimat. EYD V (Tanda Koma, kaidah 4) menyatakan bahwa koma
tidak dipakai bila induk kalimat mendahului anak kalimat. EYD V tidak menyebut "sehingga"
secara khusus, tetapi anak kalimat akibat yang diawali "sehingga" mengikuti kaidah itu, jadi tulis "Galat menurun sehingga akurasi naik", bukan dengan koma sebelum
"sehingga". Bila ingin memulai kalimat baru, pakai "Akibatnya," atau "Karena itu,".

Koma tetap dipakai sebelum konjungsi pertentangan: "tetapi", "melainkan", "sedangkan".

## 3. Kehematan dan nominalisasi

Kode NM-01 (G). Verba penopang ("melakukan", "mengalami", "memberikan") ditambah nomina membuat kalimat
panjang tanpa menambah makna. Pakai verbanya langsung.

| Boros | Hemat |
|---|---|
| adalah merupakan (KE-02) | adalah / merupakan |
| disebabkan karena | disebabkan oleh / karena |
| agar supaya, demi untuk, sejak dari (KE-03) | agar; supaya; demi; untuk; sejak |
| berdasarkan kepada | berdasarkan |
| dalam rangka untuk | untuk |
| sangat … sekali (KE-04) | sangat … |
| para responden-responden, banyak data-data (KE-05) | para responden / responden |
| berbagai macam metode (KE-06) | berbagai metode; bermacam-macam metode |
| naik ke atas, mundur ke belakang (KE-07) | naik; mundur |
| saling tolong-menolong (KE-08) | tolong-menolong; saling menolong |
| seperti: A, B, dan lain-lain (KE-09) | seperti A dan B; antara lain A dan B |
| masih … hingga kini | masih …; … hingga kini |
| Dengan demikian dapat disimpulkan bahwa | Jadi, …; Simpulannya, … |
| hasil daripada penelitian | hasil penelitian |
| melakukan analisis terhadap data | menganalisis data |
| melakukan pengukuran | mengukur |
| melakukan perbandingan antara | membandingkan |
| mengalami peningkatan sebesar 12% | naik 12% |
| memberikan pengaruh terhadap | memengaruhi |
| telah dilakukan pengujian terhadap sampel | sampel diuji |
| Penelitian ini bertujuan untuk mengetahui | Penelitian ini bertujuan mengukur / menguji / membandingkan |

Nominalisasi tetap wajar bila nominanya memang pokok bahasan: "Hasil **analisis** regresi menunjukkan…" benar; "peneliti **melakukan analisis** regresi" → "peneliti **menganalisis** dengan regresi" lebih tajam. Keduanya baku; pilih yang lebih langsung, konsisten.

## 4. Keparalelan

> ❌ "Tahapan penelitian meliputi pengumpulan data, mengolah data, dan data dianalisis."
> ✅ "Tahapan penelitian meliputi pengumpulan, pengolahan, dan analisis data."

Rincian bernomor juga paralel: semua butir mulai verba, atau semua nomina; jangan campur.

## 5. Kelogisan dan kekuatan klaim

Kode KK-01 menandai `membuktikan` agar kekuatannya dicek.

- "Waktu dan tempat kami persilakan" → "Bapak X kami persilakan".
- Persentase dan angka harus konsisten dengan teks: "mayoritas (43%)" salah, karena 43% bukan mayoritas.
- Korelasi ≠ kausalitas: "berhubungan dengan" ≠ "menyebabkan"; pilih verba sesuai desain penelitian (eksperimen boleh "menyebabkan"; survei korelasional "berkaitan/berasosiasi"). `menunjukkan` tidak sama dengan `membuktikan`.
- Generalisasi sesuai sampel: sampel 40 mahasiswa satu kampus tidak menghasilkan "remaja Indonesia".
- "Signifikan" hanya dalam arti statistik dan disertai nilai ujinya.

## 6. Diksi akademik

| Hindari | Pakai |
|---|---|
| bikin, banget, nggak, kayak | membuat, sangat, tidak, seperti |
| dll./dsb. di kalimat penting | sebutkan lengkap, atau "antara lain" dengan sadar |
| kata emosional: mencengangkan, luar biasa, sayangnya | laporkan angka dan biarkan pembaca menilai |
| klaim mutlak: pasti, tidak diragukan lagi, semua orang | temuan menunjukkan…, sebagian besar responden… |
| "signifikan" sebagai kata gaya | hanya untuk hasil uji statistik + nilai p |
| "efektif/berpengaruh" tanpa ukuran | sebut besaran efeknya |

Penanda ketidakpastian dipakai **satu lapis** dan jujur: "temuan ini **mengindikasikan**…" (bukan "mungkin dapat cenderung mengindikasikan"). Hedging yang sah — *diduga, cenderung, kemungkinan* — jangan dihapus.

Verba pelapor: pilih yang tepat, bukan *mengatakan* untuk semua sumber. *Mengukur, menemukan, mengusulkan, membantah, memperluas, mengkritik, merangkum*.

## 7. Parafrase yang benar

Parafrase kosmetik (menukar sinonim, menggeser urutan kata) tetap plagiarisme struktur, dan biasanya melahirkan "yang mana/di mana" serta kalimat rancu. Prosedur yang benar:

1. Baca bagian sumber sampai bisa menjelaskan tanpa melihat.
2. Tutup sumber; tulis ulang dari pemahaman, dalam struktur kalimat sendiri.
3. Buka sumber; cek akurasi makna dan pastikan tak meminjam frasa khas.
4. Pasang sitasi. Kutipan langsung (dengan tanda petik + halaman) hanya untuk definisi/pernyataan yang rumusannya penting.

## 8. Tabel, gambar, lampiran

- Setiap tabel/gambar dirujuk di teks ("Tabel 3 menyajikan…") dan diberi nomor + judul mandiri (dipahami tanpa membaca teks).
- Teks tidak mengulang seluruh isi tabel; soroti pola pentingnya saja.
- Satuan dan format angka konsisten (desimal koma untuk naskah Indonesia: 0,05).