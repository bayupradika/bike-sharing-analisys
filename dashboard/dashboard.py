import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure the Streamlit app
st.set_page_config(page_title="Dashboard Analisis Penggunaan Sepeda", layout="wide")

# Load the dataset
@st.cache_data
def load_data():
    # Update the path to match the location of your CSV file
    return pd.read_csv('./data/day.csv')

day = load_data()

# Title of the Streamlit app
st.title('Dashboard Analisis Penggunaan Sepeda')

# Display basic dataset information
st.subheader('Informasi Dataset')
buffer = st.empty()
buffer.text(day.info())  # Streamlit doesn't support .info() directly; displaying as text

# Display raw data
st.subheader('Data Mentah')
st.write(day.head())

# Display missing values check
st.subheader('Cek Nilai Hilang')
missing_values = day.isnull().sum()
st.write(missing_values)

# Display descriptive statistics
st.subheader('Statistik Deskriptif')
st.write(day.describe())

# Scatter plot for temperature vs. bike usage
st.subheader('Suhu vs. Penggunaan Sepeda')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=day, x='temp', y='cnt', ax=ax1)
ax1.set_title('Hubungan antara Suhu dan Penggunaan Sepeda', fontsize=16)
ax1.set_xlabel('Suhu (Dinormalisasi)', fontsize=12)
ax1.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
st.pyplot(fig1)

# Bar plot for bike usage by season
st.subheader('Penggunaan Sepeda Berdasarkan Musim')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=day, x='season', y='cnt', palette='viridis', ax=ax2)
ax2.set_title('Penggunaan Sepeda Berdasarkan Musim', fontsize=16)
ax2.set_xlabel('Musim', fontsize=12)
ax2.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
ax2.set_xticklabels(['Musim Semi', 'Musim Panas', 'Musim Gugur', 'Musim Dingin'], fontsize=10)
st.pyplot(fig2)

# Histogram for the distribution of bike usage
st.subheader('Distribusi Penggunaan Sepeda')
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.histplot(day['cnt'], kde=True, ax=ax3)
ax3.set_title('Distribusi Penggunaan Sepeda', fontsize=16)
ax3.set_xlabel('Jumlah Penggunaan Sepeda', fontsize=12)
ax3.set_ylabel('Frekuensi', fontsize=12)
st.pyplot(fig3)

# Line plot for the trend of bike usage over time
st.subheader('Tren Penggunaan Sepeda Berdasarkan Hari')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=day, x='dteday', y='cnt', ax=ax4)
ax4.set_title('Tren Penggunaan Sepeda dari Waktu ke Waktu', fontsize=16)
ax4.set_xlabel('Tanggal', fontsize=12)
ax4.set_ylabel('Jumlah Penggunaan Sepeda', fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig4)

# Correlation heatmap for numerical features
st.subheader('Heatmap Korelasi Fitur Numerik')
fig5, ax5 = plt.subplots(figsize=(12, 8))
sns.heatmap(day.corr(), annot=True, cmap='coolwarm', ax=ax5)
ax5.set_title('Korelasi antara Fitur Numerik', fontsize=16)
st.pyplot(fig5)

# Pairplot for visualizing pairwise relationships
st.subheader('Visualisasi Pairwise Relationships')
fig6 = sns.pairplot(day, diag_kind='kde')
st.pyplot(fig6)

