from student import Student
class StudentController:
    def __init__(self, connection):
        self.connection = connection

    def addStudent(self, student):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s)", student.getValues())
        self.connection.commit()
        cursor.close()

    def getStudentById(self, student_id):
        cursor = self.connection.cursor()
        query = "SELECT id, nom, prenom, date FROM student WHERE id = %s"
        cursor.execute(query, (student_id,))
        result = cursor.fetchone()  # Fetch a single result
        cursor.close()
        return Student(*result)

    def getAllStudents(self):
        cursor = self.connection.cursor()
        query = "SELECT id, nom, prenom, date FROM student"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results

    def updateStudent(self, student):
        cursor = self.connection.cursor()
        query = """
        UPDATE student 
        SET nom = %s, prenom = %s, date = %s 
        WHERE id = %s
        """
        cursor.execute(query, (student.nom, student.prenom, student.date, student.id))
        self.connection.commit()
        cursor.close()

    def deleteStudent(self, id):
        cursor = self.connection.cursor()
        query = "DELETE FROM student WHERE id = %s"
        cursor.execute(query, (id,))
        self.connection.commit()
        cursor.close()

