class livre:
    def __init__(self,titre,auteur,nbp,statut="disponible"):
        self.titre=titre
        self.auteur=auteur
        self.nombre_page=nbp
        self.statut=statut
    def afficher_details(self):
        return f"titre={self.titre} auteur={self.auteur} pages={self.nombre_page} statut={self.statut}"
    def emprunter(self):
        if self.statut=="disponible":
            self.statut="emprunté"
            print("le livre est emprunté")
        else:
            print("le livre est deja emprunté")
    def rendre(self):
        self.statut="disponible"
        print("le livre est maintenent disponible")

        