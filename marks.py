student_marks = {"pallavi":85,"keertan":90,"raju":78}


for student, marks in student_marks.items():
    print(f"{student}----{marks}")



    students = ["pallavi","keertan","raju"]
    marks = [85,90,78]
    
    student_marks = {}
    
    for i, student in enumerate(students):
        student_marks[student] = marks[i] 
    