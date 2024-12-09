from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from std1_def import *
from std_base import *
import mysql.connector


class StudentMain:
    def __init__(self):
        # Initialiser la connexion à la base de données MySQL
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Remplacez par votre utilisateur MySQL
            password="",  # Remplacez par votre mot de passe MySQL
            database="etudiant"  # Remplacez par le nom de votre base de données
        )

        # Initialiser le contrôleur des étudiants
        self.controller = StudentController(self.connection)

        # Initialiser la fenêtre principale
        self.window = Tk()
        self.window.geometry("900x500")
        self.window.configure(bg="#FFFFFF")
        # Charger les ressources
        self.ui = StudentUI(self.window, self.controller)

        # Initialiser l'interface utilisateur
        self.initialize_ui()



    def initialize_ui(self):
        # Charger les images et créer les éléments de l'interface


        # Ajoutez d'autres boutons et widgets similaires ici...
        self.ui.Table()
        self.ui.displaydata()



    def run(self):
        # Lancer la boucle principale de l'application
        self.window.resizable(False, False)
        self.window.mainloop()


# Démarrer l'application
if __name__ == "__main__":
    app = StudentMain()
    app.run()
