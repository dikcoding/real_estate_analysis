import pandas as pd

def load_data(file_path):
    """
    Memuat data properti dari file CSV dan membersihkan kolom yang tidak relevan
    """

    try:python -m pip install --upgrade pip

        df = pd.read_csv(file_path)

        # Memilih kolom yang relevan
        column_to_keep = ["date", "price", "bedrooms", "bathrooms", "sqft_living", 
                           "yr_renovated", "city", "statezip"]
        df = df[column_to_keep]

        # Konversi kolom 'date' ke format datatime
        df["date"] = pd.to_datetime(df["date"], errors='coerce')

        # hapus baris dengan data kosong (NaN)
        df.dropna(inplace=True)

        return df
    except Exception as e:
        print(f"Tejadi kesalahan dalam memuat data: {e}")
        return None