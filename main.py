"""Menu-driven project combining the three Python internship tasks."""
from grade_calculator import run_grade_calculator
from student_records import run_student_records
from number_analysis import run_number_analysis


def main():
    while True:
        print("\n" + "=" * 48)
        print("       PYTHON PROGRAMMING MINI PROJECT")
        print("=" * 48)
        print("1. Student Grade Calculator")
        print("2. Student Record Management")
        print("3. Number Analysis")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            run_grade_calculator()
        elif choice == "2":
            run_student_records()
        elif choice == "3":
            run_number_analysis()
        elif choice == "4":
            print("Thank you for using the project!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
