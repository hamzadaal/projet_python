# 1. Liste des jours de la semaine
Semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
print("Jours de la semaine :")
for jour in Semaine:
    print("-", jour)

# 2. Liste des couleurs avec boucle
Couleurs = []
for couleur in ["Rouge", "Orange", "Bleu", "Violet", "Vert"]:
    Couleurs.append(couleur)
print("\nCouleurs sélectionnées :")
for c in Couleurs:
    print("-", c)

# 3. Liste de réels et affichage de certains indices
Reels = [10.1, 20.5, 30.0, 40.3, 50.6, 60.9, 70.2]
indices_a_afficher = [1, 3, 5]
print("\nÉléments aux indices 1, 3 et 5 :")
for i in indices_a_afficher:
    print(f"Indice {i} : {Reels[i]}")
