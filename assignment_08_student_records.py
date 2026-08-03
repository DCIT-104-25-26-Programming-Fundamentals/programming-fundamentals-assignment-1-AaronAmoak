# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# - Store all student records in a list of dictionaries.
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#
# =============================================================================


def compute_average(student):
    scores = student["scores"]
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def add_student(students):
    name = input("Student name: ")
    student_id = int(input("Student ID: "))
    num_scores = int(input("How many scores? "))

    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')


def display_all_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
    print("-" * 50)
    for student in students:
        scores_str = ", ".join(str(int(s)) if s == int(s) else str(s) for s in student["scores"])
        avg = compute_average(student)
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{avg:<10.2f}")
    print("-" * 50)


def calculate_average_for_id(students):
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            avg = compute_average(student)
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print("Error: Student ID not found.")


def print_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []
    running = True

    while running:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_average_for_id(students)
        elif choice == "4":
            print("Goodbye!")
            running = False
        else:
            print("Error: Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
