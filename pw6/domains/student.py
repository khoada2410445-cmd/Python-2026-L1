import math
import numpy as np
from domains.person import Person

class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name, dob)
        self._marks = {}  # course_id -> mark
        self._gpa = 0.0

    def add_mark(self, course_id, mark):
        # Round down using math.floor
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
            np_marks = np.array(marks_list)
            np_credits = np.array(credits_list)
            self._gpa = np.sum(np_marks * np_credits) / np.sum(np_credits)
            
        return self._gpa

    def get_gpa(self):
        return self._gpa