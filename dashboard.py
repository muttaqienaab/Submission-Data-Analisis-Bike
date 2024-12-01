import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca data
try:
    day_df = pd.read_csv('day.csv')
    st.success("Data berhasil di-load!")
    st.write(day_df.head())
except FileNotFoundError:
    st.error("File 'day.csv' tidak ditemukan. Pastikan file ada di direktori yang benar.")
    st.stop()

# Judul Dashboard
st.title("🚴 Dashboard Analisis Bike Sharing")
st.markdown("Visualisasi interaktif data penggunaan sepeda berdasarkan kondisi cuaca, suhu, dan waktu.")

# Sidebar untuk filter interaktif
st.sidebar.header("🔧 Filter Data")
selected_season = st.sidebar.selectbox("Pilih Musim:", ["Semua"] + list(day_df['season'].unique()))
selected_year = st.sidebar.radio("Pilih Tahun:", ["Semua"] + sorted(day_df['yr'].unique()))

# Filter data
filtered_data = day_df.copy()
if selected_season != "Semua":
    filtered_data = filtered_data[filtered_data['season'] == selected_season]
if selected_year != "Semua":
    filtered_data = filtered_data[filtered_data['yr'] == selected_year]

# Distribusi jumlah pengguna sepeda
st.subheader("📊 Distribusi Jumlah Pengguna Sepeda Harian")
fig, ax = plt.subplots()
sns.histplot(filtered_data['cnt'], kde=True, ax=ax, color='blue')
ax.set_title("Distribusi Jumlah Pengguna Sepeda Harian", fontsize=14)
ax.set_xlabel("Jumlah Pengguna", fontsize=12)
ax.set_ylabel("Frekuensi", fontsize=12)
st.pyplot(fig)

# Hubungan suhu vs jumlah pengguna sepeda
st.subheader("🌡️ Hubungan Suhu dan Jumlah Pengguna Sepeda")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_data, x='temp', y='cnt', ax=ax, color='green', alpha=0.6)
ax.set_title("Hubungan Suhu dan Jumlah Pengguna Sepeda", fontsize=14)
ax.set_xlabel("Suhu", fontsize=12)
ax.set_ylabel("Jumlah Pengguna", fontsize=12)
st.pyplot(fig)

# Heatmap korelasi
st.subheader("📈 Visualisasi Korelasi Antar Variabel")
numeric_data = filtered_data.select_dtypes(include=['float64', 'int64'])
if numeric_data.shape[1] > 1:
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Heatmap Korelasi Antar Variabel", fontsize=14)
    st.pyplot(fig)
else:
    st.info("Tidak ada cukup data numerik untuk menampilkan heatmap korelasi.")

# Statistik Deskriptif
st.subheader("📋 Statistik Deskriptif")
st.write(filtered_data.describe())

# Sidebar informasi tambahan
st.sidebar.markdown("---")
st.sidebar.info("""
**Tips Dashboard**  
- Gunakan filter untuk melihat data spesifik.  
- Visualisasi interaktif akan berubah berdasarkan filter.  
- Selamat menganalisis!
""")
