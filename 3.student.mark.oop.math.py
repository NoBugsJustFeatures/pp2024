import math as m
import numpy as np

class Student:
    def __init__(self, name, dob, student_id):
        self.name = name
        self.dob = dob
        self.student_id = student_id
        self.marks = {}

    def add_mark(self, subject, mark):
            self.marks[subject] = m.floor(float(mark) * 10) / 10

    def gpa(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)
    def display_info(self):
        print(f"ID: {self.student_id} - Name: {self.name} - DoB: {self.dob}")
        if self.marks:
            print("Marks:")
            for subject, mark in self.marks.items():
                print(f"  {subject}: {mark}")
    
    def weighted_gpa(self,credits) :
        if not self.marks:
            return 0
        total_weighted_marks = sum(np.array(list(self.marks.values()) * np.array(credits)))
        total_credit = sum(credits)
        return total_weighted_marks / total_credit 

class Course:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Name: {self.name}")


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

    def main_menu(self):
        while True:
            print("""
            =============================
            0. Exit
            1. Input students
            2. Input courses
            3. Input marks
            4. Display students
            5. Display courses
            =============================
            """)
            option = int(input("Your choice: "))
            if option == 0:
                print("\nExit program ...")
                break
            elif option == 1:
                self.input_students()
            elif option == 2:
                self.input_courses()
            elif option == 3:
                self.input_marks()
            elif option == 4:
                self.list_students()
            elif option == 5:
                self.list_courses()
            else:
                print("Invalid Option\n")

if __name__ == "__main__":
    school = School()
    school.main_menu()