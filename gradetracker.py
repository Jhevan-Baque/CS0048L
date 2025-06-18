# Student Grade Tracker

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}  # subject: grade

    def add_grade(self, subject, grade):
        self.grades[subject] = float(grade)
        print(f"Added grade for {self.name} in {subject}: {grade}")

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def display_grades(self):
        if not self.grades:
            print("No grades available.")
        else:
            for subject, grade in self.grades.items():
                print(f"{subject}: {grade}")
            print(f"Average: {self.calculate_average():.2f}")

def is_valid_grade(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def AddStudent():
    print("\n[Add Student]")
    name = input("Enter Student Name: ")
    return Student(name)

def AddGrade(student):
    subject = input("Enter Subject Name: ")
    grade = input(f"Enter Grade for {subject}: ")
    while not is_valid_grade(grade):
        print("Invalid input. Please enter a valid number.")
        grade = input(f"Enter Grade for {subject}: ")
    student.add_grade(subject, grade)

def main():
    students = []
    while True:
        print("=" * 30)
        print("{:^30}".format("Student Grade Tracker"))
        print("=" * 30)
        print("1. Add Student")
        print("2. Add Grade to Student")
        print("3. View Student Grades")
        print("4. Calculate Average Grade")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student = AddStudent()
            students.append(student)
            print(f"\nStudent {student.name} added successfully!")

        elif choice == "2":
            if not students:
                print("\nNo students available. Please add a student first.")
                continue
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.name}")
            selected = input("Select student to add grade: ")
            if selected.isdigit() and 1 <= int(selected) <= len(students):
                AddGrade(students[int(selected)-1])
            else:
                print("Invalid selection.")

        elif choice == "3":
            if not students:
                print("\nNo students available.")
                continue
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.name}")
            selected = input("Select student to view grades: ")
            if selected.isdigit() and 1 <= int(selected) <= len(students):
                print(f"\nGrades for {students[int(selected)-1].name}:")
                students[int(selected)-1].display_grades()
            else:
                print("Invalid selection.")

        elif choice == "4":
            if not students:
                print("\nNo students available.")
                continue
            for i, student in enumerate(students, 1):
                print(f"{i}. {student.name}")
            selected = input("Select student to calculate average: ")
            if selected.isdigit() and 1 <= int(selected) <= len(students):
                avg = students[int(selected)-1].calculate_average()
                print(f"\nAverage grade for {students[int(selected)-1].name}: {avg:.2f}")
            else:
                print("Invalid selection.")

        elif choice == "5":
            print("Exit Program")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
