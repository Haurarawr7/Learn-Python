# Soal 1 : Hasil dari Sigma 1/3i dengan i=1 dan n=7
# Cara 1 Langsung Jumlah

total_sum = 0  #untuk menyimpan total awal

# Pengulangan
for i in range(1, 8):  # untuk n =7, range adalah limitasi
    total_sum += 1 / (3 * i) # masukan rumus

# output
print("Hasil:", total_sum) #hasil akhir semua penjumlahan

# Cara 2 Untuk melihat hasil secara bertahap
total_sum = 0

# Perhitungan menggunakan metode perulangan
for i in range(1, 8):  # untuk n=7
    rumus = 1 / (3*i) #masukan rumus notasi sigma
    total_sum += rumus #total awal akan ditambah dengan hasil rumus secara berkala
    print(f" untuk i = {i}, adalah = {rumus:.4f}, total= {total_sum:.4f}") #menampilkan hasil penjumlahan secara berkala

# Output
print("Total akhir:", total_sum) #hasil akhir total penjumlahan

#JANGAN LUPA HITUNG MANUAL DI BUKU TUGAS UNTUK PEMBUKTIAN
