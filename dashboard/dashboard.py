import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dday = pd.read_csv('data/day.csv')

# Title of the dashboard
st.title('Dashboard Analisis Penjualan Sepeda')

# Visualisasi Pertanyaan 1: Hubungan Suhu dan Jumlah Sepeda
st.subheader('Hubungan Suhu dan Jumlah Sepeda')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=dday, x='temp', y='cnt', ax=ax1)
plt.title('Hubungan Suhu Terhadap Penggunaan Sepeda')
plt.xlabel('Suhu')
plt.ylabel('Jumlah Sepeda')
st.pyplot(fig1) 

# Visualisasi Pertanyaan 2: Penggunaan Sepeda Berdasarkan Musim
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=dday, x='season', y='cnt', ax=ax2)
plt.title('Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda')
st.pyplot(fig2) 
