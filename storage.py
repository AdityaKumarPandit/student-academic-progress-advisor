import json

def load_students():
    
    with open("data/students.json" , "r") as file:
        students = json.load(file)
              
    return students

def save_students(students):
    
    with open("data/students.json", "w") as file:
        json.dump(students, file, indent = 4)
    