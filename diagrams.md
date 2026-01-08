classDiagram
    class Student {
      - student_id: str
      - name: str
      - age: int
      - class_name: str
      + __init__(student_id, name, age, class_name)
      + __str__()
    }

    class database {
      - students: list
      + add_student(student)
      + view_students()
      + find_student(student_id)
      + update_student(student_id, name, age, class_name)
      + delete_student(student_id)
    }

    Student --> database : stored insequenceDiagram
    actor User
    participant CLI as main.py
    participant DB as database.py
    participant S as Student

    User->>CLI: choose Add Student
    CLI->>User: prompt id,name,age,class
    User-->>CLI: enter fields
    CLI->>S: create Student(id,name,age,class)
    CLI->>DB: add_student(student)
    DB-->>CLI: success
    CLI-->>User: "Student added successfully"
