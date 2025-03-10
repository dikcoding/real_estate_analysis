import matplotlib.pyplot as plt

def plot_price_trends(avg_price_per_year, output_path="output/price_trends.png"):
    """
    Membuat grafik tren harga properti dari tahun ke tahun
    """
    if avg_price_per_year.empty:
        print("Data tren harga properti kosong. Tidak bisa membuat grafik.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(avg_price_per_year.index, avg_price_per_year.values, marker="o", linestyle="-", color="b", linewidth=2, markersize=6, label="Harga Rata-rata")
    
    # Tambahkan label pada setiap titik
    for x, y in zip(avg_price_per_year.index, avg_price_per_year.values):
        plt.text(x, y, f"{y:,.0f}", ha="right", fontsize=9)

    plt.xlabel("Tahun")
    plt.ylabel("Harga Rata-rata (USD)")
    plt.title("Tren Harga Properti per Tahun")
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(output_path)
    plt.show()

def plot_city_prices(avg_price_per_city, output="output/city_prices.png"):
    """
    Membuat grafik harga rata-rata per kota dengan label harga di atas batang.
    """
    plt.figure(figsize=(12, 6))
    ax = avg_price_per_city.head(10).plot(kind="bar", color="skyblue")

    plt.xlabel("Kota")
    plt.ylabel("Harga Rata-rata (USD)")
    plt.title("Harga Rata-rata Properti di 10 Kota Teratas")
    plt.xticks(rotation=45)

    # Menambahkan label harga di atas batang
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', 
                    (p.get_x() + p.get_width() / 2, p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='black')

    plt.savefig(output)
    plt.show()

