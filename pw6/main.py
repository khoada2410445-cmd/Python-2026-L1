import os
import zipfile
import pickle
import curses
import input
import output

DATA_FILE = "pw6/students.dat"

def save_data(students, courses):
    """Serialize students and courses data using pickle and compress into students.dat"""
    # Dump objects into temporary pickle files
    with open("pw6/students.pkl", "wb") as f:
        pickle.dump(students, f)
    with open("pw6/courses.pkl", "wb") as f:
        pickle.dump(courses, f)
        
    # Compress pickle files into students.dat archive
    with zipfile.ZipFile(DATA_FILE, 'w') as zipf:
        zipf.write("pw6/students.pkl", "students.pkl")
        zipf.write("pw6/courses.pkl", "courses.pkl")
            
    # Clean up temporary pickle files
    if os.path.exists("pw6/students.pkl"):
        os.remove("pw6/students.pkl")
    if os.path.exists("pw6/courses.pkl"):
        os.remove("pw6/courses.pkl")


def load_data(students, courses):
    """Decompress students.dat and load serialized objects using pickle"""
    if os.path.exists(DATA_FILE):
        try:
            with zipfile.ZipFile(DATA_FILE, 'r') as zipf:
                zipf.extractall("pw6")
                
            if os.path.exists("pw6/students.pkl"):
                with open("pw6/students.pkl", "rb") as f:
                    loaded_students = pickle.load(f)
                    students.extend(loaded_students)
                os.remove("pw6/students.pkl")
                
            if os.path.exists("pw6/courses.pkl"):
                with open("pw6/courses.pkl", "rb") as f:
                    loaded_courses = pickle.load(f)
                    courses.extend(loaded_courses)
                os.remove("pw6/courses.pkl")
        except Exception as e:
            pass


def main(stdscr):
    students = []
    courses = []

    # Decompress and unpickle data if available
    load_data(students, courses)

    while True:
        stdscr.clear()
        stdscr.addstr("===================================\n")
        stdscr.addstr("   STUDENT MANAGEMENT SYSTEM (PW6) \n")
        stdscr.addstr("===================================\n")
        stdscr.addstr("1. Input Student Info\n")
        stdscr.addstr("2. Input Course Info\n")
        stdscr.addstr("3. Input Marks for Course\n")
        stdscr.addstr("4. Show Student List & Ranked GPA\n")
        stdscr.addstr("5. Exit & Compress Pickled Data\n")
        stdscr.addstr("===================================\n")
        stdscr.addstr("Enter choice [1-5]: ")
        stdscr.refresh()

        curses.echo()
        choice = stdscr.getstr().decode('utf-8').strip()
        curses.noecho()

        if choice == '1':
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses)
        elif choice == '3':
            input.input_marks(stdscr, students, courses)
        elif choice == '4':
            output.display_gpa(stdscr, students)
        elif choice == '5':
            save_data(students, courses)
            break


if __name__ == "__main__":
    curses.wrapper(main)