# Blueprint 1: The Student Class
# This class is the blueprint for creating individual student objects.
class Student:
    # The __init__ method is the "constructor". It runs when you create a new Student.
    # It sets up the object's initial data (attributes).
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []  # A new student starts with an empty list of grades

    # This is a method (a function inside a class) to add a grade.
    def add_grade(self, grade):
        self.grades.append(grade)

    # This method calculates the student's average grade.
    def get_average_grade(self):
        if not self.grades:  # Avoid dividing by zero if there are no grades
            return 0
        return sum(self.grades) / len(self.grades)

    # This special method defines how the object should be represented as a string.
    # It's what gets called when you do `print(student_object)`. Very useful!
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Average Grade: {self.get_average_grade():.2f}"


# Blueprint 2: The School Class
# This class manages all the Student objects.
class School:
    def __init__(self, name):
        self.name = name
        self.students = []  # The school starts with an empty list of students

    # A method to add a student object to the school's list.
    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully.")

    ### THE FIX: The missing method is added here ###
    # A method to find a student by their ID.
    def find_student_by_id(self, student_id):
        # We loop through every student object in our list.
        for student in self.students:
            # We check if the student's ID matches the one we're looking for.
            if student.student_id == student_id:
                return student  # If we find it, we return the entire student object
        return None  # If the loop finishes and we haven't found a match, return None

    #################################################

    # A method to show all students. ANOTHER LOOP.
    def show_all_students(self):
        print(f"\n--- Students at {self.name} ---")
        if not self.students:
            print("No students in the system yet.")
        else:
            # We loop through every student and print their details.
            # The __str__ method in the Student class makes this print out nicely.
            for student in self.students:
                print(student)
        print("----------------------------\n")


# Main Program Logic (The User Menu)
# This is where we run the whole system.
def main():
    # Create one instance of a School.
    my_school = School("Python Coding Academy")

    # This is the main loop that keeps the program running.
    while True:
        print("\nStudent Management System Menu")
        print("1. Add Student")
        print("2. Find Student by ID")
        print("3. Show All Students")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            # Create a new Student object from our blueprint
            new_student = Student(name, student_id)
            # Use the school object's method to add the student
            my_school.add_student(new_student)

        elif choice == "2":
            student_id = input("Enter student ID to find: ")
            found_student = my_school.find_student_by_id(student_id)
            if found_student:
                print("\n--- Student Found ---")
                print(found_student)
                # Let's add a grade for fun
                try:
                    grade_input = input(
                        f"Enter a grade to add for {found_student.name} (or press Enter to skip): "
                    )
                    if grade_input:  # only try to convert if the user typed something
                        grade = float(grade_input)
                        found_student.add_grade(grade)
                        print("Grade added.")
                except ValueError:
                    print("Invalid grade format. No grade added.")
                print("---------------------")
            else:
                print("Student not found.")

        elif choice == "3":
            my_school.show_all_students()

        elif choice == "4":
            print("Goodbye!")
            break  # This exits the while loop

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# This line makes the `main()` function run when the script is executed.
if __name__ == "__main__":
    main()
