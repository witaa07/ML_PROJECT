import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------------------------
# PAGE CONFIG
# -----------------------------------------
st.set_page_config(
    page_title="UNSRAT Weather Assistant",
    page_icon="🌤️",
    layout="centered"
)

# -----------------------------------------
# HEADER
# -----------------------------------------
st.title("UNSRAT Weather Assistant")
st.write("Prediksi cuaca sederhana untuk membantu mahasiswa UNSRAT membuat keputusan harian.")
st.caption("Data saat ini masih dummy. Integrasi Google Sheets akan ditambahkan setelah pipeline n8n aktif.")

st.divider()

# -----------------------------------------
# LAST UPDATE (Dummy)
# -----------------------------------------
st.subheader("Last Update")
current_time = datetime.now().strftime("%d %B %Y • %H:%M WITA")
st.info(f"Data diperbarui: **{current_time}**")

# -----------------------------------------
# RECOMMENDATION (Dummy)
# -----------------------------------------
st.subheader("Rekomendasi Cepat")
st.write("Berdasarkan kondisi cuaca saat ini (dummy):")

st.success("Kemungkinan hujan 40% → Disarankan membawa payung kecil.")

col1, col2, col3 = st.columns(3)
col1.metric("Suhu", "29°C")
col2.metric("Kelembapan", "76%")
col3.metric("Curah Hujan", "0.8 mm")

st.divider()

# -----------------------------------------
# HOURLY FORECAST (Dummy)
# -----------------------------------------
st.subheader("Perkiraan Cuaca Per Jam (Dummy)")

df = pd.DataFrame({
    "Jam": ["10:00", "11:00", "12:00", "13:00", "14:00", "15:00"],
    "Suhu (°C)": np.random.randint(26, 32, 6),
    "Curah Hujan (mm)": np.random.randint(0, 3, 6)
})

st.line_chart(df.set_index("Jam")["Suhu (°C)"])

st.divider()

# -----------------------------------------
# WEEKLY INSIGHT (Dummy)
# -----------------------------------------
st.subheader("Tren Suhu Mingguan (Dummy)")

dummy_week = pd.DataFrame({
    "Tanggal": pd.date_range(start="2024-01-01", periods=7),
    "Suhu": np.random.randint(27, 32, 7)
})

st.bar_chart(dummy_week.set_index("Tanggal")["Suhu"])

st.caption("Analisis akan diperbarui setelah dataset historis selesai ditemukan.")
