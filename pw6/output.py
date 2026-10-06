import curses
import pandas as pd
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
    import pandas as pd

def export_to_csv(students, courses):
    """Export student, course, and mark data to CSV files"""
    # 1. Export students.csv
    student_data = [{"id": s.get_id(), "name": s.get_name(), "dob": s.get_dob()} for s in students]
    df_students = pd.DataFrame(student_data)
    df_students.to_csv("pw6/students.csv", index=False)

    # 2. Export courses.csv
    course_data = [{"id": c.get_id(), "name": c.get_name(), "credits": c.get_credits()} for c in courses]
    df_courses = pd.DataFrame(course_data)
    df_courses.to_csv("pw6/courses.csv", index=False)

    # 3. Export marks.csv
    mark_data = []
    for s in students:
        for course_id, mark in s.get_marks().items():
            mark_data.append({"student_id": s.get_id(), "course_id": course_id, "mark": mark})
    df_marks = pd.DataFrame(mark_data)
    df_marks.to_csv("pw6/marks.csv", index=False)


def query_student_by_name(stdscr):
    """Query student information using Pandas DataFrame"""
    stdscr.clear()
    stdscr.addstr("=== EXTRA: PANDAS QUERY FUNCTION ===\n\n")
    
    try:
        # Load CSV files into Pandas DataFrames
        df_students = pd.read_csv("pw6/students.csv")
        
        stdscr.addstr("Enter student name condition (e.g. Mr. Volunteers or partial name): ")
        stdscr.refresh()
        
        curses.echo()
        search_name = stdscr.getstr().decode('utf-8').strip()
        curses.noecho()
        
        # Run query on Pandas DataFrame
        result = df_students[df_students['name'].str.contains(search_name, case=False, na=False)]
        
        stdscr.addstr("\n--- Query Results (Pandas DataFrame) ---\n")
        if result.empty:
            stdscr.addstr("No matching student found!\n")
        else:
            stdscr.addstr(result.to_string(index=False) + "\n")
            
    except FileNotFoundError:
        stdscr.addstr("Error: CSV files not found. Please export CSV data first (Option 6)!\n")
    except Exception as e:
        stdscr.addstr(f"Error executing query: {e}\n")
        
    stdscr.addstr("\nPress any key to return to main menu...")
    stdscr.refresh()
    stdscr.getch()