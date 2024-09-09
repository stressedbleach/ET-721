"""
Simridhi Sharma
Lab 3, python review
9/9/2024
"""

print ("---------- Example 1: control flow ---------- ")

labs= int(input("Enter labs' grade: "))
exams = int(input("Enter exams' grade: "))
final=0
gpa = ''

if (0<=labs<=100 and 0<=exams<=100): 
    final = (labs+exams) / 2
    if (100>=final>=90):
        gpa = 'A'
    elif(90>final>=80):
        gpa = 'B'
    elif(80>final>=70):
        gpa = 'C'
    elif(70>final>=60):
        gpa = 'D'
    elif (60>final>=0):
        gpa = 'F'
    else:
        gpa = 'undefined.'
else:
    if not(0<=labs<=100):
        print(f"Grade for labs {labs} is invalid.")
    elif not(0<=exams<=100):
        print(f"Grade for exams {exams} is invalid.")
    else:
        print(f"Grade for labs {labs}, and exams {exams} are invalid.")
    gpa = "undefined"
    
    
print(f"Your final grade for the class is {final}, and your gpa is {gpa}.")