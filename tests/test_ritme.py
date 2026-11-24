"""Uji pemeriksa irama (ritme.py). Jalankan: python3 -m unittest discover -s tests"""

import pathlib
import sys
import unittest

AKAR = pathlib.Path(__file__).resolve().parent.parent
INTI = AKAR / "skills" / "bahasa-inti"
sys.path.insert(0, str(INTI / "scripts"))
import ritme  # noqa: E402


def metrik(teks, genre="prosa"):
    return {t["metrik"] for t in ritme.periksa(teks, genre)["temuan"]}


DATAR = (
    "Sistem ini bertujuan untuk meningkatkan efisiensi proses pencatatan data pada instansi "
    "pemerintahan di seluruh wilayah kerja. Sistem ini menggunakan pendekatan digital dalam "
    "melakukan pengolahan data yang selama ini dilakukan secara manual. Sistem ini juga "
    "menyediakan fitur pelaporan otomatis yang dapat diakses oleh pengguna dengan hak akses "
    "tertentu.\n\n"
    "Sistem ini diharapkan dapat mengurangi beban kerja petugas dalam melakukan pencatatan "
    "data secara harian. Sistem ini telah diuji pada tiga instansi pemerintahan dengan jumlah "
    "pengguna yang cukup beragam. Sistem ini menghasilkan peningkatan efisiensi yang cukup "
    "signifikan pada seluruh instansi yang mengikuti pengujian tersebut.\n\n"
    "Sistem ini juga dilengkapi dengan modul pelaporan yang dapat disesuaikan dengan kebutuhan "
    "masing-masing instansi pengguna. Modul pelaporan tersebut menyajikan data dalam bentuk "
    "tabel dan grafik yang mudah dipahami oleh pengguna.\n\n"
    "Kesimpulannya, sistem ini layak untuk diadopsi oleh instansi pemerintahan yang ingin "
    "meningkatkan efisiensi pencatatan data secara berkelanjutan."
)

ALAMI = (
    "Pencatatan manual di tiga kecamatan memakan 15 menit per berkas. Kami mengukurnya selama "
    "dua minggu, dengan stopwatch, di meja loket yang sama.\n\n"
    "Angkanya beragam. Loket pertama rata-rata 12 menit, loket ketiga 21 menit. Sebabnya bukan "
    "petugas, melainkan buku register yang harus dicari dulu ke ruang belakang setiap kali ada "
    "berkas baru masuk.\n\n"
    "Setelah register dipindahkan ke depan, rata-ratanya turun jadi 9 menit. Tidak ada "
    "pelatihan, tidak ada perangkat baru, dan tidak ada anggaran yang keluar."
)


class Irama(unittest.TestCase):
    def test_teks_datar_terdeteksi(self):
        m = metrik(DATAR)
        self.assertIn("irama_seragam", m)
        self.assertIn("pembuka_berulang", m)
        self.assertIn("penutup_ritual", m)
        self.assertGreaterEqual(ritme.periksa(DATAR)["skor_jejak_mesin"], 15)

    def test_teks_alami_bersih(self):
        hasil = ritme.periksa(ALAMI)
        self.assertEqual([], hasil["temuan"])
        self.assertLess(hasil["skor_jejak_mesin"], 15)

    def test_staccato_dan_genre(self):
        stacc = "\n\n".join(["Pagi."] * 8)
        self.assertIn("staccato", metrik(stacc))
        self.assertNotIn("staccato", metrik(stacc, "sosial"))

    def test_tanda_pisah_dan_paralelisme(self):
        self.assertIn("tanda_pisah", metrik("A — B — C — D — E — F — G."))
        paralel = ("Bukan hanya cepat, tetapi juga murah. " * 2
                   + "Ini bukan pilihan, melainkan keharusan. " * 2)
        self.assertIn("paralelisme_negatif", metrik(paralel))

    def test_kode_dan_judul_dilewati(self):
        teks = "```\nKesimpulannya, sistem ini layak. Sistem ini bagus.\n```\n\n# Kesimpulannya\n\nIsi biasa."
        self.assertNotIn("penutup_ritual", metrik(teks))

    def test_singkatan_tidak_memotong_kalimat(self):
        # "Prof." dan "dr." menyambung; "dll." boleh menutup kalimat.
        k = ritme.pecah_kalimat("Menurut Prof. Santoso, angkanya naik. Data diambil dari BPS.")
        self.assertEqual(2, len(k))
        self.assertIn("dll. Ini kalimat baru", " ".join(ritme.pecah_kalimat(
            "Alat yang dipakai: sensor, kabel, dll. Ini kalimat baru.")))


if __name__ == "__main__":
    unittest.main()