import curses
import sys
from input import input_students, input_courses, input_marks
from output import save_data_background, load_data

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
        self.save_thread = None

    def load_initial_data(self):
        saved_data = load_data()
        if saved_data and isinstance(saved_data, dict):
            self.students = saved_data.get("students", [])
            self.courses = saved_data.get("courses", [])
            self.marks = saved_data.get("marks", [])

    def trigger_background_save(self):
        data_to_save = {
            "students": self.students,
            "courses": self.courses,
            "marks": self.marks
        }
        self.save_thread = save_data_background(data_to_save)

    def main_menu(self, stdscr):
        curses.curs_set(0)
        
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "=== STUDENT MANAGEMENT SYSTEM (PW8 - MULTITHREADED) ===")
            stdscr.addstr(2, 0, "1. Input Students")
            stdscr.addstr(3, 0, "2. Input Courses")
            stdscr.addstr(4, 0, "3. Input Marks")
            stdscr.addstr(5, 0, "4. Save Data (Background Thread)")
            stdscr.addstr(6, 0, "5. Exit")
            stdscr.addstr(8, 0, "Select an option [1-5]: ")
            stdscr.refresh()

            key = stdscr.getkey()

            if key == '1':
                try:
                    self.students = input_students(stdscr, self.students)
                except TypeError:
                    self.students = input_students(stdscr)
            elif key == '2':
                try:
                    self.courses = input_courses(stdscr, self.courses)
                except TypeError:
                    self.courses = input_courses(stdscr)
            elif key == '3':
                try:
                    self.marks = input_marks(stdscr, self.students, self.courses)
                except TypeError:
                    self.marks = input_marks(stdscr)
            elif key == '4':
                self.trigger_background_save()
                stdscr.addstr(10, 0, "Save initiated in background thread! Press any key...")
                stdscr.refresh()
                stdscr.getch()
            elif key == '5':
                self.trigger_background_save()
                if self.save_thread and self.save_thread.is_alive():
                    self.save_thread.join()
                break

    def run(self):
        self.load_initial_data()
        curses.wrapper(self.main_menu)

if __name__ == "__main__":
    app = StudentManagementSystem()
    app.run()