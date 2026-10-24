"""Student grade calculator using the grading scale in the internship report."""


def calculate_result(name, marks):
    """Return total, average, and grade for exactly three marks (0-100 each)."""
    if len(marks) != 3:
        raise ValueError("Enter marks for exactly three subjects.")
    if any(not isinstance(mark, (int, float)) or mark < 0 or mark > 100 for mark in marks):
        raise ValueError("Each mark must be between 0 and 100.")

    total = sum(marks)
    average = total / 3

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return {
        "name": name.strip(),
        "total": total,
        "average": average,
        "grade": grade,
    }


def run_grade_calculator():
    print("\n--- Student Grade Calculator ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Student name cannot be empty.")
        return

    marks = []
    for subject in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {subject} (0-100): "))
                if not 0 <= mark <= 100:
                    print("Marks must be between 0 and 100.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a valid number.")

    result = calculate_result(name, marks)
    print("\nStudent Name :", result["name"])
    print("Total Marks  :", result["total"])
    print(f"Average      : {result['average']:.2f}")
    print("Grade        :", result["grade"])
