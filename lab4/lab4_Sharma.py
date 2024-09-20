'''
Simridhi Sharma
lab 4
9/13/2024
python data and functions
'''

print ("\n ---------- example 1: dictionary ---------- ")
car = {
    "brand" : "Subaru",
    "model" : "WRX",
    "year" : 2024,
    "last visit" : "March 2024"
}

print (f"Best car 2024 = {car['brand']}, model = {car['model']}")

print ("\n---------- example 2: loops through each key in a dictionary ----------")

for k in car:
    print(f"{k} has a value of {car[k]}")
    print(car[k])

print ("\n--------- example 3: among of key-pair in a dictionary ----------")
print (f"dictionary has {len(car)} key-value pairs.")

print ("\n--------- example 4: remove a key-value air from a dictionary ----------")
print(f"dictionary after removing the 'year' key-value pair. {car.pop('year')}")
for k in car:
    print(f"{k} , {car[k]}")

print ("\n--------- example 5: get value of a key ----------")
look_key = "last visit"
print(f"The value of key '{look_key}' is '{car[look_key]}'.") #you can replace {car[look_key]} with {car.get(look_key)}

print ("\n--------- example 6: store data in a dictionary ----------")
phrase = "to be or not to be"
phrase = phrase.split()
print(f"phrase after split method {phrase}")

word_count_dict = {} #empty dictionary
for word in phrase:
    if word not in word_count_dict:
        word_count_dict[word] = 1
    else:
        word_count_dict[word] += 1

print(word_count_dict)


print("\n---------- Excerise ----------")
#give the following user list, find the numbers of users that use 'gmail', 'hotmail' and 'yahoo'
user = '''
peter = ppan@gmail.com
diana = d@hotmail.com
kent = ckent@yahoo.com
bruce = bwayne@hotmail.com
tony = tstark@gmail.com
shrek = shrek@gmail.com
'''

email_count = {'gmail': 0, 'hotmail': 0, 'yahoo': 0}

users = user.strip().split('\n')
print (users)

for line in users:
    email = line.split('=')[1].strip()
    if 'gmail.com' in email:
        email_count['gmail'] += 1
    elif 'hotmail.com' in email:
        email_count['hotmail'] += 1
    elif 'yahoo.com' in email:
        email_count['yahoo'] += 1

print(email_count)
