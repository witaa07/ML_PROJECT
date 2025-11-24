import pandas as pd

# ==========================================
# FITUR MODEL SUHU
# ==========================================
FEATURES_SUHU = [
    'Suhu',
    'Kelembapan',
    'jam_dalam_hari',
    'suhu_1jam_lalu',
    'suhu_24jam_lalu',
    'kelembapan_1jam_lalu'
]

# ==========================================
# FITUR MODEL HUJAN
# ==========================================
FEATURES_HUJAN = [
    'CurahHujan',
    'jam_dalam_hari',
    'Kelembapan',
    'suhu_2jam_lalu',
    'hari_dalam_minggu'
]

# ==========================================
# 1. TIMEZONE HANDLING
# ==========================================
def ensure_timezone(df, time_col='time'):
    df[time_col] = pd.to_datetime(df[time_col], errors='coerce')

    if df[time_col].dt.tz is None:
        df[time_col] = df[time_col].dt.tz_localize("UTC")

    df[time_col] = df[time_col].dt.tz_convert("Asia/Makassar")
    return df

# ==========================================
# 2. NORMALISASI NAMA KOLOM (SAMAKAN DENGAN TRAINING)
# ==========================================
def normalize_columns(df):

    if "temperature_2m (°C)" in df.columns:
        df["Suhu"] = df["temperature_2m (°C)"]

    if "relative_humidity_2m (%)" in df.columns:
        df["Kelembapan"] = df["relative_humidity_2m (%)"]

    if "rain (mm)" in df.columns:
        df["CurahHujan"] = df["rain (mm)"]

    return df

# ==========================================
# 3. KALENDAR FEATURES
# ==========================================
def add_calendar_features(df, time_col='time'):
    df["jam_dalam_hari"] = df[time_col].dt.hour
    df["hari_dalam_minggu"] = df[time_col].dt.dayofweek
    return df

# ==========================================
# 4. LAG FEATURES
# ==========================================
def add_lag_features(df):

    if "Suhu" in df.columns:
        df["suhu_1jam_lalu"] = df["Suhu"].shift(1)
        df["suhu_24jam_lalu"] = df["Suhu"].shift(24)
        df["suhu_2jam_lalu"] = df["Suhu"].shift(2)

    if "Kelembapan" in df.columns:
        df["kelembapan_1jam_lalu"] = df["Kelembapan"].shift(1)

    return df

# ==========================================
# 5. KONVERSI SEMUA FITUR NUMERIK KE FLOAT
# ==========================================
def convert_types(df):
    num_cols = [
        'Suhu', 'Kelembapan', 'CurahHujan',
        'suhu_1jam_lalu', 'suhu_24jam_lalu',
        'kelembapan_1jam_lalu', 'suhu_2jam_lalu'
    ]

    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    return df

# ==========================================
# 6. FILL NA
# ==========================================
def fill_missing(df):
    return df.ffill().bfill()

# ==========================================
# 7. MAIN FUNCTION
# ==========================================
def prepare_input(df):

    df = df.copy().reset_index(drop=True)

    df = ensure_timezone(df)
    df = normalize_columns(df)
    df = add_calendar_features(df)
    df = add_lag_features(df)

    # 🔥 PAKSA SEMUA KOLOM NUMERIK JADI FLOAT
    df = convert_types(df)

    df = fill_missing(df)

    last = df.iloc[[-1]].copy()

    all_features = list(set(FEATURES_SUHU + FEATURES_HUJAN))

    missing = [c for c in all_features if c not in last.columns]
    if missing:
        raise ValueError(f"Missing required features: {missing}")

    return last[all_features]
