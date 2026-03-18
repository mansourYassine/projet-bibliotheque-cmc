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
        messagebox.showerror(message="User name or password is wrong")

def show_main_app():
    login_frame.pack_forget()  # hide login
    main_frame.pack(fill="both", expand=True)


root = Tk()
root.geometry("500x500")
root.title("Bibliothèque CMC")
root.config(bg="#04bfb0")

# ----LOGIN FRAME----
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

# ----MAIN APP FRAME----
main_frame = Frame(root, bg="white")

# start app
root.mainloop()