# Tugas Kecil Strategi Algoritma 2
Implementasi Convex Hull untuk Visualisasi Tes Linear Separability Dataset 
dengan Algoritma  _Divide and Conquer_


## Deskripsi Singkat Program yang Dibuat
Salah satu hal penting dalam komputasi
geometri adalah menentukan convex hull dari kumpulan titik. Himpunan titik
pada bidang planar disebut convex jika untuk sembarang dua titik pada bidang
tersebut (misal p dan q), seluruh segmen garis yang berakhir di p dan q berada
pada himpunan tersebut.

Ide
pengerjaannya dijabarkan di dalam poin-poin berikut ini.
1. Mengurutkan titik berdasarkan absis, jika ditemukan titik yang dengan
absis yang sama, diurutkan berdasarkan ordinatnya.
Pengurutan titik ini menggunakan algoritma quick_sort. Titik yang
diurutkan adalah titik koordinat yang terdapat di dalam datasets
2. Pilih titik yang memiliki urutan pertama dan terakhir, bentuk suatu garis
yang membagi area menjadi dua bagian (atas dan bawah)
3. Cari titik terjauh di area atas dan cari titik terjauh di area bawah,
hubungkan kedua titik tersebut dengan titik-titik yang sudah ada di dalam
himpunan penyelesaian convex hull
Pencarian titik terjauh dilakukan dengan menggunakan fungsi
jarak_titik_ke_garis
4. Lakukan secara rekursif hingga mencapai basis (tidak ada titik di atas garis
maupun di bawah garis)
5. Diperoleh himpunan penyelesaian berupa kumpulan titik, urutkan kembali
berdasarkan absisnya, kemudian cari indeksnya menggunakan fungsi
titik_menjadi_indeks
6. Tambahkan setiap pasangan indeks titik tersebut ke dalam list hasil
7. Convex hull siap untuk divisualisasikan pada file notebook

## Requirement Program dan Instalasi Module/Package yang Diperlukan
### Requirement Program
1. Python
2. Pandas
3. Matplotlib
4. Sklearn
5. Numpy
