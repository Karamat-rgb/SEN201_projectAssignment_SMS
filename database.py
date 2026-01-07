# database.py

from student import Student

students = []

def add_student(student):
    students.append(student)

def view_students():
    return students

def find_student(student_id):
    return [s for s in students if s.student_id == student_id]

def update_student(student_id, name, age, class_name):
    for s in students:
        if s.student_id == student_id:
            s.name = name
            s.age = age
            s.class_name = class_name
            return True
    return False

def delete_student(student_id):
    global students
    students = [s for s in students if s.student_id != student_id]
