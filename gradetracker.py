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


class GradeTracker:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)
        return student

    def get_student_by_index(self, index):
        if 0 <= index < len(self.students):
            return self.students[index]
        return None

    def display_all_students(self):
        for i, student in enumerate(self.students, 1):
            print(f"{i}. {student.name}")

    def has_students(self):
        return len(self.students) > 0


def is_valid_grade(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    tracker = GradeTracker()

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
            name = input("Enter Student Name: ")
            tracker.add_student(name)
            print(f"Student '{name}' added successfully!")

        elif choice == "2":
            if not tracker.has_students():
                print("No students available. Add a student first.")
                continue
            print("\n[Select Student]")
            tracker.display_all_students()
            selected = input("Enter number: ")
            if selected.isdigit():
                index = int(selected) - 1
                student = tracker.get_student_by_index(index)
                if student:
                    subject = input("Enter Subject: ")
                    grade = input("Enter Grade: ")
                    while not is_valid_grade(grade):
                        print("Invalid input. Enter a valid number.")
                        grade = input("Enter Grade: ")
                    student.add_grade(subject, grade)
                else:
                    print("Invalid selection.")
            else:
                print("Invalid input.")

        elif choice == "3":
            if not tracker.has_students():
                print("No students available.")
                continue
            print("\n[Select Student]")
            tracker.display_all_students()
            selected = input("Enter number: ")
            if selected.isdigit():
                index = int(selected) - 1
                student = tracker.get_student_by_index(index)
                if student:
                    print(f"\nGrades for {student.name}:")
                    student.display_grades()
                else:
                    print("Invalid selection.")
            else:
                print("Invalid input.")

        elif choice == "4":
            if not tracker.has_students():
                print("No students available.")
                continue
            print("\n[Select Student]")
            tracker.display_all_students()
            selected = input("Enter number: ")
            if selected.isdigit():
                index = int(selected) - 1
                student = tracker.get_student_by_index(index)
                if student:
                    avg = student.calculate_average()
                    print(f"\nAverage grade for {student.name}: {avg:.2f}")
                else:
                    print("Invalid selection.")
            else:
                print("Invalid input.")

        elif choice == "5":
            print("Exit Program")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
