"""
ITIN 8000, Kyle Finley HW1
This code is to print out the following statements:
“Hello. Todays Date is [Month Name] [Day Number][th/nd/st/rd] of [Year].
The product of the month and day is [Month Number * Day], which is an [Odd/Even] number.
If you counted the days this month so far you would have
[Loop to count up to the current day of the month with each number on a new line] days.”
"""

# Import and assign the year month and day
# using datetime module
import datetime
year = datetime.datetime.today().strftime('%Y')
month = datetime.datetime.today().strftime('%m')
day = datetime.datetime.today().strftime('%d')

# Convert string to int
iday = int(day)
imonth = int(month)

# Create product from day and month
product = iday * imonth

# display today's date
print("\nHello. Today's Date is", month, day, "of", year, ".")

# is the product even or odd?
# display the correct statement
if (product % 2) == 0:
    print("The product of the month and day is", product, ",", "which is an even number.")
else:
    print("The product of the month and day is", product, ",", "which is an odd number.")

# print days counted statement
print("\nIf you counted the days this month so far you would have")

# Loop if x != days
# print x, ++x
for x in range(iday):
    print(x+1) # +1 b/c it starts at 0

# print "days"
print("days")
