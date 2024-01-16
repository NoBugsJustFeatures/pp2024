courses = []
students =[]
num_students = 0
num_courses = 0

def input_something(type):
    return int(input(f"Enter the number of {type} :"))

def input_info(type):
    item = {"mark": {}}
    if type == "students":
        item["name"] = input("Enter student's name: ")
        item["DoB"] = input("Enter student DoB: ")
        item["id"] = input("Enter student ID: ")
    elif type == "courses":
        item["name"] = input("Enter course name: ")
    return item

def input_mark(student):
    subject = input("Enter the subject: ")
    mark = input("Enter the mark: ")
    student["mark"][subject] = mark
    
def list_students(students):
    if len(students) == 0:
        print("\nNo students available.")
    else:
        print("Student list: ")
        for i, student in enumerate(students):
            print(f"{i + 1}. {student['id']} - {student['name']} - {student['DoB']}")
            if "mark" in student:
                print("Marks: ", end="")
                for subject, mark in student["mark"].items():
                    print(f"{subject}: {mark}", end="")
                print()
                
def list_courses(courses):
    if len(courses) == 0 :
        print("\nNo courses available.\n")
    else:
        print("Course List:\n",end='')
        for i,course in enumerate(courses):
            print(f"\n{i+1}. {course['name']}\n")
            
def main():
    while(True):
        print("""
        =============================
        0. Exit
        1. Input students
        2. Input courses
        3. Input marks
        4. Display courses
        5. Display students and mark
        =============================
        """)
        option = int(input("Your choice: "))
        if option == 0:
            print("\nExit program ...")
            break
        if option == 1:
            num_students = input_something("students")
            for i in range(num_students):
                students.append(input_info("students"))
        elif option == 2:
            num_courses = input_something("courses")
            for i in range(num_courses):
                courses.append(input_info("courses"))
        elif option == 3:
            student_id = input("Enter the student id: ")
            for student in students:
                if student["id"] == student_id:
                    input_mark(student)
                    break
        elif option == 4:
            list_courses(courses)
        elif option == 5:
            list_students(students)
        else:
            print("Invalid Option\n")
            
main()