# Soal 6 : Hasil dari Sigma (6*k * (k - 1)) / (n ** 3)  dengan k=1 dan n=input user
# Cara 1 Langsung Jumlah

total_sum = 0  # untuk menyimpan total awal

# Input
n = int(input("Masukkan nilai n: ")) # untuk menyimpan input dari user di variabel

# Pengulangan
for k in range(1, n + 1):  # range harus sampai n, jadi gunakan n + 1
    total_sum += (6*k * (k - 1)) / (n ** 3)  # masukkan rumus

# Output
print("Hasil:", total_sum)  # hasil akhir semua penjumlahan

# Cara 2 Untuk melihat hasil secara bertahap

total_sum = 0 #untuk menyimpan total awal

# Input
n = int(input("Masukkan nilai n: "))# untuk menyimpan input dari user di variabel

# Perhitungan menggunakan metode perulangan
for k in range(1, n+1):   # range harus sampai n, jadi gunakan n + 1
    rumus = (6*k * (k - 1)) / (n ** 3) #masukan rumus notasi sigma
    total_sum += rumus #total awal akan ditambah dengan hasil rumus secara berkala
    print(f" untuk i = {k}, adalah = {rumus:.4f}, total= {total_sum:.4f}") #menampilkan hasil penjumlahan secara berkala

# Output
print("Total akhir:", total_sum) #hasil akhir total penjumlahan

#JANGAN LUPA HITUNG MANUAL DI BUKU TUGAS UNTUK PEMBUKTIAN
