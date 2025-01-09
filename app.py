import streamlit as st
import pandas as pd

# Dataset contoh
data = {
    'Tanggal': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04'],
    'Kode Ikan': ['A001', 'A002', 'A001', 'A003'],
    'Nama Ikan': ['Ikan Nila', 'Ikan Lele', 'Ikan Nila', 'Ikan Mas'],
    'Stok Awal': [100, 200, 120, 150],
    'Pembelian': [50, 0, 30, 100],
    'Penjualan': [30, 50, 40, 30],
    'Harga Per Kg': [20, 25, 20, 30]  # Menambahkan harga per kg untuk menghitung total penjualan
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Menghitung Stok Akhir dan Total Penjualan
df['Stok Akhir'] = df['Stok Awal'] + df['Pembelian'] - df['Penjualan']
df['Total Penjualan'] = df['Penjualan'] * df['Harga Per Kg']

# Fungsi untuk menambah produk
def tambah_produk(tanggal, kode_ikan, pembelian):
    # Menambahkan produk ke stok
    stok_awal = df[df['Kode Ikan'] == kode_ikan]['Stok Akhir'].iloc[-1]  # Mengambil stok akhir dari ikan sebelumnya
    stok_akhir = stok_awal + pembelian
    
    # Menambahkan transaksi pembelian baru
    df_baru = pd.DataFrame({
        'Tanggal': [tanggal],
        'Kode Ikan': [kode_ikan],
        'Nama Ikan': [df[df['Kode Ikan'] == kode_ikan]['Nama Ikan'].iloc[0]],  # Nama ikan berdasarkan kode ikan
        'Stok Awal': [stok_awal],
        'Pembelian': [pembelian],
        'Penjualan': [0],  # Tidak ada penjualan untuk transaksi pembelian
        'Stok Akhir': [stok_akhir],
        'Harga Per Kg': [df[df['Kode Ikan'] == kode_ikan]['Harga Per Kg'].iloc[0]]  # Mengambil harga dari kode ikan
    })
    
    global df  # Mengupdate df global dengan data baru
    df = pd.concat([df, df_baru], ignore_index=True)

# Fungsi untuk mengurangi stok (penjualan)
def jual_produk(tanggal, kode_ikan, penjualan):
    # Mengurangi stok berdasarkan penjualan
    stok_awal = df[df['Kode Ikan'] == kode_ikan]['Stok Akhir'].iloc[-1]  # Mengambil stok akhir dari ikan sebelumnya
    if stok_awal >= penjualan:
        stok_akhir = stok_awal - penjualan
        
        # Menambahkan transaksi penjualan baru
        df_baru = pd.DataFrame({
            'Tanggal': [tanggal],
            'Kode Ikan': [kode_ikan],
            'Nama Ikan': [df[df['Kode Ikan'] == kode_ikan]['Nama Ikan'].iloc[0]],  # Nama ikan berdasarkan kode ikan
            'Stok Awal': [stok_awal],
            'Pembelian': [0],  # Tidak ada pembelian untuk transaksi penjualan
            'Penjualan': [penjualan],
            'Stok Akhir': [stok_akhir],
            'Harga Per Kg': [df[df['Kode Ikan'] == kode_ikan]['Harga Per Kg'].iloc[0]]  # Mengambil harga dari kode ikan
        })
        
        # Mengupdate df global dengan data baru
        global df
        df = pd.concat([df, df_baru], ignore_index=True)
    else:
        st.warning(f"Stok {df[df['Kode Ikan'] == kode_ikan]['Nama Ikan'].iloc[0]} tidak cukup untuk penjualan.")

# Fungsi untuk menghitung total penjualan
def hitung_total_penjualan():
    total_penjualan = df['Total Penjualan'].sum()  # Menjumlahkan seluruh total penjualan
    return total_penjualan

# Streamlit UI
st.title("Pembukuan Stok Ikan UMKM")

# Menampilkan DataFrame
st.subheader("Pembukuan Stok Ikan UMKM:")
st.dataframe(df)

# Input untuk menambah produk
st.subheader("Tambah Produk (Pembelian)")
tanggal_pembelian = st.date_input("Tanggal Pembelian", value=pd.to_datetime("2025-01-05"))
kode_ikan_pembelian = st.selectbox("Pilih Kode Ikan", df['Kode Ikan'].unique())
pembelian = st.number_input("Jumlah Pembelian (kg)", min_value=1)

if st.button("Tambah Produk"):
    tambah_produk(tanggal_pembelian.strftime('%Y-%m-%d'), kode_ikan_pembelian, pembelian)
    st.success("Produk berhasil ditambahkan!")

# Input untuk mengurangi stok (penjualan)
st.subheader("Penjualan")
tanggal_penjualan = st.date_input("Tanggal Penjualan", value=pd.to_datetime("2025-01-06"))
kode_ikan_penjualan = st.selectbox("Pilih Kode Ikan untuk Penjualan", df['Kode Ikan'].unique())
penjualan = st.number_input("Jumlah Penjualan (kg)", min_value=1)

if st.button("Proses Penjualan"):
    jual_produk(tanggal_penjualan.strftime('%Y-%m-%d'), kode_ikan_penjualan, penjualan)
    st.success("Penjualan berhasil diproses!")

# Menghitung dan menampilkan total penjualan
total_penjualan = hitung_total_penjualan()
st.subheader(f"Total Pendapatan dari Penjualan: Rp {total_penjualan}")

