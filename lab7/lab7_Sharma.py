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