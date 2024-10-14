# Bike Sharing Analysis Dashboard ✨

Proyek ini adalah dashboard analisis data sharing sepeda berdasarkan dataset *Bike-sharing-dataset*. Proses analisis mencakup eksplorasi data, visualisasi, dan pembuatan dashboard interaktif menggunakan **Streamlit**.

## Setup Environment - Anaconda
Jika Anda menggunakan **Anaconda**, ikuti langkah-langkah berikut untuk menyiapkan lingkungan:

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
Setup Environment - Shell/Terminal
Jika Anda menggunakan Shell/Terminal, ikuti langkah-langkah berikut:

bash
Copy code
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
Menjalankan Aplikasi Streamlit
Setelah menyiapkan lingkungan, jalankan dashboard menggunakan perintah berikut:

streamlit run submission/dashboard/dashboard.py
Struktur Direktori

submission
├───dashboard
│   ├───dashboard.py        # File dashboard menggunakan Streamlit
│   └───all_data.csv        # Dataset hasil gabungan (jika diperlukan)
├───data
│   ├───hour.csv            # Dataset jam-jam
│   └───day.csv             # Dataset harian
├───notebook.ipynb          # Proses analisis lengkap dalam bentuk Jupyter Notebook
├───README.md               # Dokumentasi proyek
├───requirements.txt        # Daftar dependencies
└───url.txt                 # Tautan penting terkait proyek
Dependencies
Pastikan Anda telah menginstall semua dependencies yang diperlukan melalui requirements.txt. Ini berisi semua pustaka yang dibutuhkan untuk menjalankan analisis dan dashboard.

Pertanyaan Bisnis
Analisis dalam proyek ini menjawab dua pertanyaan bisnis utama:

Bagaimana suhu mempengaruhi penggunaan sepeda?
Bagaimana penggunaan sepeda bervariasi menurut musim?
Terima kasih telah melihat proyek ini! Jangan ragu untuk menjalankan analisis atau melakukan modifikasi pada dashboard sesuai kebutuhan.
