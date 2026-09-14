from storage import load_students

def view_report():
    print(" ")
    print("=====================================================")
    print("               VIEW ACADEMIC RECORD                  ")
    print("=====================================================")
    print(" ")

    reg_num = input("Enter Registration Number: ")
    students = load_students()

    if reg_num not in students:
        print("Student Not Found.")
        return

    student = students[reg_num]

    print(" ")
    print("=====================================================")
    print("                 STUDENT DETAILS                     ")
    print("=====================================================")
    print(" ")

    print("Name:", student["name"])
    print(f"Registration Number: {student['reg_num']}")
    print(f"Semester: {student['semester']}")
    print(f"Program: {student['program']}")
    print(f"Number of Subjects: {student['sub_num']}")

    confirm = input("Is this the correct student? (y/n): ")

    if confirm == "y":

        if "subjects" not in student:
            print("No marks have been entered for this student.")
            return

        print(" ")
        print("-----------------------------------------------------")
        print("Subjects                   Max Marks         Obtained")
        print("-----------------------------------------------------")

        subjects = student["subjects"]

        for sub_name, marks in subjects.items():
            print(f"{sub_name:<26} {marks['max_marks']:<17} {marks['marks_obtained']}")

# {sub_name:<26} means to Print sub_name left-aligned inside a space 26 characters wide.
# Similarly 
# {marks['max_marks']:<17} means to print maximum marks left-aligned inside a spce of 17 characters wide.
# here < means left alignment.

        print("-----------------------------------------------------")

    elif confirm == "n":
        print("Returning to main menu.")

    else:
        print("Please answer only with 'y' or 'n'.")