<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<header>
    <h1>🌤️ UNSRAT Climate AI</h1>
    <p>Hyper-local Campus Weather Forecasting System</p>
    <div class="badges">
        <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python" alt="Python">
        <img src="https://img.shields.io/badge/Streamlit-App-ff4b4b?style=flat-square&logo=streamlit" alt="Streamlit">
        <img src="https://img.shields.io/badge/Model-XGBoost-orange?style=flat-square" alt="XGBoost">
        <img src="https://img.shields.io/badge/Pipeline-n8n-FF6B6B?style=flat-square" alt="n8n">
    </div>
</header>

<section id="background">
    <h2>🧐 Latar Belakang</h2>
    <p>Cuaca di daerah tropis seperti Manado sering berubah secara cepat dan bersifat lokal (<i>micro-climate</i>). Informasi prakiraan cuaca umum seringkali kurang spesifik untuk kebutuhan harian mahasiswa. Proyek ini bertujuan membangun sistem <b>End-to-End</b> yang tidak hanya memprediksi angka cuaca, tetapi memberikan <b>Rekomendasi Aksi (<i>Actionable Insights</i>)</b> secara <i>real-time</i> yang spesifik untuk area Kampus UNSRAT Bahu.</p>
</section>

<section id="architecture">
    <h2>🏗 Arsitektur Solusi</h2>
    <p>Sistem ini terdiri dari tiga komponen utama yang saling terintegrasi:</p>
    <ol>
        <li><b>Automated Data Pipeline (n8n):</b> Mengambil data cuaca aktual dari API BMKG setiap jam dan menyimpannya ke <i>Cloud Database</i> (Google Sheets).</li>
        <li><b>Machine Learning Engine (XGBoost):</b> Memproses data historis dan input <i>real-time</i> untuk memprediksi kondisi masa depan.</li>
        <li><b>Interactive Dashboard (Streamlit):</b> Antarmuka pengguna untuk menampilkan prediksi dan rekomendasi cerdas.</li>
    </ol>
</section>

<section id="methodology">
    <h2>🧠 Metodologi & Pendekatan Teknis</h2>
    
    <h3>1. Direct Multi-step Forecasting</h3>
    <p>Alih-alih menggunakan metode <i>Recursive</i> yang rentan error, kami melatih <b>model terpisah</b> untuk setiap horizon waktu (T+1, T+3, T+6 jam).</p>

    <h3>2. Hybrid Strategy (Suhu vs Hujan)</h3>
    <ul>
        <li><b>Suhu:</b> Dimodelkan menggunakan <b>Regresi</b> (<code>XGBRegressor</code>).</li>
        <li><b>Hujan:</b> Dimodelkan menggunakan <b>Klasifikasi</b> (<code>XGBClassifier</code>) dengan penyesuaian <i>threshold</i> (>5mm) untuk mengatasi data <i>imbalanced</i>.</li>
    </ul>
</section>

<section id="evaluation">
    <h2>📊 Evaluasi Model</h2>
    <p>Model dievaluasi menggunakan data <i>hold-out</i> (Januari 2025 - Sekarang).</p>
    <table>
        <thead>
            <tr>
                <th>Horizon Waktu</th>
                <th>MAE Suhu (°C)</th>
                <th>Akurasi Hujan</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><b>1 Jam (T+1)</b></td>
                <td>0.36</td>
                <td>83%</td>
                <td>✅ Sangat Presisi</td>
            </tr>
            <tr>
                <td><b>3 Jam (T+3)</b></td>
                <td>0.59</td>
                <td>74%</td>
                <td>✅ Andal</td>
            </tr>
            <tr>
                <td><b>6 Jam (T+6)</b></td>
                <td>0.71</td>
                <td>72%</td>
                <td>👌 Cukup</td>
            </tr>
        </tbody>
    </table>
</section>

<section id="features">
    <h2>📱 Fitur Aplikasi</h2>
    <ul>
        <li><b>Hybrid Input:</b> Menerima input otomatis dari n8n atau input manual untuk simulasi.</li>
        <li><b>Smart Recommendation:</b> Menerjemahkan angka prediksi menjadi saran bahasa manusia. Contoh: <i>"☔ Sedia Payung/Jas Hujan: Akan turun hujan ringan. Lantai koridor mungkin licin."</i></li>
        <li><b>Mode Malam:</b> Dukungan tema gelap untuk kenyamanan visual.</li>
    </ul>
</section>

<section id="disclaimer">
    <h2>ℹ️ Disclaimer Akademis</h2>
    <div class="highlight-box">
        <p><b>Sumber Data Latih:</b> Model dilatih menggunakan data historis Stasiun Klimatologi Manado (Mapanget) sebagai <i>regional proxy</i>.</p>
        <p><b>Validitas Lokasi:</b> Meskipun dilatih dengan data regional, sistem dirancang untuk menerima input kondisi aktual <b>Lokal (Kampus Bahu)</b> saat <i>inference</i>, sehingga prediksi tetap relevan dengan mikroklimat kampus.</p>
    </div>
</section>

<div class="footer">
    <p>Dikembangkan oleh <b>Kelompok 1</b> | Teknik Informatika - Universitas Sam Ratulangi | 2025</p>
</div>

</body>
</html>
