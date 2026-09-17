from student_manager import create_student_profile
from marks_manager import enter_subject_marks
from acedemic_report import view_report
from performance_analysis import performance_analysis_report
from Edit import edit_profile

def introscreen():

    print(" ")
    print("=====================================================")
    print("         STUDENT ACADEMIC PROGRESS ADVISOR           ")
    print("=====================================================")
    print(" ")
    print("1. Create Student Profile")
    print(" ")
    print("2. Enter Subject Marks")
    print(" ")
    print("3. View Academic Record")
    print(" ")
    print("4. Analyze Performance")
    print(" ")
    print("5. Edit Student Details")
    print(" ")
    print("6. Update Subject Marks")
    print(" ")
    print("7. Delete Student Record")
    print(" ")
    print("8. Search Student")
    print(" ")
    print("9. Exit")
    print(" ")
    print("=====================================================")
    print(" ")
    
    a = int(input("Enter your choice: "))

    print(" ")

    return a


while True:

    a = introscreen()

    if a == 1:

        print("You have selected 1. Create Student Profile")
        create_student_profile()

    elif a == 2:

        print("You have selected 2. Enter Subject Marks")
        enter_subject_marks()

    elif a == 3:

        print("You have selected 3. View Academic Record")
        view_report()
        
    elif a == 4:

        print("You have selected 4. Analyze Performance")
        performance_analysis_report()
        
    elif a == 5:

        print("You have selected 5. Edit Student Details")
        edit_profile()
        
    elif a == 6:

        print("You have selected 6. Update Subject Marks")

    elif a == 7:

        print("You have selected 7. Delete Student Record")

    elif a == 8:

        print("You have selected 8. Search Student")

    elif a == 9:

        print("You have selected 9. Exit")
        print(" ")
        print("Thank you for using Student Academic Progress Advisor.")
        print(" ")
        print("=====================================================")
        break

    else:

        print("Error: Please enter a choice between 1 and 9.")

    print(" ")