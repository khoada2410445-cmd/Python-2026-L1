import os
import zipfile
import curses
import input
import output
from domains.student import Student
from domains.course import Course

DATA_FILE = "students.dat"
TXT_FILES = ["students.txt", "courses.txt", "marks.txt"]

def load_data(students, courses):
    if os.path.exists(DATA_FILE):
        try:
            with zipfile.ZipFile(DATA_FILE, 'r') as zipf:
                zipf.extractall(".")
        except Exception:
            pass

    # Load students.txt
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    students.append(Student(parts[0], parts[1], parts[2]))

    # Load courses.txt
    if os.path.exists("courses.txt"):
        with open("courses.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    courses.append(Course(parts[0], parts[1], float(parts[2])))

    # Load marks.txt
    if os.path.exists("marks.txt"):
        with open("marks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    s_id, c_id, mark = parts[0], parts[1], float(parts[2])
                    for s in students:
                        if s.get_id() == s_id:
                            s.add_mark(c_id, mark)

def save_and_compress():
    with zipfile.ZipFile(DATA_FILE, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in TXT_FILES:
            if os.path.exists(file):
                zipf.write(file)
                os.remove(file)  # Delete text file after archiving

def main(stdscr):
    curses.curs_set(1)
    students = []
    courses = []

    # Load data from students.dat on startup
    load_data(students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr("=====================================\n")
        stdscr.addstr("  STUDENT MANAGEMENT SYSTEM (PW5)    \n")
        stdscr.addstr("=====================================\n")
        stdscr.addstr("1. Input Student Info\n")
        stdscr.addstr("2. Input Course Info\n")
        stdscr.addstr("3. Input Marks for Course\n")
        stdscr.addstr("4. Show Student List & Ranked GPA\n")
        stdscr.addstr("5. Exit & Compress Data\n")
        stdscr.addstr("-------------------------------------\n")
        stdscr.addstr("Enter choice [1-5]: ")
        
        curses.echo()
        choice = stdscr.getstr().decode('utf-8')
        
        if choice == '1':
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses)
        elif choice == '3':
            input.input_marks(stdscr, students, courses)
        elif choice == '4':
            output.display_students(stdscr, students, courses)
        elif choice == '5':
            save_and_compress()
            break

if __name__ == "__main__":
    curses.wrapper(main)