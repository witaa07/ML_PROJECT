# ML Project: Prediksi Waktu Tempuh Rute UNSRAT ke Mantos

## Deskripsi Singkat
Proyek ini bertujuan untuk memprediksi **waktu tempuh perjalanan** dari UNSRAT ke Mantos menggunakan data historis perjalanan.  
Aplikasi dibuat dengan **Streamlit** untuk memudahkan pengguna meng-input data perjalanan dan menampilkan prediksi secara interaktif.

## Minggu 1: Inisiasi & Eksplorasi Data
- **Business Understanding:** memprediksi waktu tempuh rute UNSRAT ke Mantos
- **Data Understanding:** fitur yang digunakan (Hari, Jam, Rute), target (Menit)

---

## Fitur & Mock-Up Streamlit
### Input (di sidebar)
- File CSV berisi data perjalanan (opsional untuk upload dataset besar)
- Dropdown untuk memilih hari
- Slider untuk jam keberangkatan
- Dropdown atau pilihan rute
- Tombol “Prediksi Waktu Tempuh”

### Output (di main area)
- Tabel preview data (contoh 5 baris pertama)
- Prediksi waktu tempuh (Menit)
- Grafik visualisasi distribusi waktu tempuh
- Tombol download hasil prediksi (CSV)

---


## Mock-Up Visual Streamlit (Teks)
```text
Sidebar:
+---------------------------+
| [Upload CSV]             |
| [Select Day ▼]           |
| Select Hour: [---●---------] 14   <-- slider
| [Select Route ▼]         |
| [Run Prediction]         |
+---------------------------+

Main Area:
+-------------------------------------------+
| ML Project Dashboard                      |
|-------------------------------------------|
| Table Preview (5 rows sample)            |
| Predicted Travel Time: XX minutes        |
| Chart Visualization (Histogram / Line)   |
| [Download Result Button]                 |
+-------------------------------------------+

Struktur Folder (Awal)
```text
ML_PROJECT/
│
├── README.md
├── app.py                # Streamlit app
├── requirements.txt
├── data/                 # Dataset
│   └── dataset.csv
└── model/                # Model ML (nanti)
    └── model.pkl

