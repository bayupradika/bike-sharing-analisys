import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config for better visuals in Streamlit
st.set_page_config(page_title="Dashboard Analisis Penggunaan Sepeda", layout="wide")

# Memuat dataset
@st.cache_data
def load_data():
    # Replace this path with the correct one for your environment
    return pd.read_csv('./data/day.csv')

day = load_data()

# Judul aplikasi Streamlit
st.title('Dashboard Analisis Penggunaan Sepeda')

# Menampilkan data mentah
st.subheader('Data Mentah')
st.write(day.head())

# Scatter plot untuk suhu vs. penggunaan sepeda
st.subheader('Suhu vs. Penggunaan Sepeda')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=day, x='temp', y='cnt', ax=ax1)
ax1.set_title('Hubungan antara Suhu dan Penggunaan Sepeda', fontsize=16)
ax1.set_xlabel('Suhu (Dinormalisasi)', fontsize=12)
ax1.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
st.pyplot(fig1)

# Bar plot untuk penggunaan sepeda berdasarkan musim
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=day, x='season', y='cnt', palette='viridis', ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Musim', fontsize=16)
ax2.set_xlabel('Musim', fontsize=12)
ax2.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
ax2.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'], fontsize=10)
st.pyplot(fig2)

# Histogram untuk distribusi penggunaan sepeda
st.subheader('Distribusi Penggunaan Sepeda')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.histplot(day['cnt'], kde=True, ax=ax3)
ax3.set_title('Distribusi Penggunaan Sepeda', fontsize=16)
ax3.set_xlabel('Jumlah Penggunaan Sepeda', fontsize=12)
ax3.set_ylabel('Frekuensi', fontsize=12)
st.pyplot(fig3)

# Line plot untuk tren penggunaan sepeda berdasarkan hari
st.subheader('Tren Penggunaan Sepeda Berdasarkan Hari')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=day, x='dteday', y='cnt', ax=ax4)
ax4.set_title('Tren Penggunaan Sepeda dari Waktu ke Waktu', fontsize=16)
ax4.set_xlabel('Tanggal', fontsize=12)
ax4.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig4)

# Menambahkan informasi tambahan jika ada data lain yang ingin ditampilkan
st.subheader('Statistik Deskriptif Dataset')
st.write(day.describe())
