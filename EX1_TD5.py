import numpy as np

# 1. Création des tableaux

# Tableau 1D contenant les entiers pairs de 0 à 18
tableau_1D = np.arange(0, 20, 2)
print("Nouveau tableau 1D :", tableau_1D)

# Tableau 2D (4x4) avec des entiers aléatoires entre 10 et 50
tableau_2D = np.random.randint(10, 50, size=(4, 4))
print("\nNouveau tableau 2D :\n", tableau_2D)

# Tableau 3D (2x2x3) rempli de 1
tableau_3D = np.ones((2, 2, 3))
print("\nNouveau tableau 3D :\n", tableau_3D)

# 2. Accès et modification des éléments

# Dernier élément du tableau 1D
print("\nDernier élément du tableau 1D :", tableau_1D[-1])

# Troisième ligne, deuxième colonne du tableau 2D
print("Élément [2][1] du tableau 2D :", tableau_2D[2, 1])

# Modifier plusieurs éléments dans le tableau 3D
tableau_3D[1, :, 1] = 9
print("\nTableau 3D après modification :\n", tableau_3D)
