import json

# 1. Définir la classe CarnetAdresses
class CarnetAdresses:
    def __init__(self, fichier="contacts.json"):
        self.fichier = fichier
        self.contacts = self.charger_contacts()

    # Méthode pour charger les contacts depuis un fichier
    def charger_contacts(self):
        try:
            with open(self.fichier, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    # Méthode pour sauvegarder les contacts dans un fichier
    def sauvegarder_contacts(self):
        with open(self.fichier, 'w') as f:
            json.dump(self.contacts, f, indent=4)

    # 2. Ajouter un contact
    def ajouter_contact(self, nom, email, telephone):
        self.contacts[nom] = {"email": email, "telephone": telephone}
        self.sauvegarder_contacts()
        print(f"Contact {nom} ajouté avec succès.")

    # 3. Supprimer un contact
    def supprimer_contact(self, nom):
        if nom in self.contacts:
            del self.contacts[nom]
            self.sauvegarder_contacts()
            print(f"Contact {nom} supprimé avec succès.")
        else:
            print(f"Le contact {nom} n'existe pas.")

    # 4. Rechercher un contact par nom
    def rechercher_contact(self, nom):
        if nom in self.contacts:
            info = self.contacts[nom]
            print(f"Nom : {nom}, Email : {info['email']}, Téléphone : {info['telephone']}")
        else:
            print(f"Le contact {nom} n'a pas été trouvé.")

# === Test du code ===

# Créer un objet CarnetAdresses
carnet = CarnetAdresses()

# Ajouter des contacts
carnet.ajouter_contact("HAMZA", "Hamza@example.com", "123456789")
carnet.ajouter_contact("SAIID", "saiid@example.com", "987654321")

# Rechercher un contact
carnet.rechercher_contact("HAMZA")

# Supprimer un contact
carnet.supprimer_contact("SAIID")

# Rechercher un contact supprimé
carnet.rechercher_contact("SAIID")
