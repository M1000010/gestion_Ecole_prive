import mysql.connector
from tkinter import *
from student_controller import StudentController
from student_ui import StudentUI


def main():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Remplacez par votre utilisateur MySQL
        password="",  # Remplacez par votre mot de passe MySQL
        database="gestion_donnees"
    )
    controller = StudentController(connection)

    root = Tk()
    root.title("Gestion des Données")
    root.geometry("1000x500")
    ui = StudentUI(root, controller)
    ui.display()
    root.mainloop()


main()
