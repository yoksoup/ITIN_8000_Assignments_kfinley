"""
Kyle Finley Homework 2 ITIN 8000

# Generate a quantity for each of the menu items
Entrees (Random quantity between 1 and 6 of each)
Chicken
Beef
Vegetarian

Sides (Random quantity between 5 and 10 of each)
Soup
Salad

Wines (Random quantity between 2 and 5 each)
Merlot
Chardonnay
Pinot Noir
Rose

Desserts (Random quantity between 1 and 3 each)
Flan
Creme Brulee
Chocolate Moose
Cheesecake


# prompt the user to input a role
Waiter Customer Manager


# prompt the user an action
Read Menu: lists how much of each menu item is available
What are the (Entrees/Wines/Sides/Desserts): lists how much of each of the chosen categories is available

Order (ordered food): takes an order from the customer and subtracts the order from the available food total.
Customers are told if what they ordered is not available and asked if they would like something else
Customers must be able to make their selection in any order and leave out choices. For example, they could just ask for Merlot or they could ask for Flan, Pinot Noir, Salad, and Beef
Random Choice
A random order is made using the choice function from the random module
See Chapter 11 of IP or 3.11 of the Python Cookbook

Manager
Close: Lists the remaining food at the end of the night and then sets all of the values to zero
Open: Restarts the main .py file and generates a new random amount of foods
"""
#import
import random

# -----Generate a quantity for each of the menu items-----
# Entrees (Random quantity between 1 and 6 of each)
Chicken = random.randint(1,6)
Beef = random.randint(1,6)
Vegetarian = random.randint(1,6)

# Sides (Random quantity between 5 and 10 of each)
Soup = random.randint(5,10)
Salad = random.randint(5,10)

# Wines (Random quantity between 2 and 5 each)
Merlot = random.randint(2,5)
Chardonnay = random.randint(2,5)
Pinot_Noir = random.randint(2,5)
Rose = random.randint(2,5)

# Desserts (Random quantity between 1 and 3 each)
Flan = random.randint(1,3)
Creme_Brulee = random.randint(1,3)
Chocolate_Moose = random.randint(1,3)
Cheesecake = random.randint(1,3)

# -----prompt the user to input a role-----
# Waiter Customer Manager
# Loops until input is not between 1-3
role_flag = 1
while role_flag:
    print ("\nWhat [role] do you want? (Type corresponding number)")
    print ("(1)Waiter (2)Customer (3)Manager")
    role = input("Enter your choice:")

    irole = int(role) #convert to int

    # checks the interger in irole
    # after the correct role is entered flag is turned off
    if 1 > irole or irole > 3:
        print ("\n[Enter a number between 1 and 3]")
    else:
        role_flag = 0

"""
# Set role string
srole = {
    1 : "Waiter",
    2 : "Customer",
    3 : "Manager",
}

print("srole =", srole)
"""

# prompt the user an action based on role
# Waiter Customer Manager
action_flag = 1
while action_flag:
    print("\nWhat [action] do you want? (Type corresponding number)")

    # checks the interger in irole to list correct options
    # after the correct action is entered flag is turned off
    if irole == 1: # Waiter options
        print("Read Menu: (1)Entrees (2)Wines (3)Sides (4)Desserts")
        action = input("Enter your choice:")
        iaction = int(action)  # convert to int

        if 1 > iaction or iaction > 4:
            print("\n[Enter a number between 1 and 4]")
        else:
            action_flag = 0

    elif irole == 2: # Customer options
        print("(1)Order Food (2)Random Order")
        action = input("Enter your choice:")
        iaction = int(action)  # convert to int

        if 1 > iaction or iaction > 2:
            print("\n[Enter a number between 1 and 2]")
        else:
            action_flag = 0

    elif irole == 3: # Manager options
        print("(1)Close (2)Open")
        action = input("Enter your choice:")
        iaction = int(action)  # convert to int

        if 1 > iaction or iaction > 2:
            print("\n[Enter a number between 1 and 2]")
        else:
            action_flag = 0

    else:
        print ("Role out of bounds error, retry")
        action_flag = 0