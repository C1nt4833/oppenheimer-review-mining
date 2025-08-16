# Oppenheimer review mining

Proyek ini menganalisis sentimen dari ulasan film *Oppenheimer* yang diambil dari IMDb, menggunakan teknik Natural Language Processing (NLP).

## 📌 Fitur Utama
- Scraping 100 review film dari IMDb
- Preprocessing teks (Case Folding, Tokenizing, Stopword Removal, Stemming)
- TF-IDF Vectorization
- Klasifikasi dengan Naive Bayes
- Visualisasi hasil (Word Cloud, Pie Chart, Confusion Matrix)

## 📂 Struktur Proyek
- *data/* → Dataset mentah & hasil preprocessing
- *outputs/* → Hasil visualisasi
- *scripts/* → Script Python modular
- *requirements.txt* → Daftar library yang dibutuhkan

## 🚀 Cara Menjalankan
1. Clone repository ini
   ```bash
   git clone https://github.com/C1nt4833/oppenheimer-review-mining.git
   cd oppenheimer-review-mining
2. Buat & aktifkan  Virtual Environment (Windows)
   '''bash
   python -m venv venv
   venv\Scripts\activate
3. Install dependencies
   '''bash
   pip install -r requiments.txt
4. Jalankan Analisis
   
