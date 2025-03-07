import numpy as np
import pandas as pd

# Dara Bersih
housePredict = pd.read_csv('data/data_house.csv')

# Cek Nilai Kosong
print(housePredict.isnull().sum())

# Hapus Baris dengan Nilai Kosonnh
housePredict = housePredict.dropna()

# Cek Data Apakah ada nilai NaN
print(housePredict.isna().sum())

# Cek Apakah Ada Data yang Bukan Angka di Kolom Numerik
for col in housePredict.select_dtypes(include=['int64', 'float64']).columns:
    print(f"\n--Kolom: {col}---")
    print(housePredict[col].unique()[:10])

# Cek tipe data kolom
print(housePredict.dtypes)

# Cek Duplikasi Data
print(f"Jumlah data duplikat: {housePredict.duplicated().sum()}")  
