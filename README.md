# Python Programming Internship Mini Project

A menu-driven Python project based on the three practical tasks documented in the Python Programming internship report:

1. **Student Grade Calculator** — accepts a student's name and marks for three subjects, then calculates total, average, and grade.
2. **Student Record Management** — adds, displays, searches, and removes student names using a Python list.
3. **Number Analysis** — calculates the largest, smallest, and average values in a list of numbers.

## Technology
- Python 3
- Built-in Python modules only (no external packages required)

## Grade scale
The Student Grade Calculator follows the report's scale:

| Average marks | Grade |
| --- | --- |
| 90 and above | A |
| 75 to below 90 | B |
| 60 to below 75 | C |
| 50 to below 60 | D |
| Below 50 | F |

Each subject mark must be between 0 and 100.

## Run the project
1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python main.py
```

On some Windows systems, use `py main.py` instead.

## Run tests
Run the included unit tests from the project folder:

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
Python_Programming_Internship_Project/
├── main.py
├── grade_calculator.py
├── student_records.py
├── number_analysis.py
├── tests/
│   └── test_project.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Notes
- Student records are kept in memory while the Student Record Management menu is open. They are not saved after the program exits, matching the list-based task described in the report.
- The project uses functions, conditionals, loops, lists, input validation, and basic exception handling.
