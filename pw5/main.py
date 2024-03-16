from domains.school import School
from output import Output 
from input import Input

if __name__ == "__main__":
        school = School()
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
                school.input_students()
            elif option == 2:
                school.input_courses()
            elif option == 3:
                school.input_marks()
            elif option == 4:
                school.list_students()
            elif option == 5:
                school.list_courses()
            else:
                print("Invalid Option\n")