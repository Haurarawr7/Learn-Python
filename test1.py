# Soal 1 : Hasil dari Sigma 1/3i dengan i=1 dan n=7
# Cara 1 Langsung Jumlah

total_sum = 0  #untuk menyimpan total awal

# Pengulangan
for i in range(1, 8):  # untuk n =7, range adalah limitasi
    total_sum += 1 / (3 * i) # masukan rumus

# output
print("Hasil:", total_sum) #hasil akhir semua penjumlahan

#JANGAN LUPA HITUNG MANUAL DI BUKU TUGAS UNTUK PEMBUKTIAN
