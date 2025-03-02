from domains.student import Student
from domains.course import Course

import json
import gzip

def input_students():
    students = []
    total_student = int(input("Enter the number of students: "))
    for _ in range(total_student):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (DD/MM/YYYY): ")
        students.append({'id': id, 'name': name, 'dob': dob})
    
    with open('students.txt', 'w') as file:
        json.dump(students, file)
    
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter the number of courses: "))
    for _ in range(num_courses):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credit = input("Enter course credit: ")
        courses.append({'id': id, 'name': name, 'credit': credit})
    
    with open('courses.txt', 'w') as file:
        json.dump(courses, file)
    
    return courses

def input_marks(students, courses):
    marks = []
    course_id = input("Enter the course ID to input marks for: ")
    for course in courses:
        if course['id'] == course_id:
            for student in students:
                mark = input(f"Enter mark for student {student['name']}: ")
                marks.append({'course': course['name'], 'student': student['name'], 'mark': mark})
    
    with open('marks.txt', 'w') as file:
        json.dump(marks, file)
    
    return marks


def compress_files():
    with open('students.txt', 'rb') as file:
        students_data = file.read()
    with open('courses.txt', 'rb') as file:
        courses_data = file.read()
    with open('marks.txt', 'rb') as file:
        marks_data = file.read()
    
    with gzip.open('students.dat', 'wb') as file:
        file.write(students_data)
        file.write(courses_data)
        file.write(marks_data)

def check_and_decompress():
    try:
        with gzip.open('students.dat', 'rb') as file:
            data = file.read()
        
        students_data = data[:len(data)//3]
        courses_data = data[len(data)//3:2*len(data)//3]
        marks_data = data[2*len(data)//3:]
        
        with open('students.txt', 'wb') as file:
            file.write(students_data)
        with open('courses.txt', 'wb') as file:
            file.write(courses_data)
        with open('marks.txt', 'wb') as file:
            file.write(marks_data)
        
        return True
    except FileNotFoundError:
        return False