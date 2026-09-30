import csv

FILE_NAME = "students.csv"


def load_students():
    students = []

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            row["Maths"] = float(row["Maths"])
            row["Science"] = float(row["Science"])
            row["English"] = float(row["English"])
            row["Attendance"] = float(row["Attendance"])
            students.append(row)

    return students


def calculate_result(student):
    total = student["Maths"] + student["Science"] + student["English"]
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    elif percentage >= 40:
        grade = "E"
    else:
        grade = "F"

    if (
        student["Maths"] >= 40
        and student["Science"] >= 40
        and student["English"] >= 40
    ):
        result = "Pass"
    else:
        result = "Fail"

    return total, percentage, grade, result


def view_students(students):
    for student in students:
        total, percentage, grade, result = calculate_result(student)

        print(
            student["Student ID"],
            student["Name"],
            "Percentage:", round(percentage, 2),
            "Grade:", grade,
            "Result:", result
        )


def subject_averages(students):
    print("\nSubject Averages")

    for subject in ["Maths", "Science", "English"]:
        total = sum(student[subject] for student in students)
        average = total / len(students)

        print(subject, ":", round(average, 2))


def top_students(students):
    ranked = sorted(
        students,
        key=lambda student: calculate_result(student)[1],
        reverse=True
    )

    print("\nTop Students")

    for student in ranked[:5]:
        percentage = calculate_result(student)[1]
        print(student["Name"], "-", round(percentage, 2), "%")


def find_student(students):
    student_id = input("Enter Student ID: ")

    for student in students:

        if student["Student ID"].lower() == student_id.lower():

            total, percentage, grade, result = calculate_result(student)

            print("\nStudent Details")
            print("Name:", student["Name"])
            print("Class:", student["Class"])
            print("Total:", total)
            print("Percentage:", round(percentage, 2))
            print("Grade:", grade)
            print("Result:", result)
            print("Attendance:", student["Attendance"])

            return

    print("Student not found.")


def main():

    students = load_students()

    while True:

        print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
        print("1. View all students")
        print("2. Subject averages")
        print("3. Top students")
        print("4. Find student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students(students)

        elif choice == "2":
            subject_averages(students)

        elif choice == "3":
            top_students(students)

        elif choice == "4":
            find_student(students)

        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

