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