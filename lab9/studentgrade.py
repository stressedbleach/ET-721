"""
SIMRIDHI SHARMA
sep 30th, 
unit testing input data
"""


def main():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                break
            else:
                print("Invalid input.")

        except ValueError:
            print("Invalid input, try again.")
    totalsumgrade = 0
    for i in range(num_students):
        while True:
            try:
                grade = int(input(f"Enter a grade for student {i+1}: "))
                if 0<= grade <=100:
                    totalsumgrade += grade
                    break
                else:
                    print("Grade must be between 0 and 100")

            except ValueError:
                print("Invalid input")

    average = totalsumgrade / num_students
    print(f"The class average is {average: .2f}")

if __name__ == "__main__":
    main()