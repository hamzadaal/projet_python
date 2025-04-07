# 1. Définir la fonction pour extraire les nombres pairs
def extraire_pairs(liste):
    return [nombre for nombre in liste if nombre % 2 == 0]

# 2. Tester la fonction avec une liste d'exemple
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nombres_pairs = extraire_pairs(nombres)

# 3. Afficher la liste des nombres pairs
print("Nombres pairs :", nombres_pairs)
