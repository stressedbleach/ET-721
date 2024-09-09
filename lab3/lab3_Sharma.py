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


print ("---------- Example 2: loops ----------")

secret = 8

userguess = int(input("Guess the secret number between 1 and 10: "))

while not (secret == userguess):
    userguess = int(input("wrong guess...womp womp loser :( \n Guess again: "))

print(f"Congrats! {userguess} is the right number!")

print("---------- Example 3: loops, break statements ----------")

balance = 1000
widthdraw = 0
deposit = 0

while True:
    userinput = input("Do you want to widthdraw (1), or deposit (2) your money today? ")
    if userinput == '1':
        w_amount = int(input("How much do you want to widthdraw? "))
        if w_amount>balance:
            print(f"Insufficient funds. You cannot widthdraw more than your balance, {balance}")
        else:
            balance -= w_amount
            print(f"Your new balance is {balance}.")
    elif userinput == '2':
        d_amount = int(input("How much do you want to deposit? "))
        balance += d_amount
        print(f"Your new balance is {balance}.")
    else: 
        print("Invalid selection!")
    
    choice = input("Would you like to do another transaction? (Y/N) ")
    if not(choice=='Y' or choice == 'y'):
        break

print("Thank you for banking with us!")