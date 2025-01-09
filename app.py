import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Manajemen Keuangan (Pembukuan sederhana)
def laporan_keuangan():
    # Data transaksi (tanggal, deskripsi, pengeluaran, pemasukan)
    data_transaksi = {
        "Tanggal": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04"],
        "Deskripsi": ["Penjualan A", "Pembelian Bahan", "Penjualan B", "Pembelian C"],
        "Pemasukan": [100000, 0, 150000, 0],
        "Pengeluaran": [0, 50000, 0, 30000]
    }

    # Membuat DataFrame untuk transaksi
    df_transaksi = pd.DataFrame(data_transaksi)

    # Menghitung total pemasukan dan pengeluaran
    total_pemasukan = df_transaksi["Pemasukan"].sum()
    total_pengeluaran = df_transaksi["Pengeluaran"].sum()

    # Menghitung laba/rugi
    laba_rugi = total_pemasukan - total_pengeluaran

    # Menampilkan DataFrame dan laporan keuangan
    st.subheader("Laporan Keuangan:")
    st.write("Data Transaksi:", df_transaksi)
    st.write(f"Total Pemasukan: {total_pemasukan}")
    st.write(f"Total Pengeluaran: {total_pengeluaran}")
    st.write(f"Laba/Rugi: {laba_rugi}")

# 2. Pengelolaan Persediaan (Stok Barang)
def pengelolaan_persediaan():
    # Data persediaan (Nama barang, jumlah stok, stok minimum)
    data_stok = {
        "Barang": ["Barang A", "Barang B", "Barang C"],
        "Stok": [50, 10, 2],  # Stok saat ini
        "Stok Minimum": [10, 5, 5]  # Stok minimum yang harus dipertahankan
    }

    # Membuat DataFrame untuk persediaan
    df_stok = pd.DataFrame(data_stok)

    # Menambahkan kolom untuk status stok
    df_stok["Status"] = df_stok.apply(lambda row: "Habis" if row["Stok"] == 0 else ("Sedikit" if row["Stok"] <= row["Stok Minimum"] else "Cukup"), axis=1)

    # Menampilkan DataFrame stok dan status
    st.subheader("Data Persediaan:")
    st.write(df_stok)

# 3. Analisis Data Penjualan
def analisis_penjualan():
    # Data penjualan (Tanggal, Produk, Jumlah Terjual)
    data_penjualan = {
        "Tanggal": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04", "2025-01-05"],
        "Produk": ["Produk A", "Produk B", "Produk A", "Produk C", "Produk A"],
        "Jumlah Terjual": [10, 5, 8, 3, 12]
    }

    # Membuat DataFrame untuk penjualan
    df_penjualan = pd.DataFrame(data_penjualan)

    # Menghitung total penjualan per produk
    penjualan_per_produk = df_penjualan.groupby("Produk")["Jumlah Terjual"].sum()

    # Menampilkan hasil analisis penjualan
    st.subheader("Total Penjualan per Produk:")
    st.write(penjualan_per_produk)

    # Visualisasi hasil analisis penjualan
    st.subheader("Grafik Penjualan per Produk:")
    penjualan_per_produk.plot(kind='bar', color='skyblue')
    plt.title("Total Penjualan per Produk")
    plt.xlabel("Produk")
    plt.ylabel("Jumlah Terjual")
    st.pyplot()

# Menyusun Tampilan Streamlit
def main():
    st.title("Sistem UMKM: Manajemen Keuangan, Persediaan, dan Penjualan")

    # Menambahkan sidebar untuk navigasi
    menu = ["Laporan Keuangan", "Pengelolaan Persediaan", "Analisis Penjualan"]
    choice = st.sidebar.selectbox("Pilih Modul", menu)

    if choice == "Laporan Keuangan":
        laporan_keuangan()
    elif choice == "Pengelolaan Persediaan":
        pengelolaan_persediaan()
    elif choice == "Analisis Penjualan":
        analisis_penjualan()

if __name__ == "__main__":
    main()
