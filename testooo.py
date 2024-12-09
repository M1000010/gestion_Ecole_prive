import tkinter as tk
from tkinter import ttk, messagebox

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des étudiants")
        self.root.geometry("600x400")

        # Données simulées (liste en mémoire)
        self.students = []
        self.selected_student_id = None

        # Interface utilisateur
        self.setup_ui()

    def setup_ui(self):
        # Champs de saisie
        tk.Label(self.root, text="Nom:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Âge:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=10)

        # Boutons
        tk.Button(self.root, text="Ajouter", command=self.add_student).grid(row=2, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Modifier", command=self.update_student).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Supprimer", command=self.delete_student).grid(row=2, column=2, padx=10, pady=10)

        # Tableau
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Âge"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Âge", text="Âge")
        self.tree.column("ID", width=50)
        self.tree.column("Nom", width=200)
        self.tree.column("Âge", width=100)
        self.tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Événement de sélection
        self.tree.bind("<<TreeviewSelect>>", self.on_row_select)

    def add_student(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        if not name or not age:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Erreur", "L'âge doit être un nombre.")
            return

        student_id = len(self.students) + 1
        self.students.append({"id": student_id, "name": name, "age": age})
        self.load_students()
        self.clear_form()
        messagebox.showinfo("Succès", "Étudiant ajouté avec succès.")

    def update_student(self):
        if self.selected_student_id is None:
            messagebox.showerror("Erreur", "Aucun étudiant sélectionné.")
            return

        name = self.name_entry.get()
        age = self.age_entry.get()

        if not name or not age:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
            return

        try:
            age = int(age)
        except ValueError:
            messagebox.showerror("Erreur", "L'âge doit être un nombre.")
            return

        for student in self.students:
            if student["id"] == self.selected_student_id:
                student["name"] = name
                student["age"] = age
                break

        self.load_students()
        self.clear_form()
        messagebox.showinfo("Succès", "Étudiant modifié avec succès.")

    def delete_student(self):
        if self.selected_student_id is None:
            messagebox.showerror("Erreur", "Aucun étudiant sélectionné.")
            return

        self.students = [s for s in self.students if s["id"] != self.selected_student_id]
        self.load_students()
        self.clear_form()
        messagebox.showinfo("Succès", "Étudiant supprimé avec succès.")

    def load_students(self):
        # Vider le tableau
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Charger les données
        for student in self.students:
            self.tree.insert("", "end", values=(student["id"], student["name"], student["age"]))

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.selected_student_id = None

    def on_row_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            values = self.tree.item(selected_item, "values")
            self.selected_student_id = int(values[0])
            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.name_entry.insert(0, values[1])
            self.age_entry.insert(0, values[2])

# Lancer l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
