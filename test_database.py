import pytest
from student import Student
import database

@pytest.fixture(autouse=True)
def clear_students():
    # Ensure tests are isolated by clearing the in-memory store before and after each test
    database.students.clear()
    yield
    database.students.clear()

def test_add_and_view_students():
    s = Student("1", "Alice", 20, "A")
    database.add_student(s)
    assert database.view_students() == [s]

def test_find_student():
    s1 = Student("1", "Alice", 20, "A")
    s2 = Student("2", "Bob", 21, "B")
    database.add_student(s1)
    database.add_student(s2)
    assert database.find_student("1") == [s1]
    assert database.find_student("2") == [s2]
    assert database.find_student("3") == []

def test_update_student_success():
    s = Student("1", "Alice", 20, "A")
    database.add_student(s)
    updated = database.update_student("1", "Alicia", 21, "A1")
    assert updated is True
    assert s.name == "Alicia"
    assert s.age == 21
    assert s.class_name == "A1"

def test_update_student_failure():
    updated = database.update_student("42", "Nobody", 0, "X")
    assert updated is False

def test_delete_student():
    s1 = Student("1", "Alice", 20, "A")
    s2 = Student("2", "Bob", 21, "B")
    database.add_student(s1)
    database.add_student(s2)
    database.delete_student("1")
    assert database.find_student("1") == []
    assert database.view_students() == [s2]

def test_delete_nonexistent_does_not_raise():
    s = Student("1", "Alice", 20, "A")
    database.add_student(s)
    database.delete_student("99")  # no error expected
    assert database.view_students() == [s]
