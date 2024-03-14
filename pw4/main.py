from domains.school import School
from output import Output 
from input import Input
if __name__ == "__main__":
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
                Input.input_students(school)
            elif option == 2:
                Input.input_courses(school)
            elif option == 3:
                Input.input_marks(school)
            elif option == 4:
                Output.list_students(school)
            elif option == 5:
                Output.list_courses(school)
            else:
                print("Invalid Option\n")