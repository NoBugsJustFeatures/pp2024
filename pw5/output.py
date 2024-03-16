class Output:
    def list_students(school):
            if not school.students:
                print("\nNo students available.")
            else:
                print("Student list:")
                for i, student in enumerate(school.students):
                    print(f"{i + 1}. ", end="")
                    student.display_info()
                    print("GPA of selected student : ", student.gpa())
            #Sỏting
            school.students.sort(key=lambda x: x.gpa(), reverse=True)
            print("\nSorted by GPA (Highest to Lowest):\n")
            for i, student in enumerate(school.students):
                print(f"{i +  1}. ", end="")
                student.display_info()

    def list_courses(school):
        if not school.courses:
            print("\nNo courses available.")
        else:
            print("Course list:")
            for i, course in enumerate(school.courses):
                print(f"{i + 1}. ", end="")
                course.display_info()