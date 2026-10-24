"""Find the largest, smallest, and average values in a list of numbers."""


def analyze_numbers(numbers):
    if not numbers:
        raise ValueError("Enter at least one number.")
    return {
        "largest": max(numbers),
        "smallest": min(numbers),
        "average": sum(numbers) / len(numbers),
    }


def run_number_analysis():
    print("\n--- Number Analysis ---")
    raw = input("Enter numbers separated by spaces or commas: ").strip()
    try:
        parts = raw.replace(",", " ").split()
        numbers = [float(part) for part in parts]
        result = analyze_numbers(numbers)
        print("Numbers  :", numbers)
        print("Largest  :", result["largest"])
        print("Smallest :", result["smallest"])
        print(f"Average  : {result['average']:.2f}")
    except ValueError as error:
        print(f"Invalid input: {error}")
