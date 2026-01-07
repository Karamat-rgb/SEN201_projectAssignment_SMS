# main.py

from student import Student
import database

def menu():
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    return input("Choose option: ")

while True:
    choice = menu()

    if choice == "1":
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        cls = input("Class: ")
        student = Student(sid, name, age, cls)
        database.add_student(student)
        print("✔️ Student Added")

    elif choice == "2":
        print("\n--- Students List ---")
        for s in database.view_students():
            print(s)

    elif choice == "3":
        sid = input("ID to update: ")
        name = input("New Name: ")
        age = input("New Age: ")
        cls = input("New Class: ")
        updated = database.update_student(sid, name, age, cls)
        print("✔️ Updated" if updated else "❌ Not Found")

    elif choice == "4":
        sid = input("ID to delete: ")
        database.delete_student(sid)
        print("✔️ Deleted (if existed)")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
