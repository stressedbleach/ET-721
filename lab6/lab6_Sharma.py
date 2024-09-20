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

