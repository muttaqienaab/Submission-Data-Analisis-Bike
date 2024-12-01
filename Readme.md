## Proses Implementasi
Instalasi Dependensi Pastikan Anda telah menginstal semua pustaka yang diperlukan dengan menjalankan perintah berikut di terminal:


## Salin kode

pip install -r requirements.txt

Mempersiapkan Dataset Dataset yang digunakan dalam proyek ini dapat diunduh dari file day.csv. Pastikan file CSV tersebut berada di direktori yang sama dengan file Python untuk menjalankan analisis dan dashboard.

Jalankan Notebook untuk Analisis

Buka file notebook.ipynb di Jupyter Notebook atau JupyterLab.
Ikuti langkah-langkah analisis untuk melakukan data wrangling, eksplorasi data (EDA), dan visualisasi.
Hasil analisis akan memberikan wawasan mengenai pola penggunaan sepeda dan faktor-faktor yang memengaruhi penggunaan sepeda.
Menjalankan Dashboard Streamlit Setelah melakukan analisis di notebook, Anda bisa menjalankan dashboard dengan perintah berikut di terminal:


## Salin kode
streamlit run dashboard.py

![Uploading image.png…]()






Interaksi di Dashboard Di dalam dashboard, pengguna dapat memilih filter berdasarkan kolom tertentu, seperti musim atau suhu, untuk menampilkan data yang relevan. Visualisasi berupa grafik distribusi, scatter plot, dan heatmap korelasi tersedia untuk analisis lebih lanjut.

Visualisasi yang Tersedia
Distribusi Jumlah Pengguna Sepeda Harian: Menggunakan histogram untuk menggambarkan distribusi pengguna sepeda harian sepanjang periode waktu.
Hubungan Suhu dan Jumlah Pengguna: Scatter plot yang menggambarkan hubungan antara suhu dan jumlah pengguna sepeda harian.
Boxplot Penggunaan Sepeda Berdasarkan Musim: Boxplot untuk menunjukkan bagaimana distribusi jumlah pengguna sepeda berbeda di setiap musim.
Korelasi antara Fitur Numerik: Heatmap untuk menunjukkan korelasi antara suhu, kelembapan, dan kecepatan angin dengan jumlah pengguna sepeda harian.
Kesimpulan
Proyek ini memberikan wawasan berharga tentang bagaimana faktor-faktor seperti suhu, kelembapan, dan musim dapat mempengaruhi penggunaan sepeda dalam sistem Bike Sharing. Melalui visualisasi yang interaktif, pengguna dapat lebih mudah memahami pola dan tren yang ada di data.

Saran Pengembangan Lebih Lanjut
Penerapan Algoritma Pembelajaran Mesin: Untuk memprediksi jumlah pengguna sepeda berdasarkan fitur-fitur tertentu, seperti suhu dan kelembapan.
Integrasi dengan Data Real-time: Menambahkan data real-time untuk menganalisis pola penggunaan sepeda secara langsung.
Visualisasi Lain: Menambahkan jenis visualisasi lainnya, seperti peta untuk menganalisis penggunaan sepeda berdasarkan lokasi.
