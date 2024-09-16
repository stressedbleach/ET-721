"""
simridhi sharma
sept. 16th, python functions
"""
import math
import random


#define a function to print a message. this is a function that doesnt return nor pass a value
def hellofunction():
    print("Welcome to function!")

#example 2: function that passes a susername as argument, but it doesnt return any values
def greeting(username):
    print(f"\nGood afternoon {username}.\n")
    

#example 3: functoin with default parameters, but doesnt return any values
def usercountry(country="USA"):
    print(f"I am from {country}.")

#example 4: function that doesnt return nor pass a value
def triplenum(num):
    return 3*num

#example 5: function that passes two numbers and check if the two numbers are divisble by each other
#the function return true if they are divisible, and false if not
def isdivisible(n1, n2):
    if(n1%n2 == 0 or n2%n1 == 0):
        return True
    else:
        return False


#example 6: functoin that passes a radius and returns the circumference
def circumference(radius=0):
    return 2*math.pi*radius


#call a function that doesnt return nor pass a value
print("\n---------- Example 1 ----------\n ")
hellofunction()
hellofunction()
print("\n")

print("\n ---------- Example 2 ---------- \n")
username = "stressedbleach"
greeting(username)

print("\n ---------- Example 3: function with default parameter ---------- \n")
usercountry("America")
usercountry()

print("\n ---------- Example 4: function that passes a number and return the triple of the number ---------- \n")
num = 9
print(f"The triple of number {num} is {triplenum(num)}.")

print("\n ---------- Example 5: function that passes two numbers and returns true or false ---------- \n")
n1 = 10
n2 = 50
check1 = isdivisible(n1,n2)
print(f"Is {n1} and {n2} divisible? {check1}.")


print("\n---------- Example 6: function that passes a radius and returns the circumference ----------\n ")
r = 5
c = circumference(r)
print(f"A circle with the radius {r} has a circumference of {c: .2f}.")

print("\n---------- Example 7: random numbers ----------\n ")
print(f"random number {random.random()}")
print(f"random uniform {random.uniform(-5,5)}")
print(f"random integer {random.randint(-10,10)}")