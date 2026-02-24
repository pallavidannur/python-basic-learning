add= lambda a,b: a+b
print (add (1,100))


double = lambda x: x*2
print (double (200))


students =[
    {"name": "Alice", "marks": 80},
    {"name": "Bob", "marks": 100},
    {"name": "Charlie", "marks": 90} 
]                    
student = sorted(students, key=lambda x: x["marks"], reverse=True)
print(student)