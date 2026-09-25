import curses
import input
import output

def main(stdscr):
    curses.curs_set(1)
    students = []
    courses = []

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
            input.input_students(stdscr, students)
        elif choice == '2':
            input.input_courses(stdscr, courses)
        elif choice == '3':
            input.input_marks(stdscr, students, courses)
        elif choice == '4':
            output.display_students(stdscr, students, courses)
        elif choice == '5':
            break

if __name__ == "__main__":
    curses.wrapper(main)