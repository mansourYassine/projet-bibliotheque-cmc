import csv
from .Livre import Livre

# from Livre import *
class Bibliotheque:
    def __init__(self,nom,adresse):
        self.nom=nom
        self.adresse=adresse
        self.listeLivres=[]
        
    def charger_livre(self):
        with open('liste_livres.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                livre = Livre(row['titre'] ,row['auteur'], row['nbre_page'], row['statut'])
                self.listeLivres.append(livre)

    def ajouter_livre(self, livre):
        self.listeLivres.append(livre)
        
        with open('liste_livres.csv', mode='a', newline='') as file:
            fieldnames = ['titre', 'auteur', 'nbre_page', 'statut']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({
                'titre': livre.titre,
                'auteur': livre.auteur,
                'nbre_page' : livre.nombre_page,
                'statut' : livre.statut
            })

    def afficher_livre_disponible(self):
        livres_dispo = []
        for livre in self.listeLivres:
            if livre.statut=="disponible":
                livres_dispo.append(livre)
        return livres_dispo

    def rechercher_livre(self,titre):
        for livre in self.listeLivres:
            if livre.titre==titre:
                return livre