# 1. Fonction qui retourne le minimum et le maximum d'une liste
def trouver_min_max(liste):
    minimum = min(liste)
    maximum = max(liste)
    return (minimum, maximum)

# 2. Liste d'exemple
nombres = [4, 8, 15, 16, 23, 42]

# 3. Appel de la fonction
resultat = trouver_min_max(nombres)

# 4. Affichage du résultat
print("Valeurs extrêmes de la liste :", resultat)
