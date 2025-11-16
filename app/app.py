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
    rec = "Kemungkinan hujan tinggi (>70%) → Wajib membawa payung!"
    st.error(rec, icon="🌧️")
elif rain_prob >= 40:
    rec = "Kemungkinan hujan 40-70% → Disarankan membawa payung."
    st.warning(rec, icon="🌦️")
else:
    rec = "Kemungkinan hujan rendah (<40%) → Tidak perlu payung."
    st.success(rec, icon="🌞")

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
# DUMMY CHART
# ===============================
st.markdown("### Grafik Curah Hujan (Dummy)")

dummy_data = np.random.randint(0, 10, size=12)
dummy_df = pd.DataFrame({
    "Jam": [f"{i}:00" for i in range(12)],
    "Curah Hujan (mm)": dummy_data
})

st.line_chart(dummy_df, x="Jam", y="Curah Hujan (mm)")

# ===============================
# TOMBOL PALSU (BUTTON)
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
