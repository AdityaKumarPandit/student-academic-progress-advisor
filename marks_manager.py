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