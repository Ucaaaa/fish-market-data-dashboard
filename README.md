# Fish Market Data Dashboard

Dashboard berbasis web untuk mengeksplorasi dan memvisualisasikan dataset ikan. Aplikasi dibuat menggunakan **Python**, **Flask**, **Pandas**, dan **Chart.js**.

Pengguna dapat melihat ringkasan data, membandingkan rata-rata berat antarspesies, mengeksplorasi hubungan panjang dan berat ikan, serta membandingkan karakteristik ukuran ikan. Dashboard juga menyediakan filter berdasarkan spesies.

## Fitur

- Ringkasan jumlah data ikan dan jumlah spesies.
- Informasi rata-rata serta berat maksimum ikan.
- Grafik rata-rata berat berdasarkan spesies.
- Scatter plot hubungan panjang (`Length1`) dan berat (`Weight`).
- Grafik perbandingan karakteristik ukuran ikan.
- Filter data berdasarkan spesies.
- Endpoint JSON sederhana untuk menyajikan data grafik.

## Teknologi

- Python 3.10+
- Flask
- Pandas
- HTML dan CSS
- JavaScript
- Chart.js 4.4.1 (dimuat melalui CDN)

## Struktur proyek

```text
fish-dashboard/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   └── fish.csv
├── screenshots/
│   └── README.md
└── templates/
    └── dashboard.html
```

## Menjalankan proyek secara lokal

Pastikan Python sudah terpasang. Jalankan perintah berikut dari folder proyek.

**1. Buat virtual environment**

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**2. Pasang dependensi**

```bash
python -m pip install -r requirements.txt
```

**3. Jalankan aplikasi**

```bash
python app.py
```

**4. Buka dashboard**

Kunjungi alamat berikut melalui browser:

```text
http://127.0.0.1:5000
```

Untuk menghentikan server, tekan `Ctrl + C` pada terminal.

## Endpoint API

| Endpoint | Keterangan |
|---|---|
| `/api/ringkasan` | Ringkasan data ikan |
| `/api/berat-spesies` | Rata-rata berat berdasarkan spesies |
| `/api/panjang-berat` | Data hubungan panjang dan berat |
| `/api/ukuran-ikan` | Rata-rata karakteristik ukuran ikan |

Semua endpoint API mendukung parameter filter `species`. Contoh:

```text
/api/ringkasan?species=Bream
```

## Dataset

Dataset utama berada di `data/fish.csv`. Kolom yang digunakan:

- `Species`: spesies ikan.
- `Weight`: berat ikan.
- `Length1`, `Length2`, `Length3`: pengukuran panjang ikan.
- `Height`: tinggi ikan.
- `Width`: lebar ikan.

## Screenshots

Folder `screenshots/` disediakan untuk dokumentasi tampilan aplikasi. Tambahkan tangkapan layar dashboard setelah aplikasi dijalankan, lalu tampilkan di bagian ini. Panduan penamaan dan penambahannya tersedia di `screenshots/README.md`.

## Catatan

- Dependensi Python dicantumkan di `requirements.txt`; folder virtual environment tidak perlu diunggah ke GitHub.
- Grafik Chart.js memerlukan koneksi internet karena library dimuat dari CDN.
- `debug=True` digunakan untuk pengembangan lokal. Jangan gunakan mode debug untuk deployment publik.

## Pengembangan

Silakan fork repository ini atau buat branch untuk mengembangkan fitur baru.
