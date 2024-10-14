import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat dataset
day = pd.read_csv('./data/day.csv')

# Judul aplikasi Streamlit
st.title('Dashboard Analisis Penggunaan Sepeda')

# Menampilkan data mentah
st.subheader('Data Mentah')
st.write(day.head())

# Scatter plot untuk suhu vs. penggunaan sepeda
st.subheader('Suhu vs. Penggunaan Sepeda')
fig1, ax1 = plt.subplots()
sns.scatterplot(data=day, x='temp', y='cnt', ax=ax1)
ax1.set_title('Hubungan antara Suhu dan Penggunaan Sepeda')
ax1.set_xlabel('Suhu (Dinormalisasi)')
ax1.set_ylabel('Jumlah Penggunaan Sepeda')
st.pyplot(fig1)

# Bar plot untuk penggunaan sepeda berdasarkan musim
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig2, ax2 = plt.subplots()
sns.barplot(data=day, x='season', y='cnt', palette='viridis', ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Musim')
ax2.set_xlabel('Musim')
ax2.set_ylabel('Jumlah Penggunaan Sepeda')
ax2.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'])
st.pyplot(fig2)