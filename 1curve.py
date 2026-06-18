#Step 1 : Gambarkanlah kurva f(x) = -x2 +5 pada interval [0,2]
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 100)  # 100 titik dari 0 ke 2 (agar tidak patah2)
y = -x**2 + 5  #masukan fungsi

# Buat garis
plt.plot(x, y, label='f(x) = -x^2 + 5', color='blue')  # garis f(x)
plt.axvline(x=2, label='x=2', color='red') # garis interval 2

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
