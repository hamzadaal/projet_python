import numpy as np
import matplotlib.pyplot as plt

# 1. Matrice de covariance
# Génération d’un tableau aléatoire (100 échantillons, 3 variables)
donnees = np.random.rand(100, 3)

# Calcul de la matrice de covariance (transposé nécessaire)
covariance = np.cov(donnees.T)
print("Matrice de covariance :\n", covariance)

# 2. Transformation de Fourier d’un signal sinusoïdal
# Génération d’un signal sinusoïdal
t = np.linspace(0, 1, 500)  # 500 points entre 0 et 1 seconde
signal = np.sin(2 * np.pi * 10 * t)  # sinusoïde à 10 Hz

# Application de la FFT (transformée de Fourier rapide)
frequences = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
spectre = np.abs(np.fft.fft(signal))

# Affichage du spectre de fréquences
plt.figure(figsize=(8, 4))
plt.plot(frequences[:len(frequences)//2], spectre[:len(spectre)//2])
plt.title("Spectre de fréquences")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.tight_layout()
plt.show()

# 3. Simulation de lancers de dés
# Lancer 2 dés 1000 fois
de1 = np.random.randint(1, 7, size=1000)
de2 = np.random.randint(1, 7, size=1000)
somme = de1 + de2

# Affichage de l’histogramme des sommes
plt.figure(figsize=(6, 4))
plt.hist(somme, bins=np.arange(2, 14) - 0.5, edgecolor='black', rwidth=0.8)
plt.title("Histogramme des sommes de deux dés (1000 lancers)")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.xticks(range(2, 13))
plt.grid(axis='y')
plt.tight_layout()
plt.show()
