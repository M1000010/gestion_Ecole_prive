import tkinter as tk

# Créer la fenêtre principale
root = tk.Tk()
root.title("Tester la couleur")

# Définir la taille de la fenêtre
root.geometry("400x300")

# Modifier la couleur de fond de la fenêtre
root.config(bg="#0BD0CE")

# Ajouter un label au centre
label = tk.Label(root, text="Couleur de fond : #0BD0CE", fg="white", font=("Arial", 14), bg="#0BD0CE")
label.pack(expand=True)

# Lancer la boucle principale pour afficher la fenêtre
root.mainloop()

