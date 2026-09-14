from storage import load_students, save_students

def enter_subject_marks():
    reg_num = input("Enter Registration Number: ")
    students = load_students()

    if reg_num not in students:
        print("Student Not Found.")
        return

    student = students[reg_num]

    print("Name:", student["name"])
    print(f"Registration Number: {student['reg_num']}")
    print(f"Semester: {student['semester']}")
    print(f"Program: {student['program']}")
    print(f"Number of Subjects: {student['sub_num']}")

    confirm = input("Is this the correct student? (y/n): ")

    if confirm == "y":

        subjects = {}

        for i in range(student["sub_num"]):

            print(f"\nSubject {i + 1}")

            sub_name = input("Enter Subject Name: ")
            max_marks = int(input("Enter Maximum Marks: "))
            sub_marks = int(input("Enter Marks Obtained: "))

            subjects[sub_name] = {
                "max_marks": max_marks,
                "marks_obtained": sub_marks
            }

        student["subjects"] = subjects

        save_students(students)

        print("Subject marks saved successfully.")

    elif confirm == "n":

        print("Returning to main menu.")

    else:

        print("Please answer only with 'y' or 'n'.")