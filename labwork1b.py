# Global data structures
students = []  # List of tuples: (student_id, student_name, dob)
courses = []   # List of tuples: (course_id, course_name)
marks = {}     # Dict: (course_id, student_id) -> mark

# --- Input Functions ---

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_info():
    num_students = input_number_of_students()
    for i in range(num_students):
        print(f"\n--- Student {i + 1} ---")
        student_id = input("  Enter Student ID: ").strip()
        student_name = input("  Enter Student Name: ").strip()
        dob = input("  Enter DoB (DD/MM/YYYY): ").strip()
        students.append((student_id, student_name, dob))

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    num_courses = input_number_of_courses()
    for i in range(num_courses):
        print(f"\n--- Course {i + 1} ---")
        course_id = input("  Enter Course ID: ").strip()
        course_name = input("  Enter Course Name: ").strip()
        courses.append((course_id, course_name))

def input_marks_for_course():
    if not courses:
        print("\nNo courses available. Please add courses first!")
        return
    if not students:
        print("\nNo students available. Please add students first!")
        return

    print("\n=== SELECT A COURSE TO INPUT MARKS ===")
    list_courses()
    selected_course_id = input("Enter Course ID: ").strip()

    # Check if course exists
    course_exists = any(c[0] == selected_course_id for c in courses)
    if not course_exists:
        print("Course ID not found!")
        return

    print(f"\nEntering marks for Course: {selected_course_id}")
    for student in students:
        student_id, student_name, _ = student
        mark = float(input(f"  Enter mark for {student_name} (ID: {student_id}): "))
        marks[(selected_course_id, student_id)] = mark

# --- Listing Functions ---

def list_courses():
    print("\n=== COURSE LIST ===")
    if not courses:
        print("No courses added yet.")
        return
    print(f"{'Course ID':<12} | {'Course Name':<25}")
    print("-" * 40)
    for course_id, course_name in courses:
        print(f"{course_id:<12} | {course_name:<25}")

def list_students():
    print("\n=== STUDENT LIST ===")
    if not students:
        print("No students added yet.")
        return
    print(f"{'Student ID':<12} | {'Student Name':<25} | {'DoB':<12}")
    print("-" * 55)
    for student_id, student_name, dob in students:
        print(f"{student_id:<12} | {student_name:<25} | {dob:<12}")

def show_student_marks():
    if not courses:
        print("\nNo courses available.")
        return

    selected_course_id = input("\nEnter Course ID to view marks: ").strip()
    
    # Check if course exists
    course_exists = any(c[0] == selected_course_id for c in courses)
    if not course_exists:
        print("Course ID not found!")
        return

    print(f"\n=== MARKS FOR COURSE: {selected_course_id} ===")
    print(f"{'Student ID':<12} | {'Student Name':<25} | {'Mark':<5}")
    print("-" * 50)
    
    for student in students:
        student_id, student_name, _ = student
        key = (selected_course_id, student_id)
        mark = marks.get(key, "N/A")
        print(f"{student_id:<12} | {student_name:<25} | {mark:<5}")

# --- Main Program ---

def main():
    while True:
        print("\n==================================")
        print("   STUDENT MARK MANAGEMENT SYSTEM  ")
        print("==================================")
        print("1. Input Student Information")
        print("2. Input Course Information")
        print("3. Select Course & Input Marks")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Marks for a Course")
        print("7. Exit")
        print("----------------------------------")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            input_student_info()
        elif choice == '2':
            input_course_info()
        elif choice == '3':
            input_marks_for_course()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            list_students()
        elif choice == '6':
            show_student_marks()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option! Please choose between 1 and 7.")

if __name__ == "__main__":
    main()