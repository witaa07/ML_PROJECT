import streamlit as st
import pandas as pd
import datetime
import numpy as np
import os

# ============================
# IMPORT MODULES
# ============================
from utils.google_sheets import read_sheet, append_row
from utils.preprocessing import prepare_input
from utils.models import load_all_models, predict_suhu, predict_hujan

# ============================
# CLEAN TABLE — untuk Google Sheets
# ============================
def clean_sheet_dataframe(df):
    df = df.loc[:, ~df.columns.str.contains("^col_|Unnamed")]

    rename_map = {
        "temperature_2m (°C)": "Suhu (°C)",
        "relative_humidity_2m (%)": "Kelembapan (%)",
        "rain (mm)": "Curah Hujan (mm)",
    }
    df = df.rename(columns=rename_map)

    num_cols = ["Suhu (°C)", "Kelembapan (%)", "Curah Hujan (mm)"]
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    return df

# ============================
# CONFIG STREAMLIT
# ============================
st.set_page_config(
    page_title="UNSRAT Weather Assistant",
    page_icon="⛅",
    layout="wide"
)

# ============================
# GOOGLE SHEETS CONFIG
# ============================
JSON_PATH = "utils/beaming-ring-478707-m1-2dd3d047f00d.json"
SPREADSHEET_ID = "1kJB5wsiNZTPSk6rFJ4qQKQOy_ORUhGvkG2JUQtHDmUs"
SHEET_NAME = "Sheet1"

# ============================
# LOAD MODELS (Cached)
# ============================
@st.cache_resource
def load_models_cached():
    return load_all_models()

models = load_models_cached()

# ============================
# HEADER
# ============================
st.title("UNSRAT Weather Assistant ⛅")
st.write("Prediksi cuaca berdasarkan model Machine Learning UNSRAT.")
st.markdown("---")

# ============================
# INPUT FORM
# ============================
st.subheader("📥 Input Pengamatan Cuaca Saat Ini")

col1, col2 = st.columns(2)
with col1:
    suhu_now = st.number_input("Suhu Saat Ini (°C)", value=28.0)
    kelembapan_now = st.number_input("Kelembapan (%)", value=75.0)

with col2:
    curah_now = st.number_input("Curah Hujan (mm)", value=0.0)
    date_now = st.date_input("Tanggal Pengamatan", value=datetime.date.today())

time_now_only = st.time_input("Waktu Pengamatan", value=datetime.datetime.now().time())
time_now = datetime.datetime.combine(date_now, time_now_only)

# ============================
# DROPDOWN — PILIH JARAK PREDIKSI
# ============================
st.subheader("⏱️ Pilih Jarak Prediksi")
pred_option = st.selectbox(
    "Pilih periode waktu:",
    ["1 Jam", "3 Jam", "6 Jam"]
)

pred_map = {"1 Jam": 1, "3 Jam": 3, "6 Jam": 6}

# ============================
# PREDIKSI
# ============================
if st.button("🚀 Jalankan Prediksi Cuaca"):
    try:
        df_hist = read_sheet(JSON_PATH, SPREADSHEET_ID, SHEET_NAME)

        new_row = {
            "time": time_now.isoformat(),
            "temperature_2m (°C)": suhu_now,
            "relative_humidity_2m (%)": kelembapan_now,
            "rain (mm)": curah_now
        }
        df_hist = pd.concat([df_hist, pd.DataFrame([new_row])], ignore_index=True)

        X = prepare_input(df_hist)

        jam = pred_map[pred_option]

        # pilih model sesuai dropdown
        if jam == 1:
            suhu_pred = predict_suhu(models["suhu_1h"], X)
            hujan_pred = predict_hujan(models["hujan_1h"], X)
        elif jam == 3:
            suhu_pred = predict_suhu(models["suhu_3h"], X)
            hujan_pred = predict_hujan(models["hujan_3h"], X)
        else:
            suhu_pred = predict_suhu(models["suhu_6h"], X)
            hujan_pred = predict_hujan(models["hujan_6h"], X)

        # ============================
        # DISPLAY RESULT
        # ============================
        st.success("Prediksi berhasil dihitung ✔")

        st.markdown(f"### 🌡️ Prediksi Suhu — {pred_option}")
        st.metric(pred_option, f"{suhu_pred:.2f}°C")

        def label_to_text(l):
            return ["Cerah", "Hujan Ringan", "Hujan Lebat"][l]

        st.markdown(f"### 🌧️ Prediksi Curah Hujan — {pred_option}")
        st.metric(
            pred_option,
            label_to_text(hujan_pred["label"]),
            f"{hujan_pred['confidence']*100:.1f}%"
        )

        # ============================
        # REKOMENDASI PAYUNG
        # ============================
        st.markdown("### 🎒 Rekomendasi")
        if hujan_pred["label"] == 0:
            st.success("☀ Tidak perlu membawa payung")
        else:
            st.warning("☔ Disarankan membawa payung")

        # ============================
        # SAVE TO GOOGLE SHEETS
        # ============================
        save_row = [
            time_now.isoformat(),
            suhu_now, kelembapan_now, curah_now,
            suhu_pred,
            hujan_pred["label"], hujan_pred["confidence"],
        ]

        append_row(JSON_PATH, SPREADSHEET_ID, SHEET_NAME, save_row)
        st.info("📡 Input + hasil prediksi telah disimpan ke Google Sheets.")

    except Exception as e:
        st.error(f"Terjadi kesalahan selama prediksi: {e}")

# ============================
# DISPLAY DATA SHEETS
# ============================
st.markdown("---")
st.subheader("📊 Data Realtime dari Google Sheets")

try:
    df_live = read_sheet(JSON_PATH, SPREADSHEET_ID, SHEET_NAME)
    df_live = clean_sheet_dataframe(df_live)

    st.dataframe(
        df_live.style.format({
            "Suhu (°C)": "{:.2f}",
            "Kelembapan (%)": "{:.0f}",
            "Curah Hujan (mm)": "{:.2f}"
        })
    )

except Exception as e:
    st.error(f"Gagal membaca data realtime Google Sheets: {e}")
