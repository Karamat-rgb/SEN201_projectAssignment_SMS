# SEN201_projectAssignment_SMS
A simple command-line Student Management System built with Python that allows users to manage student records efficiently
Student Management System (SMS)
📌 Project Description

The Student Management System (SMS) is a command-line based software application developed using Python to manage student records efficiently. The system allows users to add, view, update, and delete student information such as Student ID, Name, Age, and Class.

This project was developed following the Software Development Life Cycle (SDLC) and demonstrates fundamental software engineering principles, modular programming, and version control using Git and GitHub.

🔄 Software Development Life Cycle (SDLC)
1. Planning

The planning phase defines the purpose and scope of the project.

Objectives:

To design and implement a simple student record management system.

To apply SDLC concepts in a real project.

To practice version control using GitHub.

Scope:
The system focuses on basic student record management using a command-line interface.

Stakeholders:

Administrator (system user)

Students (data subjects)

Constraints:

Limited to a CLI-based application.

Uses in-memory data storage.

2. Requirements Analysis
Functional Requirements

The system shall allow users to add a new student.

The system shall display all student records.

The system shall update existing student information.

The system shall delete student records.

Non-Functional Requirements

The system shall be easy to use.

The system shall be modular and maintainable.

The system shall respond quickly to user input.

3. System Design

The system is designed using a modular architecture where each module has a specific responsibility.

Module Design

student.py: Defines the Student class and student attributes.

database.py: Handles storage and manipulation of student data.

main.py: Provides the command-line interface and controls program flow.

Folder Structure
sms_project/
├── README.md
├── .gitignore
├── student.py
├── database.py
└── main.py

4. Implementation

The system is implemented in Python using object-oriented programming concepts.

The Student class models student data.

A list is used to store student records.

CRUD operations are implemented through functions.

The main.py file contains the menu-driven interface.

All names and modules used in the design phase are consistent with the implementation phase.

5. Testing

The system was tested manually using different test cases.

Test Cases:

Adding a student with valid inputs.

Viewing student records when the list is empty and when it contains data.

Updating an existing student record.

Deleting a student record.

The system behaved as expected in all test cases.

6. Deployment

The project is deployed by pushing the source code to a GitHub repository using Git version control.

Steps:

Initialize Git repository

Commit project files

Push code to GitHub

The application is executed locally via the command line.

7. Maintenance

Future improvements may include:

File or database storage instead of in-memory storage

Graphical User Interface (GUI)

User authentication

Improved validation and error handling

🛠️ Technologies Used

Python

Git

GitHub

Command Line Interface (CLI)

▶️ How to Run the Project

Ensure Python is installed.

Clone the repository.

Navigate to the project directory.

Run the command:

python main.py

🎯 Purpose of the Project

This project is developed for academic purposes to demonstrate understanding of the Software Development Life Cycle (SDLC), basic system design, implementation, and GitHub version control as part of a Software Engineering course.

👤 Author

Karamat Ajiboye

Software Engineering Student
