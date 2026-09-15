from storage import load_students, save_students

def create_student_profile():
    print(" ")
    print("=====================================================")
    print("              CREATE STUDENT PROFILE                 ")
    print("=====================================================")
    print(" ")
    
    name = input("Enter Student Name: ")
    reg_num = input("Enter Registration Number: ")
    semester = int(input("Enter Semester: "))
    program = input("Enter Program: ")
    sub_num = int(input("Enter Number of Subjects: "))
    
    print(" ")
    print("=====================================================")
    print("       Student profile created successfully.         ")
    print("=====================================================")
    print(" ")
    student = {
    "name" : name, 
    "reg_num" : reg_num, 
    "semester" : semester,
    "program" : program, 
    "sub_num" : sub_num
    }
    
    students = load_students()
    
    students[reg_num] = student
    
    save_students(students)
    
    return student