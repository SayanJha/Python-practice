class Student:
    """A simple attempt to model a student gradebook.""" # This is a docstring

    def __init__(self, first_name, middle_name, last_name, marks):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.marks = marks

    def full_name(self):
        if self.middle_name:
            return f"{self.first_name} {self.middle_name} {self.last_name}".title()
        else:
            return f"{self.first_name} {self.last_name}".title()

    def calculate_display_avg(self):
        total = sum(self.marks)
        average = round(total / len(self.marks), 2)

        print(f"\nHello, {self.full_name()}!")
        print(f"You obtained {total} marks in total.")
        print(f"Your average is {average}.")

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 50:
            grade = "D"
        elif average >= 40:
            grade = "E"
        else:
            grade = "F (Fail)"

        print(f"Your grade is {grade}\n")
        return grade


def student_info():
    print("\nEnter student details:")
    first_name = input("First name: ").strip()
    middle_name = input("Middle name (or press Enter to skip): ").strip()
    last_name = input("Last name: ").strip()

    while True:
        try:
            num_subjects = int(input("How many subjects do you want to enter marks for? (Max = 10): "))
            if num_subjects <= 0 or num_subjects > 10:
                print("Please enter a valid number between 1 and 10: ")
                continue
            break
        except ValueError:
            print("Please enter a valid number between 1 and 10.")

    marks = []
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i}: "))
                if mark < 0 or mark > 100:
                    print("Enter marks between 0 and 100.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("Please enter a valid number.")

    return Student(first_name, middle_name, last_name, marks)

def main():
    print("Welcome to the Student GradeBook!")

    while True:
        student = student_info()
        student.calculate_display_avg()

        repeat = input("Do you want to enter another student's result? (Enter 'q' to quit): ").strip().lower()
        if repeat == "q":                                                               # Function chaining
            print("\nThank you for using Student GradeBook. Goodbye!")
            break

if __name__ == "__main__":
    main()
