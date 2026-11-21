
import os

FILE_NAME = "student.txt"


# Function to load student records from file

def load_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        for line in lines:
            if line.startswith("|") and "Roll Number" not in line:
                parts = line.strip().strip("|").split("|")

                if len(parts) == 3:
                    roll = parts[0].strip()
                    name = parts[1].strip()
                    marks = float(parts[2].strip())

                    students.append({
                        "roll": roll,
                        "name": name,
                        "marks": marks
                    })

    return students



# Function to save student records to file

def save_students(students):
    with open(FILE_NAME, "w") as file:

        file.write("=" * 59 + "\n")
        file.write("             STUDENT RECORDS DATABASE\n")
        file.write("=" * 59 + "\n\n")

        file.write("+-------------+----------------------+----------+\n")
        file.write("| Roll Number | Name                 | Marks    |\n")
        file.write("+-------------+----------------------+----------+\n")

        for student in students:
            file.write(
                f"| {student['roll']:<11} "
                f"| {student['name']:<20} "
                f"| {student['marks']:<8} |\n"
            )

        file.write("+-------------+----------------------+----------+\n")



# Function to add a student
def add_student(students):
    try:
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        marks = float(input("Enter Marks: "))

        if not roll or not name:
            print("Roll number and name cannot be empty!")
            return

        if any(s["roll"] == roll for s in students):
            print("Roll number already exists!")
            return

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        student = {
            "roll": roll,
            "name": name,
            "marks": marks
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError:
        print("Invalid marks! Please enter a number.")


# Function to view all students
def view_students(students):
    if not students:
        print("No student records found!")
        return

    print("\n------ STUDENT RECORDS ------")

    for student in students:
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("-----------------------------")


# Function to search for a student
def search_student(students):
    roll = input("Enter Roll Number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            return

    print("Student not found!")


# Function to calculate average marks
def calculate_average(students):
    if not students:
        print("No student records available!")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks:", round(average, 2))


# Main program
students = load_students()

while True:

    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Calculate Average Marks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        calculate_average(students)

    elif choice == "5":
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please enter 1 to 5.")
