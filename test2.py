# Soal 2 : Hasil dari Sigma 2/i+5 dengan i=1 dan n=10
# Cara 1 Langsung Jumlah

total_sum = 0  #untuk menyimpan total awal

# Pengulangan
for i in range(1, 11):  # untuk n =10, range adalah limitasi
    total_sum += 2 / (i + 5) # masukan rumus

# output
print("Hasil:", total_sum) #hasil akhir semua penjumlahan

# Cara 2 Untuk melihat hasil secara bertahap
total_sum = 0

# Perhitungan menggunakan metode perulangan
for i in range(1, 11):  # untuk n=10
    rumus = 2 / (i + 5) #masukan rumus notasi sigma
    total_sum += rumus #total awal akan ditambah dengan hasil rumus secara berkala
    print(f" untuk i = {i}, adalah = {rumus:.4f}, total= {total_sum:.4f}") #menampilkan hasil penjumlahan secara berkala

# Output
print("Total akhir:", total_sum) #hasil akhir total penjumlahan

#JANGAN LUPA HITUNG MANUAL DI BUKU TUGAS UNTUK PEMBUKTIAN
