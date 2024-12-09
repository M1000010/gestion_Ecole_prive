from tkinter import ttk, Entry, PhotoImage, Button, END, Canvas
from tkinter import *
from tkinter.ttk import Combobox

import mysql.connector
from std_base import *
from std_etd import *
from tkcalendar import DateEntry
from pathlib import Path



# Fonction de création des actions pour les boutons
def button_7_action():
    print("button_7 clicked")
    # Ajouter l'action que vous souhaitez pour le bouton 7 ici


def button_8_action():
    print("button_8 clicked")
    # Ajouter l'action que vous souhaitez pour le bouton 8 ici


def button_9_action():
    print("button_9 clicked")
    # Ajouter l'action que vous souhaitez pour le bouton 9 ici


class StudentUI:
    def __init__(self, window, cotroller):
        self.assets_path = Path(__file__).parent / Path(r"C:\Users\DELL\Desktop\projet BD\gestion Ecole "
                                                        r"prive\assets\frame0")
        self.controller = cotroller
        self.root = window
        self.root.title("Student Information")
        self.canvas = Canvas(
            self.root,
            bg="#FFFFFF",
            height=500,
            width=900,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.tree = None  # Référence au Treeview
        # Création des champs de saisie
        self.idF = None
        self.cinF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.cneF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.nomF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.prenomF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.dateF = DateEntry(self.root,width=12,background='darkblue',foreground='white',
                               borderwidth=2,date_pattern='yyyy-mm-dd')  # Format de la date
        self.numF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.mailF = Entry(self.root, bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
        self.selected_option = StringVar()
        self.choices = ["Choix 1", "Choix 2", "Choix 3"]
        self.filiereF = Combobox(self.root, values=self.choices)

        # id_etd
        self.entry_image_10 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_10.png")
        self.entry_bg_10 = self.canvas.create_image(
            205.0,
            363.0,
            image=self.entry_image_10
        )

        # cin_etd
        self.entry_image_9 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_9.png")
        self.entry_bg_9 = self.canvas.create_image(
            205.0,
            388.0,
            image=self.entry_image_9
        )
        # cne_etd
        self.entry_image_8 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_8.png")
        self.entry_bg_8 = self.canvas.create_image(
            205.0,
            413.0,
            image=self.entry_image_8
        )

        # nom_etd
        self.entry_image_7 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_7.png")
        self.entry_bg_7 = self.canvas.create_image(
            205.0,
            438.0,
            image=self.entry_image_7
        )
        # prenom etd
        self.entry_image_1 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            205.0,
            463.0,
            image=self.entry_image_1
        )

        # date_etd
        self.entry_image_6 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_6.png")
        entry_bg_6 = self.canvas.create_image(
            594.5,
            361.0,
            image=self.entry_image_6
        )

        # id_niv
        self.entry_image_3 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            594.5,
            436.0,
            image=self.entry_image_3
        )
        # num_etd
        self.entry_image_5 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_5.png")
        self.entry_bg_5 = self.canvas.create_image(
            594.5,
            386.0,
            image=self.entry_image_5
        )
        # mail_etd
        self.entry_image_4 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_4.png")
        self.entry_bg_4 = self.canvas.create_image(
            594.5,
            411.0,
            image=self.entry_image_4
        )

        # id_filiere
        self.entry_image_2 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            594.5,
            461.0,
            image=self.entry_image_2
        )
        # Ajout des boutons
        self.button_image_7 = PhotoImage(file="C:/Users/DELL/Desktop/projet BD/gestion Ecole "
                                              "prive/assets/frame0/button_7.png")
        self.button_7 = Button(self.root, image=self.button_image_7, borderwidth=0, highlightthickness=0,
                               command=self.addStudent, relief="flat")
        self.button_7.place(x=787.0, y=361.0, width=87.0, height=22.0)

        self.button_image_8 = PhotoImage(file="C:/Users/DELL/Desktop/projet BD/gestion Ecole "
                                              "prive/assets/frame0/button_8.png")
        self.button_8 = Button(self.root, image=self.button_image_8, borderwidth=0, highlightthickness=0,
                               command=self.updateStudent, relief="flat")
        self.button_8.place(x=787.0, y=400.0, width=87.0, height=22.0)

        self.button_image_9 = PhotoImage(file="C:/Users/DELL/Desktop/projet BD/gestion Ecole "
                                              "prive/assets/frame0/button_9.png")
        self.button_9 = Button(self.root, image=self.button_image_9, borderwidth=0, highlightthickness=0,
                               command=self.deletestudent, relief="flat")
        self.button_9.place(x=786.0, y=446.0, width=87.0, height=22.0)

        # Ajout des champs de saisie dans la fenêtre
        self.cinF.place(x=138.0, y=381.0, width=140.0, height=20.0)
        self.cneF.place(x=138.0, y=406.0, width=140.0, height=20.0)
        self.nomF.place(x=138.0, y=431.0, width=140.0, height=20.0)
        self.prenomF.place(x=138.0, y=456.0, width=140.0, height=20.0)
        self.dateF.place(x=527.0, y=354.0, width=140.0, height=20.0)
        self.numF.place(x=527.0, y=379.0, width=140.0, height=20.0)
        self.mailF.place(x=527.0, y=404.0, width=140.0, height=20.0)
        self.filiereF.place(x=527.0, y=454.0, width=140.0, height=20.0)



        self.image_image_1 = PhotoImage(file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_1.png")
        self.image_1 = self.canvas.create_image(
            450.0,
            95.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=627.0,
            y=119.0,
            width=71.0,
            height=24.0
        )

        self.button_image_2 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=810.0,
            y=119.0,
            width=78.0,
            height=24.0
        )

        self.button_image_3 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=532.0,
            y=119.0,
            width=78.0,
            height=24.0
        )

        self.button_image_4 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_4.png")
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=431.0,
            y=119.0,
            width=84.0,
            height=24.0
        )

        self.button_image_5 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_5.png")
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=330.0,
            y=119.0,
            width=84.0,
            height=24.0
        )

        self.button_image_6 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_6.png")
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=715.0,
            y=119.0,
            width=78.0,
            height=24.0
        )

        self.image_image_2 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_2.png")
        self.image_2 = self.canvas.create_image(
            851.0,
            38.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_3.png")
        self.image_3 = self.canvas.create_image(
            271.0,
            137.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_4.png")
        self.image_4 = self.canvas.create_image(
            450.0,
            266.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_5.png")
        self.image_5 = self.canvas.create_image(
            394.0,
            413.0,
            image=self.image_image_5
        )

        self.button_image_10 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_10.png")
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=778.0,
            y=159.0,
            width=87.0,
            height=23.0
        )

        self.entry_image_11 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/entry_11.png")
        self.entry_bg_11 = self.canvas.create_image(
            435.0,
            171.0,
            image=self.entry_image_11
        )
        self.entry_11 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_11.place(
            x=97.0,
            y=159.0,
            width=676.0,
            height=22.0
        )

        self.image_image_6 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/image_6.png")
        self.image_6 = self.canvas.create_image(
            53.0,
            171.0,
            image=self.image_image_6
        )

        self.button_image_11 = PhotoImage(
            file="C:/Users/DELL/Desktop/projet BD/gestion Ecole prive/assets/frame0/button_11.png")
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_11.place(
            x=128.0,
            y=120.0,
            width=84.0,
            height=24.0
        )

    def displaydata(self):
        self.loadStudents()

    def loadStudents(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        students = self.controller.getAllStudents()
        for etudiant in students:
            self.tree.insert("", "end", values=etudiant)

    # Fonction d'ajout d'un étudiant (à personnaliser selon votre logique)
    def addStudent(self):
        print("Ajouter un étudiant")
        # Code pour ajouter un étudiant, par exemple :
        student = etudiant(None, self.cinF.get(), self.cneF.get(),self.nomF.get(), self.prenomF.get(), self.dateF.get(),
                           self.numF.get(), self.mailF.get(), self.filiereF.get())
        self.controller.addStudent(student)
        self.loadStudents()
        self.clearForm()

    def updateStudent(self):
        selected_item = self.tree.selection()
        if not selected_item:
            print("Aucun étudiant sélectionné")
            messagebox.showinfo("Erreur", "Aucun étudiant sélectionné")
            return
        cin_etd = self.cinF.get()
        cne_etd = self.cneF.get()
        nom_etd = self.nomF.get()
        prenom_etd = self.prenomF.get()
        date_n_etd = self.dateF.get()
        num_etd = self.numF.get()
        mail_etd = self.mailF.get()
        filiere = self.filiereF.get()
        values = self.tree.item(selected_item, 'values')
        id_etd = values[0]
        if not (cin_etd and cne_etd and nom_etd and prenom_etd and date_n_etd and num_etd and mail_etd and filiere):
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        student = etudiant(
            id_etd=int(id_etd),
            cin_etd=cin_etd,
            cne_etd=cne_etd,
            nom_etd=nom_etd,
            prenom_etd=prenom_etd,
            date_n_etd=date_n_etd,
            num_etd=int(num_etd),
            mail_etd=mail_etd,
            filiere=filiere
        )

        self.controller.updateStudent(student)

        # Recharger la liste des étudiants et effacer le formulaire
        self.loadStudents()
        self.clearForm()
        messagebox.showinfo("Succès", "Étudiant modifié avec succès.")


    def deletestudent(self):
        print("delete student")
        # Appeler la méthode onRowClick pour récupérer l'ID de l'étudiant sélectionné
        selected_item = self.tree.selection()  # Retourne un tuple avec l'ID de l'élément sélectionné
        if selected_item:
            # Récupérer l'ID de l'étudiant à partir de la sélection (assume que l'ID est dans la première colonne)
            id_etd = self.tree.item(selected_item, 'values')[0]

            # Passer l'ID à la méthode du contrôleur
            self.controller.deleteStudent(id_etd)
            self.loadStudents()
            self.clearForm()


        else:
            print("No student selected")
            messagebox.showinfo("Error", "No student selected")

    def fillForm(self, student):
        self.clearForm()
        self.cinF.insert(0, student.cin)
        self.cneF.insert(0, student.cne)
        self.nomF.insert(0, student.nom)
        self.prenomF.insert(0, student.prenom)
        self.dateF.insert(0, student.date_naissance)
        self.numF.insert(0, student.numero)
        self.mailF.insert(0, student.email)
        self.filiereF.insert(0, student.filiere)

    def clearForm(self):
        self.cinF.delete(0, END)
        self.cneF.delete(0, END)
        self.nomF.delete(0, END)
        self.prenomF.delete(0, END)
        self.dateF.delete(0, END)
        self.numF.delete(0, END)
        self.mailF.delete(0, END)
        self.filiereF.delete(0, END)
        self.idF = None


    def Table(self):
        """
        Initialise le tableau des étudiants avec colonnes et barre de défilement.
        """
        # Création du Treeview
        self.tree = ttk.Treeview(self.root, columns=(
            "id_etd", "cin_etd", "cne_etd", "nom_etd", "prenom_etd", "date_n_etd", "num_etd", "mail_etd", "filiere"
        ), show="headings", height=5)

        # Définition des en-têtes des colonnes
        self.tree.heading("id_etd", text="ID étudiant")
        self.tree.heading("cin_etd", text="CIN")
        self.tree.heading("cne_etd", text="CNE")
        self.tree.heading("nom_etd", text="Nom")
        self.tree.heading("prenom_etd", text="Prénom")
        self.tree.heading("date_n_etd", text="Date de naissance")
        self.tree.heading("num_etd", text="Numéro Tel")
        self.tree.heading("mail_etd", text="Mail")
        self.tree.heading("filiere", text="Filière")

        # Configuration des dimensions et alignements des colonnes
        self.tree.column("id_etd", width=90, anchor="center")
        self.tree.column("cin_etd", width=90, anchor="center")
        self.tree.column("cne_etd", width=90, anchor="center")
        self.tree.column("nom_etd", width=100, anchor="center")
        self.tree.column("prenom_etd", width=100, anchor="center")
        self.tree.column("date_n_etd", width=100, anchor="center")
        self.tree.column("num_etd", width=120, anchor="center")
        self.tree.column("mail_etd", width=120, anchor="center")
        self.tree.column("filiere", width=90, anchor="center")

        # Ajout d'une barre de défilement verticale
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Placement du Treeview et de la barre de défilement
        self.tree.grid(row=0, column=0, sticky="nsew", padx=(10, 0), pady=10)

        # Définition des styles pour les lignes
        self.tree.tag_configure("evenrow", background="#ffffff")
        self.tree.tag_configure("oddrow", background="#f0f0f0")

        # Placement dans un canvas si nécessaire
        if self.canvas:
            self.canvas.create_window(450.0, 266.0, window=self.tree)

        # Liaison de l'événement de clic sur une ligne
        self.tree.bind("<ButtonRelease-1>", self.onRowClick)

    def onRowClick(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_data = self.tree.item(selected_item[0])
            student_data = item_data["values"]
            student_id = student_data[0]
            student = self.controller.getStudentById(student_id)
            print("Étudiant sélectionné :", student_data)
            self.fillForm(student)
