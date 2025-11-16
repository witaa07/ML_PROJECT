import streamlit as st
import pandas as pd
import numpy as np
import datetime

# ===============================
# CONFIG
# ===============================
st.set_page_config(
    page_title="UNSRAT Weather Assistant",
    page_icon="⛅",
    layout="wide"
)

# ===============================
# HEADER
# ===============================
st.title("UNSRAT Weather Assistant ⛅")
st.write(
    "Prediksi cuaca sederhana untuk membantu mahasiswa UNSRAT membuat keputusan harian.\n"
    "Data saat ini masih dummy. Integrasi Google Sheets akan ditambahkan setelah pipeline n8n aktif."
)

st.markdown("---")

# ===============================
# LAST UPDATE (DUMMY)
# ===============================
st.subheader("Last Update")

last_update = datetime.datetime.now().strftime("%d %B %Y • %H:%M WITA")
st.info(f"**Data diperbarui:** {last_update}", icon="📅")

# ===============================
# REKOMENDASI CEPAT (DUMMY)
# ===============================
st.subheader("Rekomendasi Cepat")

rain_prob = 40  # dummy
if rain_prob >= 70:
    st.error("Kemungkinan hujan tinggi (>70%) → Wajib membawa payung!", icon="🌧️")
elif rain_prob >= 40:
    st.warning("Kemungkinan hujan 40-70% → Disarankan membawa payung.", icon="🌦️")
else:
    st.success("Kemungkinan hujan rendah (<40%) → Tidak perlu payung.", icon="🌞")

# ===============================
# MODE PILIHAN (HARIAN / PER JAM)
# ===============================
st.subheader("Mode Prediksi (Placeholder)")
mode = st.radio("Pilih Mode Prediksi:", ["Per Jam (Dummy)", "Harian (Dummy)"])
st.caption("⌛ Fitur ini akan aktif setelah model ML selesai dilatih.")

# ===============================
# FORECAST (DUMMY)
# ===============================
st.markdown("### Perkiraan Cuaca")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("1 Jam ke Depan", "Hujan Ringan", "40%")
with col2:
    st.metric("3 Jam ke Depan", "Berawan", "-10%")
with col3:
    st.metric("6 Jam ke Depan", "Berawan Tebal", "+20%")

# ===============================
# CONFIDENCE MODEL (PLACEHOLDER)
# ===============================
st.subheader("Confidence Model (Placeholder)")
st.info("Model ML belum tersedia. Nilai confidence berikut hanya dummy.", icon="🤖")

st.metric("Confidence", "--%")
st.caption("Setelah model selesai, confidence menunjukkan seberapa yakin model terhadap prediksi.")

# ===============================
# INSIGHT MODEL (PLACEHOLDER)
# ===============================
st.subheader("Insight Prediksi (Placeholder)")
st.warning(
    "Penjelasan ini masih dummy. Nanti akan masuk analisis: suhu naik, kelembapan tinggi, angin kencang, dll.",
    icon="📊"
)
st.write(
    """
    **Contoh Dummy Insight:**  
    • Kelembapan di Manado sedang meningkat.  
    • Tekanan udara menurun perlahan.  
    • Faktor-faktor ini meningkatkan peluang hujan ringan dalam 1–2 jam ke depan.
    """
)

# ===============================
# GRAFIK CURAH HUJAN (DUMMY)
# ===============================
st.markdown("### Grafik Curah Hujan (Dummy)")

dummy_data = np.random.randint(0, 10, size=12)
dummy_df = pd.DataFrame({
    "Jam": [f"{i}:00" for i in range(12)],
    "Curah Hujan (mm)": dummy_data
})
st.line_chart(dummy_df, x="Jam", y="Curah Hujan (mm)")

# ===============================
# GOOGLE SHEETS REALTIME TABLE (PLACEHOLDER)
# ===============================
st.subheader("Data Cuaca Realtime (Placeholder)")
st.info("Tabel ini masih dummy. Akan otomatis terisi dari Google Sheets setelah n8n aktif.", icon="📡")

dummy_realtime = pd.DataFrame({
    "Waktu": ["--", "--", "--"],
    "Suhu (°C)": ["--", "--", "--"],
    "Kelembapan (%)": ["--", "--", "--"],
    "Curah Hujan": ["--", "--", "--"]
})
st.dataframe(dummy_realtime)

# ===============================
# EDA DATASET HISTORIS (PLACEHOLDER)
# ===============================
st.subheader("EDA Dataset Historis (Placeholder)")
st.warning("Grafik-grafik berikut masih dummy. Dataset asli akan diberikan oleh Person 2.", icon="📁")

dummy_hist = pd.DataFrame({
    "Tanggal": pd.date_range("2025-01-01", periods=7),
    "Curah Hujan": np.random.uniform(0, 20, 7)
})
st.line_chart(dummy_hist.set_index("Tanggal"))

# ===============================
# LOKASI UNSRAT (MAP)
# ===============================
st.subheader("Lokasi Kampus UNSRAT (Placeholder)")
st.caption("Peta ini masih placeholder, akan diganti peta cuaca sungguhan.")

unsrat_map = pd.DataFrame({
    "lat": [1.4555],
    "lon": [124.8248]
})
st.map(unsrat_map)

# ===============================
# TOMBOL PALSU
# ===============================
st.markdown("### Aksi Lainnya")

btn1, btn2 = st.columns(2)
with btn1:
    st.button("Refresh (Dummy)")
with btn2:
    st.button("Lihat Data Mentah (Dummy)")

# ===============================
# CATATAN
# ===============================
st.caption("📌 Semua data di atas masih dummy. Data asli akan otomatis ditarik dari Google Sheets via n8n ketika pipeline sudah aktif.")
