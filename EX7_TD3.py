# 1. Création de la deuxième liste
autres_nombres = [7, 11, 19, 24, 33]

# 2. Fonction qui fusionne deux listes et les trie
def fusionner_et_trier(liste1, liste2):
    liste_fusionnee = liste1 + liste2
    return sorted(liste_fusionnee)

# Liste d'exemple (tu peux changer les valeurs si besoin)
nombres = [4, 8, 15, 16, 23, 42]

# 3. Test de la fonction
resultat = fusionner_et_trier(nombres, autres_nombres)

# Affichage du résultat
print("Liste fusionnée et triée :", resultat)
