import curses
from domains.student import Student
from domains.course import Course

def input_students(stdscr, students):
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
            
            students.append(Student(s_id, s_name, s_dob))
        stdscr.addstr("\nStudents added successfully! Press any key...")
    except ValueError:
        stdscr.addstr("\nInvalid number! Press any key...")
        
    stdscr.getch()

def input_courses(stdscr, courses):
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
            
            courses.append(Course(c_id, c_name, c_credits))
        stdscr.addstr("\nCourses added successfully! Press any key...")
    except ValueError:
        stdscr.addstr("\nInvalid input format! Press any key...")
        
    stdscr.getch()

def input_marks(stdscr, students, courses):
    stdscr.clear()
    if not courses or not students:
        stdscr.addstr("Please add students and courses first! Press any key...")
        stdscr.getch()
        return

    stdscr.addstr("=== INPUT MARKS ===\n\n")
    stdscr.addstr("Available Courses:\n")
    for c in courses:
        stdscr.addstr(f"  - {c.get_id()}: {c.get_name()}\n")

    stdscr.addstr("\nSelect Course ID: ")
    curses.echo()
    c_id = stdscr.getstr().decode('utf-8')

    course_found = any(c.get_id() == c_id for c in courses)
    if not course_found:
        stdscr.addstr("\nCourse ID not found! Press any key...")
        stdscr.getch()
        return

    stdscr.addstr(f"\nEnter marks for Course {c_id}:\n")
    for student in students:
        try:
            stdscr.addstr(f"  Mark for {student.get_name()} ({student.get_id()}): ")
            mark = float(stdscr.getstr().decode('utf-8'))
            student.add_mark(c_id, mark)
        except ValueError:
            stdscr.addstr("  Invalid mark, setting default to 0.0\n")
            student.add_mark(c_id, 0.0)

    stdscr.addstr("\nMarks saved! Press any key...")
    stdscr.getch()