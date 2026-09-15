from storage import load_students

def performance_analysis_report():
    
    print(" ")
    print("=====================================================")
    print("               PERFORMANCE ANALYSIS                  ")
    print("=====================================================")
    print(" ")
    
    reg_num = input("Enter the Registration Number: ")
    
    print(" ")
    
    students = load_students()
        
    if reg_num not in students:
        print("No data of this registration Number.")
        return
    
    student = students[reg_num]
    
    print("Name:", student["name"])
    print(f"Registration Number: {student['reg_num']}")
    print(f"Semester: {student['semester']}")
    print(f"Program: {student['program']}")
    print(f"Number of Subjects: {student['sub_num']}")
    
    print(" ")
    print("----------------------------------------------------------------------------------")
    print("Subjects                      Marks                               %age            ")
    print("----------------------------------------------------------------------------------")
    
    subjects = student["subjects"]
    
    for sub_name, marks in subjects.items():
        print(f"{sub_name}                  {marks['max_marks']}                 {(marks['marks_obtained']/marks['max_marks'])*100}")
        