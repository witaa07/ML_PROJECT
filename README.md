# UNSRAT Weather Assistant 
Aplikasi prediksi cuaca real-time untuk membantu mahasiswa UNSRAT membuat keputusan harian yang lebih baik — seperti apakah perlu membawa payung, bagaimana suhu beberapa jam ke depan, dan seberapa besar peluang hujan di area kampus.

---

## Tujuan Proyek
1. Memberikan prediksi cuaca real-time berbasis data API BMKG melalui pipeline n8n → Google Sheets → Streamlit.
2. Menyediakan rekomendasi langsung (actionable) tanpa pengguna harus membaca data mentah.
3. Membantu mahasiswa mengambil keputusan harian seperti:
   - “Perlu bawa payung atau tidak?”
   - “Bagaimana suhu sore hari untuk kegiatan kampus?”
   - “Apakah hujan akan turun dalam 1–3 jam ke depan?”

---

## Roles & Tugas Tim
### **Person 1 — Data Engineer**
- Membuat pipeline n8n untuk mengambil data cuaca real-time dari API BMKG.
- Sinkronisasi otomatis ke Google Sheets (cron per 1–6 jam).
- Menjamin data selalu terbaru dan tidak basi.

### **Person 2 — Data Analyst & Modeler**
- Mengumpulkan data historis dari BMKG, Kaggle, NOAA.
- Melakukan EDA, data cleaning, dan feature engineering.
- Melatih model prediksi cuaca (temperature, rain probability, dll).
- Menyediakan output model untuk integrasi ke Streamlit.

### **Person 3 — Project Manager & Deployment (Sabdawita)**
- Membuat kerangka UI Streamlit (dummy terlebih dahulu).
- Menyusun interaksi pengguna + rekomendasi.
- Integrasi model dan data setelah siap.
- Menyiapkan aplikasi untuk deployment.

---
