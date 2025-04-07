# 1. Fonction qui retourne une nouvelle liste contenant les carrés des éléments
def liste_carres(liste):
    return [x**2 for x in liste]

# 2. Liste d'exemple
nombres = [1, 2, 3, 4, 5, 6]

# 3. Test de la fonction
carres = liste_carres(nombres)

# 4. Affichage du résultat
print("Liste des carrés :", carres)
