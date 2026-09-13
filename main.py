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
    print("5. Find Strongest / Weakest Subjects")
    print(" ")
    print("6. Set Target Marks")
    print(" ")
    print("7. Generate Study Recommendations")
    print(" ")
    print("8. Compare Current & Previous Performance")
    print(" ")
    print("9. Generate Student Report")
    print(" ")
    print("10. Class Performance Statistics")
    print(" ")
    print("11. Exit")
    print(" ")
    print("=====================================================")
    print(" ")
    a = int(input("Enter your choice:"))
    print(" ")
    return a

a = introscreen()

if a == 1 :
    print("You have selected 1. Create Student Profile")

elif a == 2 :
    print("You have selected 2. Enter Subject Marks")
    
elif a == 3 :
    print("You have selected 3. View Academic Record")
    
elif a == 4 :
    print("You have selected 4. Analyze Performance")
    
elif a == 5 :
    print("You have selected 5. Find Strongest / Weakest Subjects")
    
elif a == 6 :
    print("You have selected 6. Set Target Marks")
    
elif a == 7 :
    print("You have selected 7. Generate Study Recommendations")
    
elif a == 8 :
    print("You have selected 8. Compare Current & Previous Performance")
    
elif a == 9 :
    print("You have selected 9. Generate Student Report")
    
elif a == 10 :
    print("You have selected 10. Class Performance Statistics")
    
elif a == 11 :
    print("You have selected 11. Exit")

else:
    print("Error")
    
print(" ")