# 1. Déclaration de la fonction pour vérifier la présence d'un élément dans une liste
def verifier_presence(liste, valeur):
    if valeur in liste:
        return True
    else:
        return False

# 2. Liste d'exemple
nombres = [4, 8, 15, 16, 23, 42]

# 3. Vérification avec deux éléments différents
existe_15 = verifier_presence(nombres, 15)
existe_50 = verifier_presence(nombres, 50)

# 4. Affichage des résultats
print(f"Est-ce que 15 est présent dans la liste ? {existe_15}")
print(f"Est-ce que 50 est présent dans la liste ? {existe_50}")

