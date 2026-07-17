class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


def menu():
    print("\n--- STUDENT MANAGER ---")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Remove student")
    print("5. Exit")


def add_student():
    name = input("Enter student name: ")

    if not name:
        print("Student name cannot be empty")
        return

    try:
        age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid age")
        return

    course = input("Enter course: ")

    if not course:
        print("Course cannot be empty")
        return

    student = Student(name, age, course)

    students.append(student)

    print("Student added successfully")


def view_students():
    if not students:
        print("No students found")
        return

    print("\n--- STUDENTS ---")

    for student in students:
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Course: {student.course}")
        print("--------------------")


def search_student():
    if not students:
        print("No students found")
        return
    
    name= input("enter student name to search")

    for student in students:
        if student.name.lower()==name.lower():
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Course: {student.course}")
            return
    
    print("student not found")


def remove_student():
    if not students:
        print("No students found")
        return
    
    name=input("enter student name to remove")

    for student in students:
        if student.name.lower()==name.lower():
            students.remove(student)
            print("student removed")
            return
    
    print("student not found")


students = []


while True:
    menu()
    option = input("Choose an option: ")

    if option == "1":
        add_student()

    elif option == "2":
        view_students()

    elif option == "3":
        search_student()

    elif option == "4":
        remove_student()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")
