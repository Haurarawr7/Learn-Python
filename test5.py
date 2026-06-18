# Soal 5 : Hasil dari Sigma (3*i + 2)/(n**2) dengan i=1 dan n=input user
# Cara 1 Langsung Jumlah

total_sum = 0  # untuk menyimpan total awal

# Input
n = int(input("Masukkan nilai n: "))# untuk menyimpan input dari user di variabel

# Pengulangan
for i in range(1, n + 1):  # range harus sampai n, jadi gunakan n + 1
    total_sum += (3 * i + 2) / (n ** 2)  # masukkan rumus

# Output
print("Hasil:", total_sum)  # hasil akhir semua penjumlahan

# Cara 2 Untuk melihat hasil secara bertahap

total_sum = 0 #untuk menyimpan total awal

# Input
n = int(input("Masukkan nilai n: "))# untuk menyimpan input dari user di variabel

# Perhitungan menggunakan metode perulangan
for i in range(1, n+1):   # range harus sampai n, jadi gunakan n + 1
    rumus = (5*i-(i/n)**2)*(3/n) #masukan rumus notasi sigma
    total_sum += rumus #total awal akan ditambah dengan hasil rumus secara berkala
    print(f" untuk i = {i}, adalah = {rumus:.4f}, total= {total_sum:.4f}") #menampilkan hasil penjumlahan secara berkala

# Output
print("Total akhir:", total_sum) #hasil akhir total penjumlahan

#JANGAN LUPA HITUNG MANUAL DI BUKU TUGAS UNTUK PEMBUKTIAN
