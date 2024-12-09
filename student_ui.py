from tkinter import *
from tkinter.ttk import Treeview

from student import Student

class StudentUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.id = None
        self.nomField = Entry(self.root, width=30)
        self.prenomField = Entry(self.root, width=30)
        self.dateField = Entry(self.root, width=30)
        self.addButton = Button(self.root, width=30, command=self.addStudent)
        self.records = Treeview(self.root, columns = ("id", "nom", "prenom", "date"))


    def addStudent(self):
        student = Student(None, self.nomField.get(), self.prenomField.get(), self.dateField.get())
        print(student.getValues())
        self.controller.addStudent(student)
        self.loadStudents()

    def display(self):
        self.addButton.pack()
        self.nomField.pack()
        self.prenomField.pack()
        self.dateField.pack()
        self.records.pack()
        self.loadStudents()
        self.records.bind("<ButtonRelease-1>", self.onRowClick)

    def loadStudents(self):
        for item in self.records.get_children():
            self.records.delete(item)
        students = self.controller.getAllStudents()
        for student in students:
            self.records.insert("", "end", values=student)

    def onRowClick(self, event):
        selected_item = self.records.selection()
        if selected_item:
            item_data = self.records.item(selected_item[0])
            student_data = item_data["values"]
            student_id = student_data[0]
            student = self.controller.getStudentById(student_id)
            self.fillForm(student)
            self.loadStudents()

    def fillForm(self, student):
        self.clearForm()
        self.nomField.insert(0, student.nom )
        self.prenomField.insert(0, student.prenom)
        self.dateField.insert(0, student.date)

    def clearForm(self):
        self.nomField.delete(0, END)
        self.prenomField.delete(0, END)
        self.dateField.delete(0, END)
        self.id = None