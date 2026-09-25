import curses

def sort_students_by_gpa(students, courses):
    for s in students:
        s.calculate_gpa(courses)
    students.sort(key=lambda s: s.get_gpa(), reverse=True)

def display_students(stdscr, students, courses):
    stdscr.clear()
    if not students:
        stdscr.addstr("No student data available. Press any key...")
        stdscr.getch()
        return

    sort_students_by_gpa(students, courses)
    stdscr.addstr("=== STUDENT LIST (SORTED BY GPA DESCENDING) ===\n\n")
    stdscr.addstr(f"{'ID':<12} | {'Name':<25} | {'DoB':<12} | {'GPA':<5}\n")
    stdscr.addstr("-" * 60 + "\n")
    
    for s in students:
        stdscr.addstr(f"{s.get_id():<12} | {s.get_name():<25} | {s.get_dob():<12} | {s.get_gpa():.2f}\n")
    
    stdscr.addstr("\nPress any key to return to menu...")
    stdscr.getch()