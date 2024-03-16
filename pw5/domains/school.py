from domains.student import Student
from domains.course import Course
import numpy as np

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            name = input("Enter student's name: ")
            dob = input("Enter student DoB: ")
            student_id = input("Enter student ID: ")
            student = Student(name, dob, student_id)
            self.students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            name = input("Enter course name: ")
            course = Course(name)
            self.courses.append(course)

    def input_marks(self):
        student_id = input("Enter the student ID: ")
        for student in self.students:
            if student.student_id == student_id:
                subject = input("Enter the subject: ")
                mark = input("Enter the mark: ")
                student.add_mark(subject, mark)
                break

    def list_students(self):
        if not self.students:
            print("\nNo students available.")
        else:
            print("Student list:")
            for i, student in enumerate(self.students):
                print(f"{i + 1}. ", end="")
                student.display_info()
                print("GPA of selected student : ", student.gpa())
        #Sỏting
        self.students.sort(key=lambda x: x.gpa(), reverse=True)
        print("\nSorted by GPA (Highest to Lowest):\n")
        for i, student in enumerate(self.students):
            print(f"{i +  1}. ", end="")
            student.display_info()

    def list_courses(self):
        if not self.courses:
            print("\nNo courses available.")
        else:
            print("Course list:")
            for i, course in enumerate(self.courses):
                print(f"{i + 1}. ", end="")
                course.display_info()