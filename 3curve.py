#Step 3 : Bagilah interval [0,2] menjadi 5 partisi dengan syarat setiap partisi harus memiliki lebar yang sama, gambarkan partisi tersebut untuk membagi daerah A secara vertikal
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # 100 titik dari 0 ke 2 (agar tidak patah2)
y = -x**2 + 5  #masukan fungsi

# Buat garis
plt.plot(x, y, label='f(x) = -x^2 + 5', color='blue')  # garis f(x)
plt.axvline(x=2, label='x=2', color='red') # garis interval 2

# Arsiran
plt.fill_between(x, y, where=(y >= 0), color='lightblue', alpha=0.5, label='A')

#Partisi
partisi = np.linspace(0, 2, 6)  # Titik partisi: 0, 0.4, 0.8, 1.2, 1.6, 2
for p in partisi:
    plt.axvline(x=p, color='green', linestyle='--', linewidth=0.8,)  # Gambar garis vertikal
    plt.text(p, 0.5, f'{p:.1f}', color='black', ha='center', va='bottom')  # Label partisi

# Diagram Kartesius
plt.title(' f(x) = -x^2 + 5')  # judul
plt.xlabel('x')  # Label x
plt.ylabel('f(x)')  # Label f(x)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()  # Memunculkan label

# Show the plot
plt.show()
