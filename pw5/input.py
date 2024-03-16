from domains.student import Student
from domains.course import Course

class Input:
    def input_students(school):
        num_students = int(input("Enter the number of students: "))
        with open("students.txt", "a") as f:
            for _ in range(num_students):
                name = input("Enter student's name: ")
                dob = input("Enter student DoB: ")
                student_id = input("Enter student ID: ")
                student = Student(name, dob, student_id)
                school.students.append(student)
                f.write(f"{name},{dob},{student_id}\n")

    def input_courses(school):
        num_courses = int(input("Enter the number of courses: "))
        with open("courses.txt", "a") as f:
            for _ in range(num_courses):
                name = input("Enter course name: ")
                course = Course(name)
                school.courses.append(course)
                f.write(f"{name}\n")

    def input_marks(school):
        student_id = input("Enter the student ID: ")
        with open("marks.txt", "a") as f:
            for student in school.students:
                if student.student_id == student_id:
                    subject = input("Enter the subject: ")
                    mark = input("Enter the mark: ")
                    student.add_mark(subject, mark)
                    f.write(f"{student_id},{subject},{mark}\n")

    