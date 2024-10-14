import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
dday = pd.read_csv('./data/day.csv')

# Tampilkan beberapa baris awal
st.title("Bike Usage Analysis")
if st.checkbox("Show raw data"):
    st.write(dday.head())

# Menampilkan informasi dasar tentang dataset
if st.checkbox("Show dataset info"):
    buffer = io.StringIO()
    dday.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

# Menampilkan statistik deskriptif untuk variabel numerik
st.subheader("Descriptive Statistics")
st.write(dday.describe())

# Mengecek apakah ada nilai yang hilang
st.subheader("Missing Values")
st.write(dday.isnull().sum())

# Mengecek data duplikat
st.subheader("Duplicate Rows")
st.write(dday.duplicated().sum())

# Boxplot untuk memeriksa outliers
st.subheader("Boxplots for Numerical Columns")
numerical_columns = ['temp', 'atemp', 'hum', 'windspeed', 'cnt']
for col in numerical_columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=dday[col])
    plt.title(f'Boxplot of {col}')
    st.pyplot(plt)

# Mengonversi kolom dteday ke format datetime
dday['dteday'] = pd.to_datetime(dday['dteday'])

# Distribusi variabel numerik dengan histogram
st.subheader("Distribution of Numerical Columns")
for col in numerical_columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(dday[col], kde=True)
    plt.title(f'Distribution of {col}')
    st.pyplot(plt)

# Korelasi antar variabel dengan heatmap
st.subheader("Correlation Heatmap")
plt.figure(figsize=(10, 6))
sns.heatmap(dday.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
st.pyplot(plt)

# Scatter plot antara suhu dan penggunaan sepeda
st.subheader("Scatterplot: Temperature vs Bike Usage")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=dday['temp'], y=dday['cnt'])
plt.title('Scatterplot between Temperature and Bike Usage')
st.pyplot(plt)

# Boxplot jumlah penggunaan sepeda berdasarkan musim
season_mapping = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
dday['season_name'] = dday['season'].map(season_mapping)

st.subheader("Bike Usage by Season")
plt.figure(figsize=(8, 5))
sns.boxplot(x='season_name', y='cnt', data=dday)
plt.title('Bike Usage by Season')
st.pyplot(plt)

# Rata-rata penggunaan sepeda berdasarkan musim
average_usage_by_season = dday.groupby('season_name')['cnt'].mean().reset_index()
plt.figure(figsize=(8, 5))
sns.barplot(x='season_name', y='cnt', data=average_usage_by_season)
plt.title('Average Bike Usage by Season')
st.pyplot(plt)

# Scatter plot untuk kelembapan dan penggunaan sepeda
st.subheader("Scatterplot: Humidity vs Bike Usage")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=dday['hum'], y=dday['cnt'])
plt.title('Scatterplot between Humidity and Bike Usage')
st.pyplot(plt)

# Scatter plot untuk kecepatan angin dan penggunaan sepeda
st.subheader("Scatterplot: Windspeed vs Bike Usage")
plt.figure(figsize=(8, 5))
sns.scatterplot(x=dday['windspeed'], y=dday['cnt'])
plt.title('Scatterplot between Windspeed and Bike Usage')
st.pyplot(plt)

# Menghitung korelasi kelembapan dan kecepatan angin terhadap penggunaan sepeda
correlation_hum_cnt = dday['hum'].corr(dday['cnt'])
correlation_wind_cnt = dday['windspeed'].corr(dday['cnt'])
st.write(f'Correlation between humidity and bike usage: {correlation_hum_cnt:.2f}')
st.write(f'Correlation between windspeed and bike usage: {correlation_wind_cnt:.2f}')
