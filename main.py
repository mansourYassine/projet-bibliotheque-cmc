from src.Livre import Livre
from src.Bibliotheque import Bibliotheque
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def check_login():
    user = user_name.get()
    password = user_password.get()

    if user == "yassine" and password == "1234":
        show_main_app()
    else:
        messagebox.showerror(message="Le nom d'utilisateur ou mot de passe est incorrect")

def show_main_app():
    login_frame.pack_forget()  # hide login
    main_frame.pack(fill="both", expand=True)

def ajoute_livre():
    nv_titre = titre_livre.get()
    nv_auteur = auteur_livre.get()
    nv_nbre_page = nbre_page_livre.get()
    
    livre = Livre(nv_titre, nv_auteur, nv_nbre_page)
    # ajouter le livre dans Bibliotheque.listeLivres[] et dans le fichier csv
    biblio.ajouter_livre(livre)
    # Ajouter le livre dans la page de Afficher livres disponibles
    afficher_dispo_livres()
    messagebox.showinfo(message="le livre a été ajouté avec succès")

def afficher_dispo_livres():
    # define columns
    tree["columns"] = ("titre", "auteur", "nombre page", "statut")

    # format columns
    tree.column("#0", width=0, stretch=NO)  # hidden first column
    tree.column("titre", anchor="center")
    tree.column("auteur", anchor="center")
    tree.column("nombre page", anchor="center")
    tree.column("statut", anchor="center")

    # headings
    tree.heading("#0", text="")
    tree.heading("titre", text="titre")
    tree.heading("auteur", text="auteur")
    tree.heading("nombre page", text="nombre page")
    tree.heading("statut", text="statut")

    # insert data
    for livre in biblio.afficher_livre_disponible():
        tree.insert("", "end", values=(livre.titre, livre.auteur, livre.nombre_page, livre.statut))

    tree.pack(fill="both", expand=True)


root = Tk()
root.geometry("500x500")
root.title("Bibliothèque CMC")
root.config(bg="#04bfb0")

biblio = Bibliotheque("Bibliothèque CMC", "Deroua")
biblio.charger_livre() # Charger les livres dans l'attribut listeLivres[] depuis csv

# ------------------------------Page de se connecter-------------------------------------------------
login_frame = Frame(root, bg="#04bfb0")
login_frame.pack(fill="both", expand=True)

formulaire = Frame(login_frame)
formulaire.pack()

# Titre de formulaire
Label(formulaire, text="Connecter à votre compte", font=("arial", 20)).grid(row=0, column=0, columnspan=2)

#Nom utilisateur
Label(formulaire, text="Nom Utilisateur:").grid(row=1, column=0)
user_name = Entry(formulaire, font=('arial', 20))
user_name.grid(row=1, column=1)

# mot de passe
Label(formulaire, text="Mot de passe:").grid(row=2, column=0)
user_password = Entry(formulaire, font=('arial', 20), show="*")
user_password.grid(row=2, column=1)

Button(formulaire, text="se connecter", command=check_login).grid(row=3, column=0, columnspan=2)

# ----------------------------------------L'application principale---------------------------------------------
main_frame = Frame(root, bg="white")
# main_frame.pack(fill="both", expand=True) # This line should be removed when you incomment the login code

notebook = ttk.Notebook(main_frame)

# --------------------------Afficher livres disponibles----------------------------
afficher_livres_tab = Frame(notebook, bg="#04bfb0")
notebook.add(afficher_livres_tab, text="Afficher livres disponibles")

tree = ttk.Treeview(afficher_livres_tab)
afficher_dispo_livres()


# --------------------------Ajouter livre---------------------------------------
ajoute_tab = Frame(notebook, bg="#04bfb0")
notebook.add(ajoute_tab, text="Ajouter Livre")

form_frame = Frame(ajoute_tab)
form_frame.pack()
title_form = Label(form_frame, text="Entrer les informations de livre:")
title_form.grid(row=0, column=0, columnspan=2)
# Titre
Label(form_frame, text="Titre").grid(row=1, column=0)
titre_livre = Entry(form_frame)
titre_livre.grid(row=1, column=1)
# Auteur
Label(form_frame, text="Auteur").grid(row=2, column=0)
auteur_livre = Entry(form_frame)
auteur_livre.grid(row=2, column=1)
# nombre pages
Label(form_frame, text="Nbre pages").grid(row=3, column=0)
nbre_page_livre = Entry(form_frame)
nbre_page_livre.grid(row=3, column=1)
# Enregistrer
Button(form_frame, text="Ajouter", command=ajoute_livre).grid(row=4, column=0, columnspan=2)

notebook.pack(expand=True, fill='both')
#------------------------Rechercher_livre-------------------------------------
recherche_tab=Frame(notebook, bg="#04bfb0")
notebook.add(recherche_tab, text="Rechercher Livre")

rech_var = StringVar()

Label(recherche_tab,text="Titre").pack()
Entry(recherche_tab,textvariable=rech_var).pack()
#zone_resultats
result_txt=Text(recherche_tab, height=5)
result_txt.pack()
#fonction
def rechercher_livre_par_titre():
    result_txt.delete(1.0, END)
    livre = biblio.rechercher_livre(rech_var.get())
    if livre:
        result_txt.insert(END,livre.afficher_details())
    else:
        result_txt.insert(END,"Livre non trouvé")
#pour_chercher
Button(recherche_tab,text="Rechercher",command=rechercher_livre_par_titre).pack()

# start app
root.mainloop()