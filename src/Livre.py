class Livre:
    nombre_livre=0
    def __init__(self,titre,auteur,nbp,statut="disponible"):
        Livre.nombre_livre += 1
        self.id_livre= Livre.nombre_livre
        self.titre=titre
        self.auteur=auteur
        self.nombre_page=nbp
        self.statut=statut

    def afficher_details(self):
        return f"id : {self.id_livre} | titre : {self.titre} | auteur : {self.auteur} | pages : {self.nombre_page} | statut : {self.statut}"

    def emprunter(self):
        if self.statut=="disponible":
            self.statut="emprunté"
            return "livre emprunté"

    def rendre(self):
        self.statut="disponible"
        return "livre rendu"