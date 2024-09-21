""""
Simridhi sharma
sep 20th 2024
python classes
"""

print("\n----------- Example 1: exception handling ----------\n")

def hour_ratio():
    
    try:
        hours = 24
        h = int(input("Please enter a number to divide 24 hours: "))

        hours /= h #hpurs = hours/h
        return hours
    except ZeroDivisionError:
        print(f"The number {h} can't be divided by 24. Result is undefined.")
    except ValueError:
        print("Input value is not a number. Re-run the program and try again.")
    except:
        print("The program has an error. Please try again.")

print(hour_ratio())

print("\n========== End of program =========== \n")

print("\n----------- Example 2: classes ----------\n")

class Complex:
    def __init__(self, realpart, imgpart) :
        self.r = realpart
        self.i = imgpart

# create an instance of the class
point1= Complex(3.0, -4.5)

#calling the instance object
real1 = point1.r 
img1 = point1.i

#prompt result
print(f"real number = {real1} with imaginary number = {img1}. ")

print("\n----------- Example 3: classes with properties and methods ----------\n")

class Car:
    # properties, attributes, of class car
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
#method of class car
    def  get_descriptive_name(self):
        full_name = f"{self.year}, {self.make}, {self.model}"
        return full_name
#method 2: read and print the odometer
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
#method 3: update and print odometer
    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")
#method 4: increment odometer
    def increment_odometer(self, miles):
        self.odometer_reading += miles

#create an instance class car
usercar1 = Car("Toyota", "Supra", 2024)

#accessing properties and methods
print(usercar1.year)
#accessing method 'get_descriptive_name'
print(usercar1.get_descriptive_name())
usercar1.read_odometer()
usercar1.update_odometer(100)
usercar1.read_odometer()
usercar1.update_odometer(20)
usercar1.read_odometer()

usercar1.increment_odometer(35)
usercar1.read_odometer()



print("\n---------- EXCERISE ----------\n")

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0  # Initial balance set to 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        elif amount > self.balance:
            print(f"Insufficient balance. Current balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

# Creating an instance of the BankAccount class
useraccount = BankAccount("123456789", "Student's name")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)  # Should indicate insufficient balance
useraccount.deposit(1000)  # Should deposit 1000
useraccount.withdraw(500)  # Should successfully withdraw 500

# Print final balance
print(f"Final balance: {useraccount.balance}")
