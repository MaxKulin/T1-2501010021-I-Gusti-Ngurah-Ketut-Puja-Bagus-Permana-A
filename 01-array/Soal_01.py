import matplotlib.pyplot as plt

# Array untuk menyimpan 10 nilai mahasiswa
nilai = []

# Input 10 nilai
for i in range(10):
    while True:
        try:
            n = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
            if 0 <= n <= 100:
                nilai.append(n)
                break
            else:
                print("Nilai harus di antara 0 sampai 100.")
        except ValueError:
            print("Input harus berupa angka.")

# Proses data
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)
rata_rata = sum(nilai) / len(nilai)
jumlah_lulus = 0

for n in nilai:
    if n >= 60:
        jumlah_lulus += 1

jumlah_tidak_lulus = len(nilai) - jumlah_lulus

# Output hasil
print("\n=== HASIL PENGELOLAAN NILAI ===")
print("Data nilai:", nilai)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Rata-rata:", rata_rata)
print("Jumlah mahasiswa lulus:", jumlah_lulus)
print("Jumlah mahasiswa tidak lulus:", jumlah_tidak_lulus)

# Grafik nilai tertinggi dan terendah
label_nilai = ["Tertinggi", "Terendah"]
data_nilai = [nilai_tertinggi, nilai_terendah]

plt.figure(figsize=(6, 4))
plt.bar(label_nilai, data_nilai)
plt.title("Grafik Nilai Tertinggi dan Terendah")
plt.ylabel("Nilai")
plt.ylim(0, 100)
plt.show()

# Grafik kelulusan
label_kelulusan = ["Lulus", "Tidak Lulus"]
data_kelulusan = [jumlah_lulus, jumlah_tidak_lulus]

plt.figure(figsize=(6, 4))
plt.bar(label_kelulusan, data_kelulusan)
plt.title("Grafik Kelulusan Mahasiswa")
plt.ylabel("Jumlah Mahasiswa")
plt.show()
