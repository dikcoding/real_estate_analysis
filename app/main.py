import os
import sys

# akses modul path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.data_loader import load_data
from app.analysis import analyze_price_trends, analyze_city_price
from app.visualization import plot_price_trends, plot_city_prices

os.makedirs("output", exist_ok=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = os.path.join(BASE_DIR, "data", "data_house.csv")

print("Menggunakan file:", data_file)

# Load data dari CSV
df = load_data(data_file)

if df is not None:
    # Analisis tren harga properti
    avg_price_per_year = analyze_price_trends(df)
    avg_price_per_city = analyze_city_price(df)

    # Buat visualisasi
    plot_price_trends(avg_price_per_year)
    plot_city_prices(avg_price_per_city)
