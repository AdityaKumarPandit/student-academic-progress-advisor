from storage import load_students, save_students

def edit_profile():    
    print(" ")
    print("=====================================================")
    print("                 EDIT STUDENT RECORD                 ")
    print("=====================================================")
    print(" ")
    
    reg_num = input("Enter the Registration Number : ")
    
    students = load_students()
        
    if reg_num in students:
        print("Student Found")
    else:
        print("Student Not Found")

    print("-----------------------------------------------------")
    print("               CURRENT STUDENT DETAILS               ")
    print("-----------------------------------------------------")
    
    student = students[reg_num]
    
    print(f"Name = {student["name"]}")
    print(f"Registration Number = {student["reg_num"]}")
    print(f"Semester = {student["semester"]}")
    print(f"Program = {student["program"]}")
    print(" ")
    
    print("-----------------------------------------------------")
    print("              WHAT DO YOU WANT TO CHANGE?            ")
    print("-----------------------------------------------------")
    print(" ")
    
    print("1. Student Name")
    print(" ")
    print("2. Semester")
    print(" ")
    print("3. Program")
    print(" ")
    print("4. Back to Main Menu")
    print(" ")
    
    choice =input("Enter you choice : ") 
    
    if   choice == "1":
        print("You have selected 1. Student Name")
        
        print(f"Current Name = {student["name"]}")
        new_name = input("Enter the New Name : ")
        student["name"] = new_name 
        save_students(students)
        print("Student Name Successfully saved.")
    
    elif choice == "2":
        print("You have Selected 2. Semester")
    
    elif choice == "3":
        print("You have selected 3. Program")
        
    elif choice == "4":
        print("You have Selected 4. Back to main menu")
    
    else:
        print("Error, Please select from 1-4 only.")

    
        
edit_profile()