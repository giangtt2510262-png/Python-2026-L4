#1:
class Student:
    def __init__(self, student_id, name, gpa):
        self.student_id = student_id
        self.name = name
        self.gpa = gpa

    def show_info(self):
        print(f"Student ID: {self.student.id} , Name: {self.name}  , Gpa:{self.gpa}")
    def is_excellent(self):
        return self.gpa >= 8.0

 sv1 = Student("SV01", "Trinh Truong Giang", 8.5)
 sv1.show_info()
 print("Excellent Student:",sv1.is_excellent())           