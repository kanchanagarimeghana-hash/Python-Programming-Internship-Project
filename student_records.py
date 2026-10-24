"""In-memory student record management using a Python list."""


def add_student(students, name):
    name = name.strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    if any(existing.casefold() == name.casefold() for existing in students):
        raise ValueError("That student is already in the list.")
    students.append(name)
    return students


def search_student(students, name):
    query = name.strip().casefold()
    return next((student for student in students if student.casefold() == query), None)


def remove_student(students, name):
    found = search_student(students, name)
    if found is None:
        return False
    students.remove(found)
    return True


def run_student_records():
    students = []
    while True:
        print("\n--- Student Record Management ---")
        print("1. Add student")
        print("2. Display students")
        print("3. Search student")
        print("4. Remove student")
        print("5. Return to main menu")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter student name: ")
            try:
                add_student(students, name)
                print("Student added successfully.")
            except ValueError as error:
                print(error)
        elif choice == "2":
            if students:
                print("\nStudent Records:")
                for index, student in enumerate(students, start=1):
                    print(f"{index}. {student}")
            else:
                print("No student records yet.")
        elif choice == "3":
            name = input("Enter name to search: ")
            found = search_student(students, name)
            print(f"Found: {found}" if found else "Student not found.")
        elif choice == "4":
            name = input("Enter name to remove: ")
            if remove_student(students, name):
                print("Student removed successfully.")
            else:
                print("Student not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
