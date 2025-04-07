import numpy as np

# 1. Opérations élément par élément
x = np.array([10, 20, 30, 40, 50])
y = np.array([2, 4, 6, 8, 10])

# Opérations
somme = x + y
diff = x - y
produit = x * y
quotient = x / y

print("Somme :", somme)
print("Différence :", diff)
print("Produit :", produit)
print("Quotient :", quotient)

# 2. Fonctions mathématiques sur un tableau linéaire de -π à π
angles = np.linspace(-np.pi, np.pi, 7)

tan_values = np.tan(angles)
log_values = np.log(np.abs(angles) + 1)  # +1 pour éviter log(0)
sqrt_values = np.sqrt(np.abs(angles))

print("\nAngles de -π à π :", angles)
print("tan :", tan_values)
print("log(|x|+1) :", log_values)
print("sqrt(|x|) :", sqrt_values)

# 3. Sélection et remplacement dans un tableau
nombres = np.arange(15)  # tableau de 0 à 14

# Sélection des multiples de 3
multiples_3 = nombres[nombres % 3 == 0]
print("\nMultiples de 3 :", multiples_3)

# Remplacement des multiples de 5 par 100
nombres_modif = nombres.copy()
nombres_modif[nombres_modif % 5 == 0] = 100
print("Tableau après remplacement des multiples de 5 par 100 :", nombres_modif)
