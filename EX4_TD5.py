import numpy as np

# 1. Statistiques sur un tableau 5x5
tableau = np.random.rand(5, 5)
print("Tableau aléatoire (5x5) :\n", tableau)

print("\n--- Statistiques par ligne ---")
print("Moyenne :", np.mean(tableau, axis=1))
print("Écart-type :", np.std(tableau, axis=1))
print("Minimum :", np.min(tableau, axis=1))
print("Maximum :", np.max(tableau, axis=1))

print("\n--- Statistiques par colonne ---")
print("Moyenne :", np.mean(tableau, axis=0))
print("Écart-type :", np.std(tableau, axis=0))
print("Minimum :", np.min(tableau, axis=0))
print("Maximum :", np.max(tableau, axis=0))

# 2. Tri et indice du max
tableau_aleatoire = np.random.rand(10)
print("\nTableau 1D aléatoire :", tableau_aleatoire)

tableau_trie = np.sort(tableau_aleatoire)
indice_max = np.argmax(tableau_aleatoire)

print("Tableau trié :", tableau_trie)
print("Indice de l'élément maximum :", indice_max)

# 3. Broadcasting : multiplication tableau 1D x tableau 2D
vecteur = np.array([2, 4, 6, 8])
matrice = np.random.randint(1, 10, size=(3, 4))

print("\nVecteur 1D :", vecteur)
print("Matrice 2D (3x4) :\n", matrice)

resultat = matrice * vecteur
print("Résultat du broadcasting (multiplication) :\n", resultat)
