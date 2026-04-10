Array adalah struktur data yang digunakan untuk menyimpan banyak data dalam satu variabel.

Dalam Python, array direpresentasikan menggunakan list.

Contoh:
nilai = [80, 70, 90, 60]

Karakteristik array:

Menyimpan banyak nilai dalam satu variabel
Diakses menggunakan index (dimulai dari 0)
Dapat dilakukan iterasi (looping)

Penggunaan array dalam program ini:

Menyimpan 10 nilai mahasiswa
Digunakan untuk mencari nilai tertinggi, terendah, dan rata-rata
Digunakan untuk menghitung jumlah mahasiswa lulus

<img width="620" height="921" alt="Screenshot 2026-04-10 122017" src="https://github.com/user-attachments/assets/446a0f79-5a70-4833-b498-ffddaf59c2ef" />


Analisis Kompleksitas

Misalkan jumlah data = n

1. Input data
for i in range(n):

Kompleksitas: O(n)
Karena membaca data satu per satu

2. Mencari nilai tertinggi
max(nilai)

Kompleksitas: O(n)
Karena harus membandingkan semua elemen

3. Mencari nilai terendah
min(nilai)

Kompleksitas: O(n)
Karena harus mengecek seluruh data

4. Menghitung rata-rata
sum(nilai) / len(nilai)

Kompleksitas: O(n)
Karena menjumlahkan semua elemen

5. Menghitung jumlah lulus
for n in nilai:

Kompleksitas: O(n)
Karena harus memeriksa setiap nilai

6. Akses elemen array
nilai[0]

Kompleksitas: O(1)
Karena langsung akses berdasarkan index

🧠 Kesimpulan Kompleksitas
Operasi dominan: O(n)
Akses langsung array: O(1)
Total kompleksitas program: O(n)



Refleksi Pembelajaran

Dari tugas ini saya belajar:

Memahami konsep dasar array dan penggunaannya
Mengolah data menggunakan looping
Menghitung nilai statistik sederhana (max, min, rata-rata)
Memahami dasar analisis kompleksitas algoritma
Menggunakan Python untuk visualisasi data sederhana
Mengelola project menggunakan Git dan GitHub

Saya juga belajar pentingnya:

Melakukan commit secara bertahap
