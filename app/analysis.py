import pandas as pd 
import numpy as np

def analyze_price_trends(df):
    """
    Menganalisis tren harga properti berdasarkan tahun
    """
    # Ubah 'date' ke datetime
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Tambahkan kolom 'year'
    df["year"] = df["date"].dt.year
    
    # Hitung rata-rata harga per tahun
    avg_price_per_year = df.groupby("year")["price"].mean()

    return avg_price_per_year

def analyze_city_price(df):
    """
    Menganalisis harga rata-rata per kota
    """
    avg_price_per_city = df.groupby("city")["price"].mean().sort_values(ascending=False)

    return avg_price_per_city
