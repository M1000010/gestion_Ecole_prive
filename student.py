class Student:
    def __init__(self, id, nom, prenom, date):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date = date

    def getValues(self):
        return self.id, self.nom, self.prenom, self.date