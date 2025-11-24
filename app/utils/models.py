import joblib
import numpy as np
import pandas as pd

# ==========================================
# FITUR MODEL SESUAI TRAINING NOTEBOOK
# ==========================================

FEATURES_SUHU = [
    'Suhu',
    'Kelembapan',
    'jam_dalam_hari',
    'suhu_1jam_lalu',
    'suhu_24jam_lalu',
    'kelembapan_1jam_lalu'
]

FEATURES_HUJAN = [
    'CurahHujan',
    'jam_dalam_hari',
    'Kelembapan',
    'suhu_2jam_lalu',
    'hari_dalam_minggu'
]

# ==========================================
# LOAD SEMUA MODEL
# ==========================================
def load_all_models(base_path="model"):
    models = {}

    # Suhu
    models["suhu_1h"] = joblib.load(f"{base_path}/suhu/suhu_1h.pkl")
    models["suhu_3h"] = joblib.load(f"{base_path}/suhu/suhu_3h.pkl")
    models["suhu_6h"] = joblib.load(f"{base_path}/suhu/suhu_6h.pkl")

    # Curah Hujan
    models["hujan_1h"] = joblib.load(f"{base_path}/curahHujan/hujan_1h.pkl")
    models["hujan_3h"] = joblib.load(f"{base_path}/curahHujan/hujan_3h.pkl")
    models["hujan_6h"] = joblib.load(f"{base_path}/curahHujan/hujan_6h.pkl")

    return models

# ==========================================
# PREDIKSI SUHU
# ==========================================
def predict_suhu(model, X_df):
    X = X_df[FEATURES_SUHU]
    pred = model.predict(X)[0]
    return float(pred)

# ==========================================
# PREDIKSI HUJAN
# ==========================================
def predict_hujan(model, X_df):
    X = X_df[FEATURES_HUJAN]

    probs = model.predict_proba(X)[0]
    label = int(np.argmax(probs))
    return {
        "label": label,
        "confidence": float(probs[label]),
        "probabilities": probs.tolist()
    }
