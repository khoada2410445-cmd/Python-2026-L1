import math
import numpy as np
import curses

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
        self._marks = {}  # course_id -> mark
        self._gpa = 0.0

    def add_mark(self, course_id, mark):
        # Round down mark to 1 decimal place using math.floor
        self._marks[course_id] = math.floor(mark * 10) / 10.0

    def get_marks(self):
        return self._marks

    def calculate_gpa(self, courses):
        marks_list = []
        credits_list = []
        
        course_credits_map = {c.get_id(): c.get_credits() for c in courses}

        for course_id, mark in self._marks.items():
            if course_id in course_credits_map:
                marks_list.append(mark)
                credits_list.append(course_credits_map[course_id])

        if not credits_list or sum(credits_list) == 0:
            self._gpa = 0.0
        else:
            # Weighted average using numpy arrays
            np_marks = np.array(marks_list)
            np_credits = np.array(credits_list)
            self._gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            
        return self._gpa

    def get_gpa(self):
        return self._gpa


class Course:
    def __init__(self, course_id, name, credits):
        self._id = course_id
        self._name = name
        self._credits = credits

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_credits(self):
        return self._credits


class StudentManagementApp:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self, stdscr):
        stdscr.clear()
        stdscr.addstr("=== INPUT STUDENTS ===\n\n")
        stdscr.addstr("Enter number of students: ")
        curses.echo()
        
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for i in range(num):
                stdscr.addstr(f"\nStudent #{i + 1}:\n")
                stdscr.addstr("  ID: ")
                s_id = stdscr.getstr().decode('utf-8')
                stdscr.addstr("  Name: ")
                s_name = stdscr.getstr().decode('utf-8')
                stdscr.addstr("  DoB (DD/MM/YYYY): ")
                s_dob = stdscr.getstr().decode('utf-8')
                
                self.students.append(Student(s_id, s_name, s_dob))
            stdscr.addstr("\nStudents added successfully! Press any key...")
        except ValueError:
            stdscr.addstr("\nInvalid input number! Press any key...")
            
        stdscr.getch()

    def input_courses(self, stdscr):
        stdscr.clear()
        stdscr.addstr("=== INPUT COURSES ===\n\n")
        stdscr.addstr("Enter number of courses: ")
        curses.echo()
        
        try:
            num = int(stdscr.getstr().decode('utf-8'))
            for i in range(num):
                stdscr.addstr(f"\nCourse #{i + 1}:\n")
                stdscr.addstr("  ID: ")
                c_id = stdscr.getstr().decode('utf-8')
                stdscr.addstr("  Name: ")
                c_name = stdscr.getstr().decode('utf-8')
                stdscr.addstr("  Credits: ")
                c_credits = float(stdscr.getstr().decode('utf-8'))
                
                self.courses.append(Course(c_id, c_name, c_credits))
            stdscr.addstr("\nCourses added successfully! Press any key...")
        except ValueError:
            stdscr.addstr("\nInvalid input format! Press any key...")
            
        stdscr.getch()

    def input_marks(self, stdscr):
        stdscr.clear()
        if not self.courses or not self.students:
            stdscr.addstr("Please add students and courses first! Press any key...")
            stdscr.getch()
            return

        stdscr.addstr("=== INPUT MARKS ===\n\n")
        stdscr.addstr("Available Courses:\n")
        for c in self.courses:
            stdscr.addstr(f"  - {c.get_id()}: {c.get_name()}\n")
            
        stdscr.addstr("\nSelect Course ID: ")
        curses.echo()
        c_id = stdscr.getstr().decode('utf-8')

        course_found = any(c.get_id() == c_id for c in self.courses)
        if not course_found:
            stdscr.addstr("\nCourse ID not found! Press any key...")
            stdscr.getch()
            return

        stdscr.addstr(f"\nEnter marks for Course {c_id}:\n")
        for student in self.students:
            try:
                stdscr.addstr(f"  Mark for {student.get_name()} ({student.get_id()}): ")
                mark = float(stdscr.getstr().decode('utf-8'))
                student.add_mark(c_id, mark)
            except ValueError:
                stdscr.addstr("  Invalid mark, setting default to 0.0\n")
                student.add_mark(c_id, 0.0)

        stdscr.addstr("\nMarks saved! Press any key...")
        stdscr.getch()

    def sort_students_by_gpa(self):
        for s in self.students:
            s.calculate_gpa(self.courses)
        # Sort in descending order by GPA
        self.students.sort(key=lambda s: s.get_gpa(), reverse=True)

    def display_students(self, stdscr):
        stdscr.clear()
        if not self.students:
            stdscr.addstr("No student data available. Press any key...")
            stdscr.getch()
            return

        self.sort_students_by_gpa()
        stdscr.addstr("=== STUDENT LIST (SORTED BY GPA DESCENDING) ===\n\n")
        stdscr.addstr(f"{'ID':<12} | {'Name':<25} | {'DoB':<12} | {'GPA':<5}\n")
        stdscr.addstr("-" * 60 + "\n")
        
        for s in self.students:
            stdscr.addstr(f"{s.get_id():<12} | {s.get_name():<25} | {s.get_dob():<12} | {s.get_gpa():.2f}\n")
        
        stdscr.addstr("\nPress any key to return to menu...")
        stdscr.getch()

def main(stdscr):
    curses.curs_set(1)  # Show cursor
    app = StudentManagementApp()

    while True:
        stdscr.clear()
        stdscr.addstr("=====================================\n")
        stdscr.addstr("      STUDENT MANAGEMENT SYSTEM      \n")
        stdscr.addstr("=====================================\n")
        stdscr.addstr("1. Input Student Info\n")
        stdscr.addstr("2. Input Course Info\n")
        stdscr.addstr("3. Input Marks for Course\n")
        stdscr.addstr("4. Show Student List & Ranked GPA\n")
        stdscr.addstr("5. Exit\n")
        stdscr.addstr("-------------------------------------\n")
        stdscr.addstr("Enter choice [1-5]: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        
        if choice == '1':
            app.input_students(stdscr)
        elif choice == '2':
            app.input_courses(stdscr)
        elif choice == '3':
            app.input_marks(stdscr)
        elif choice == '4':
            app.display_students(stdscr)
        elif choice == '5':
            break

if __name__ == "__main__":
    curses.wrapper(main)