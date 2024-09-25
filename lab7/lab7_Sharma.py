"""
simridhi sharma
9/23/2024
python files, lab 7
"""

print ("\n ----------- Example 1: python files ---------- \n")
#pipe the users.txt file
fileusers = open("users.txt", "r")
"""#use loop to go through each line of the file
for eachline in fileusers:
    print(eachline)
#alternative: print(fileusers.read())
#close file
fileusers.close()"""

print ("\n ----------- Example 2: Python limit to read files ---------- \n")
#read the first 10 characters
print(fileusers.read(10))
for eachline in fileusers:
    print(eachline)
    #reads the rest of the words

#close file
fileusers.close()

print ("\n ----------- Example 3: python read files with 'with' and 'r' ---------- \n")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    print(eachlines[0])

print ("\n ----------- Example 4: python read files with 'split()'  ---------- \n")
with open("users.txt", "r") as fileusers:
    eachlines = fileusers.readlines()
    for line in eachlines:
        word = line.split()
        print(word)


print ("\n ----------- Example 5: Python read file and check for a specific item ---------- \n")
#loop to the 'users.txt' file and check how many users are named 'Bruce'
def finduser(textfile, username):    
    with open(textfile, "r") as fileusers:
        eachlines = fileusers.readlines()
        userscounter = 0
        for line in eachlines:
            word = line.split()
            for eachword in word:
                    if eachword == username:
                        userscounter += 1
    return userscounter
user = "Bruce"
usercount = finduser("users.txt", user)
print(f"There is {usercount} with the name '{user}'")

print ("\n ----------- Example 6: Python write files ---------- \n")
def report(totalcount, username):
    with open("writeresult.txt", "w") as writeuserresult:
        writeuserresult.write(f"There is {totalcount} with the name '{username}'")
report(usercount,user)

print ("\n ----------- Example 7: Python appending data into a file ---------- \n")

def adduser(newuser,city, age, userfilename):
    try:
        with open(userfilename, "a" ) as fileusers:
            fileusers.write(f"\n{newuser}, {city}, {age}")
    except IOError:
        print(f"ERROR! couldnt find file named {userfilename}")
newusername = "Tony Stark"
city = "NYC"
age = 38
adduser(newusername, city, age, "newusers.txt")



"""Activity description: create a function, 
named email_read(), that reads a txt file and returns the number of users that have @gmail, @yahoo, and @hotmail email address. 
The function should have try-exception statement. 
You can test the function using the file user_email.txt file. 
Create a new file as "reportemail.txt
"""

def email_read():
    try:
        with open("user_email.txt", "r") as file:
            content = file.readlines()

        gmail_count = 0
        yahoo_count = 0
        hotmail_count = 0
        
        
        for email in content:
            if "@gmail.com" in email:
                gmail_count += 1
            elif "@yahoo.com" in email:
                yahoo_count += 1
            elif "@hotmail.com" in email:
                hotmail_count += 1
        
        with open("reportemail.txt", "w") as report_file:
            report_file.write(f"Gmail users: {gmail_count}\n")
            report_file.write(f"Yahoo users: {yahoo_count}\n")
            report_file.write(f"Hotmail users: {hotmail_count}\n")
        
        print("Report has been generated successfully.")
    
    except FileNotFoundError:
        print("Error: The file user_email.txt was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

email_read()