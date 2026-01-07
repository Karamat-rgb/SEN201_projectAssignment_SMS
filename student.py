# student.py

class Student:
    def __init__(self, student_id, name, age, class_name):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.class_name = class_name

    def __str__(self):
        return f"{self.student_id} | {self.name} | {self.age} | {self.class_name}"
