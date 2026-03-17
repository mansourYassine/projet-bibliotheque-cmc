class Bibliotheque:
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