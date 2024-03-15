from domains.student import Student
from domains.course import Course

class Input:
    def input_students(school):
            num_students = int(input("Enter the number of students: "))
            for _ in range(num_students):
                name = input("Enter student's name: ")
                dob = input("Enter student DoB: ")
                student_id = input("Enter student ID: ")
                student = Student(name, dob, student_id)
                school.students.append(student)

    def input_courses(school):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            name = input("Enter course name: ")
            course = Course(name)
            school.courses.append(course)

    def input_marks(school):
        student_id = input("Enter the student ID: ")
        for student in school.students:
            if student.student_id == student_id:
                subject = input("Enter the subject: ")
                mark = input("Enter the mark: ")
                student.add_mark(subject, mark)
    