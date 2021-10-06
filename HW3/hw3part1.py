"""
Kyle Finley Homework 3 ITIN 8000
Part 1

In part 1 I want you to create a python script that collects input from a user write it to a binary file and a text file and then read those files back.
Please:

Ask for the users first and last name, favorite color, and date of birth
Calculate how many days old the user is
Write the user's name in the format last name, first name and favorite color in a .txt named UserName
Write the user's age in days to a binary file named Days Old
Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old
A file named hw3part1.py should perform these tasks when it is run
"""

import datetime
import csv

# -----Ask for the users first and last name, favorite color, and date of birth-----
# collect user input
fname = input("Enter your first name:")
lname = input("Enter your last name:")
favC = input("Enter your favorite color:")
dob = input('Please enter your birthday(mm/dd/yyyy): ')


# -----Calculate how many days old the user is-----
# convert the date of birth to a datetime
birthDate = datetime.datetime.strptime(dob,'%m/%d/%Y')
# gets the current datetime for today
currentDate = datetime.datetime.today()
# get the differece between current time and data entered
dOld = currentDate - birthDate
# store days_old as just the int of days, cutoff the rest
dOldINT = dOld.days


# -----Write the user's name in the format last name, first name and favorite color in a .txt named UserName-----
# Open/create UserName.txt to append
File_object = open("UserName.txt","a")
# writes last, first, and fav color with spaces after
File_object.write(lname)
File_object.write(" ")
File_object.write(fname)
File_object.write(" ")
File_object.write(favC)
File_object.write(" ")
File_object.close()

# -----Write the user's age in days to a binary file named Days Old-----
# convert dOldINT to bytes
bytes_val = dOldINT.to_bytes(2, 'big')
# open a bin and wirte bytes to it
file = open("Days_Old.bin", "wb")
file.write(bytes_val)
file.close()


# Add the user to a CSV file named UserData.csv in the order Last Name, First Name, Favorite Color, Days Old
# opens csv with write
with open('UserData.csv', 'w', newline='') as csvfile:
    # set header names
    fieldnames = ['last_name', 'first_name', 'Favorite_Color', 'Days_Old']
    # set the writer to write the fields
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # call writer and wright the user data
    writer.writeheader()
    writer.writerow({'last_name': lname, 'first_name': fname, 'Favorite_Color': favC, 'Days_Old': dOldINT})
