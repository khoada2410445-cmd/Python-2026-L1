class Person:
    def __init__(self, person_id, name, dob):
        self._id = person_id
        self._name = name
        self._dob = dob

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_dob(self):
        return self._dob


class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)
        self._marks = {}  # {course_id: mark}

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

    def get_marks(self):
        return self._marks


class Course:
    def __init__(self, course_id, name, credits=3):
        self._id = course_id
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits


class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self):
        num = int(input("Enter number of students: "))
        for i in range(num):
            print(f"\nStudent #{i+1}:")
            s_id = input("  ID: ")
            s_name = input("  Name: ")
            s_dob = input("  DoB (DD/MM/YYYY): ")
            self._students.append(Student(s_id, s_name, s_dob))

    def input_courses(self):
        num = int(input("Enter number of courses: "))
        for i in range(num):
            print(f"\nCourse #{i+1}:")
            c_id = input("  ID: ")
            c_name = input("  Name: ")
            self._courses.append(Course(c_id, c_name))

    def input_marks(self):
        if not self._courses or not self._students:
            print("Please input students and courses first!")
            return

        print("\nAvailable courses:")
        for c in self._courses:
            print(f"  - {c.get_id()}: {c.get_name()}")
        
        c_id = input("Select course ID to enter marks: ")
        course_exists = any(c.get_id() == c_id for c in self._courses)
        
        if not course_exists:
            print("Course not found!")
            return

        print(f"\nEntering marks for course {c_id}:")
        for s in self._students:
            mark = float(input(f"  Mark for {s.get_name()} ({s.get_id()}): "))
            s.add_mark(c_id, mark)

    def list_students(self):
        print("\n=== STUDENT LIST ===")
        print(f"{'ID':<10} | {'Name':<20} | {'DoB':<12}")
        print("-" * 48)
        for s in self._students:
            print(f"{s.get_id():<10} | {s.get_name():<20} | {s.get_dob():<12}")

    def list_courses(self):
        print("\n=== COURSE LIST ===")
        print(f"{'ID':<10} | {'Name':<20}")
        print("-" * 32)
        for c in self._courses:
            print(f"{c.get_id():<10} | {c.get_name():<20}")

    def show_marks(self):
        c_id = input("\nEnter course ID to view marks: ")
        print(f"\n=== MARKS FOR COURSE {c_id} ===")
        for s in self._students:
            marks = s.get_marks()
            if c_id in marks:
                print(f"{s.get_name()} ({s.get_id()}): {marks[c_id]}")


def main():
    system = StudentMarkManagement()
    while True:
        print("\n--- STUDENT MARK MANAGEMENT (PW2) ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            system.input_students()
        elif choice == '2':
            system.input_courses()
        elif choice == '3':
            system.input_marks()
        elif choice == '4':
            system.list_students()
        elif choice == '5':
            system.list_courses()
        elif choice == '6':
            system.show_marks()
        elif choice == '7':
            break


if __name__ == "__main__":
    main()