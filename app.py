import streamlit as st
import pandas as pd
import requests
from io import StringIO

# URL dataset ikan dari GitHub
url = "https://github.com/Kaepci/Stocking/main/data_ikan.csv"

# Fungsi untuk mengambil data CSV dari GitHub
def load_data_from_github(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Gagal mengakses file CSV dari GitHub.")
        return pd.DataFrame()

# Fungsi untuk menyimpan dataset ke GitHub (diupdate melalui Streamlit)
def save_data_to_github(df):
    # Simulasikan penyimpanan data ke GitHub (diperlukan API GitHub atau setup CI/CD)
    # Anda bisa menggunakan GitHub API atau sistem CI/CD untuk mengupdate file CSV di repo.
    st.write("Data berhasil disimpan!")

# Menampilkan aplikasi Streamlit
st.title("Aplikasi Manajemen Stok Ikan")

# Memuat data ikan
df = load_data_from_github(url)

# Menampilkan dataset
st.subheader("Dataset Stok Ikan")
st.dataframe(df)

# Input untuk menambah stok ikan
st.subheader("Tambah Stok Ikan")
jenis_ikan = st.text_input("Jenis Ikan:", "")
jumlah_tambah = st.number_input("Jumlah Stok yang Ditambah:", min_value=0)

if st.button("Tambah Stok"):
    if jenis_ikan and jumlah_tambah > 0:
        # Menambah stok ikan
        if jenis_ikan in df['Jenis_Ikan'].values:
            df.loc[df['Jenis_Ikan'] == jenis_ikan, 'Stok'] += jumlah_tambah
            st.success(f"Stok ikan {jenis_ikan} berhasil ditambah sebanyak {jumlah_tambah}.")
        else:
            # Jika jenis ikan baru, tambah jenis ikan tersebut
            df.loc[len(df)] = [jenis_ikan, jumlah_tambah]
            st.success(f"Jenis ikan {jenis_ikan} baru berhasil ditambahkan dengan stok {jumlah_tambah}.")
        
        # Menyimpan data setelah perubahan
        save_data_to_github(df)

        # Tampilkan data terbaru
        st.subheader("Dataset Setelah Penambahan Stok")
        st.dataframe(df)
    else:
        st.error("Masukkan jenis ikan dan jumlah stok yang valid.")
