import numpy as np

# Fixer la graine pour des résultats reproductibles
np.random.seed(42)

# 1. Générer le tableau des ventes (12 mois x 3 produits)
ventes = np.random.randint(100, 1001, size=(12, 3))
mois = np.array(["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"])
produits = ['P1', 'P2', 'P3']

print("=== VENTES MENSUELLES ===")
print(ventes)

# 2. Total annuel par produit
totaux_produits = ventes.sum(axis=0)
print("\n=== TOTALS ANNUELS PAR PRODUIT ===")
for i, produit in enumerate(produits):
    print(f"{produit} : {totaux_produits[i]}")

# 3. Moyenne mensuelle par produit
moyennes_produits = ventes.mean(axis=0)
print("\n=== MOYENNES MENSUELLES PAR PRODUIT ===")
for i, produit in enumerate(produits):
    print(f"{produit} : {moyennes_produits[i]:.2f}")

# 4. Mois avec les ventes maximales pour chaque produit
mois_max = ventes.argmax(axis=0)
print("\n=== MOIS AVEC LES VENTES MAXIMALES ===")
for i, produit in enumerate(produits):
    print(f"{produit} : {mois[mois_max[i]]} ({ventes[mois_max[i], i]})")

# 5. Croissance mensuelle en pourcentage
croissance = np.diff(ventes, axis=0) / ventes[:-1] * 100
print("\n=== CROISSANCE MENSUELLE EN % ===")
print(np.round(croissance, 2))

# 6. Mois avec la plus forte croissance pour chaque produit
mois_croissance_max = croissance.argmax(axis=0) + 1  # +1 car np.diff diminue de 1 ligne
print("\n=== MOIS AVEC LA PLUS FORTE CROISSANCE ===")
for i, produit in enumerate(produits):
    index = mois_croissance_max[i]
    print(f"{produit} : {mois[index]} (+{croissance[index-1, i]:.2f}%)")

# 7. Somme des ventes par mois (tous produits)
somme_mensuelle = ventes.sum(axis=1)
print("\n=== SOMME DES VENTES PAR MOIS (TOUS PRODUITS) ===")
for i in range(12):
    print(f"{mois[i]} : {somme_mensuelle[i]}")
