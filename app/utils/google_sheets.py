import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

# Scope wajib untuk Google Sheets + Google Drive
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_client(json_path):
    """
    Membuat client gspread menggunakan service account JSON.
    """
    creds = Credentials.from_service_account_file(json_path, scopes=SCOPES)
    client = gspread.authorize(creds)
    return client


def read_sheet(json_path, spreadsheet_id, sheet_name):
    """
    Membaca Google Sheet dan mengembalikannya sebagai DataFrame.
    Menghindari error DUPLICATE HEADER dengan memastikan header tunggal.
    """
    client = get_client(json_path)
    sh = client.open_by_key(spreadsheet_id)
    ws = sh.worksheet(sheet_name)

    # baca semua data mentah
    rows = ws.get_all_values()

    if not rows:
        return pd.DataFrame()

    header = rows[0]
    data = rows[1:]

    # buang kolom header kosong seperti ""
    header = [h if h != "" else f"col_{i}" for i, h in enumerate(header)]

    df = pd.DataFrame(data, columns=header)

    return df


def append_row(json_path, spreadsheet_id, sheet_name, row_values):
    """
    Menambahkan baris baru ke Google Sheet.
    Aman untuk jumlah kolom yang panjang.
    Tidak akan merusak header.
    """
    client = get_client(json_path)
    sh = client.open_by_key(spreadsheet_id)
    ws = sh.worksheet(sheet_name)

    ws.append_row(
        row_values,
        value_input_option="RAW",
        insert_data_option="INSERT_ROWS"  # aman untuk banyak kolom
    )
