import tkinter as tk
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
            return "livre emprunté"
    def rendre(self):
        self.statut="disponible"
        return "livre rendu"
class bibliotheque:
    def __init__(self,nom,adresse):
        self.nom=nom
        self.adresse=adresse
        self.listeLivre=[]
    def ajouter_livre(self,livre):
        if livre not in self.listeLivre:
            self.listeLivre.append(livre)
    def afficher_livre_disponible(self):
        for livre in self.listeLivre:
            if livre.statut=="disponible":
                return livre.titre
    def rechercher_livre(self,titre):
        for livre in self.listeLivre:
            if livre.titre==titre:
                return livre

if __name__ == "__main__":
    print("test")
    fenetre=tk.TK()
    fenetre.title("Projet Bibliotheque")
    fenetre.geometry("500x600")


    fenetre.mainloop()