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
from array import *
from hw2lib import *

# creates the dictionary for all the food
FoodDict = {
    0: 'Chicken',
    1: 'Beef',
    2: 'Vegetarian',
    3: 'Soup',
    4: 'Salad',
    5: 'Merlot',
    6: 'Chardonnay',
    7: 'Pinot_Noir',
    8: 'Rose',
    9: 'Flan',
    10: 'Creme_Brulee',
    11: 'Chocolate_Moose',
    12: 'Cheesecake'
}

# StoreFlag activates the randomizer for food
StoreFlag = 1

# if StoreFlag is 2 then -> Exit Program
# if StoreFlag is 1 then -> loop program, randomize new food
# if StoreFlag is 0 then -> loop program, no new food
while StoreFlag != 2:

    # -----Checks if food needs to be randomized-----
    # if StoreFlag is 1 then -> randomize new food
    if StoreFlag == 1:

        # -----Generate a quantity for each of the menu items-----
        # Creates a food array with 13
        food = array('i', [])
        # Entrees (Random quantity between 1 and 6 of each)
        for i in range(0,3):
            food.append(random.randint(1,6))
        # Sides (Random quantity between 5 and 10 of each)
        for i in range(0,2):
            food.append(random.randint(5,10))
        # Wines (Random quantity between 2 and 5 each)
        for i in range(0, 4):
            food.append(random.randint(2, 5))
        # Desserts (Random quantity between 1 and 3 each)
        for i in range(0,4):
            food.append(random.randint(1,3))
        # Food was randomized, StoreFlag reset to 0
        StoreFlag = 0

    # -----prompt the user to input a role-----
    # Loops until input is between 1 and 3
    # returns user input "(1)Waiter (2)Customer (3)Manager"
    irole = role_input()

    # initialize action_flag to 1 to start next loop for user action input
    action_flag = 1

    # -----prompt the user for an action based on role from user input "irole"-----
    # if action_flag is 0 then -> action is complete and a valid choice was made
    # if action_flag is 1 then -> loop until valid action is selected
    while action_flag:
        # Output text for action prompt
        print("\nWhat [action] do you want? (Type corresponding number)")

        # checks the integer in irole to list correct options
        # after the correct action is entered flag is turned off
        # This is a Large if else statement for (1)Waiter (2)Customer (3)Manager
        if irole == 1: # Waiter options-------------------------------------------
            # if waiter was chosen then display waiter options
            print("Read Menu: (1)Entrees (2)Wines (3)Sides (4)Desserts (5)all")
            # collect user input
            action = input("Enter your choice:")
            # convert input to int
            iaction = int(action)

            # Resets the flag if correct choice was chosen
            # takes lowest number, highest number, input number, and action flag
            # resets flag if number is correct
            action_flag = flag_check(1, 5, iaction, action_flag)

            # Displays the information based on the correct number entered.
            # Range is determined by dictionary list at beginning

            if iaction == 1 and len(food) > 1:
                for i in range(0,3):
                    print(FoodDict[i], food[i])
            elif iaction == 2 and len(food) > 1:
                for i in range(3,5):
                    print(FoodDict[i], food[i])
            elif iaction == 3 and len(food) > 1:
                for i in range(5,9):
                    print(FoodDict[i], food[i])
            elif iaction == 4 and len(food) > 1:
                for i in range(9,13):
                    print(FoodDict[i], food[i])
            elif iaction == 5 and len(food) > 1:
                for idx, i in enumerate(food):
                    print(FoodDict[idx], i)
            else:
                # Display no food if no food
                print("\n***Store is closed, no food***")

        elif irole == 2: # Customer options-------------------------------------------
            # if customer was chosen then display customer options
            print("(1)Order Food (2)Random Order of 4 items")
            # collect user input
            action = input("Enter your choice:")
            # convert input to int
            iaction = int(action)

            # Resets the flag if correct choice was chosen
            # takes lowest number, highest number, input number, and action flag
            # resets flag if number is correct
            action_flag = flag_check(1, 2, iaction, action_flag)

            # Takes action based on choice
            if iaction == 1 and len(food) > 1: # Order Food

                # initialize order_flag to 1 to start next loop
                order_flag = 1

                # order_flag 1 means invalid options were chosen
                # if order_flag is 1 then -> loop
                while order_flag == 1:
                    order_flag = 0  # resets flag

                    # sets up description bar for menu
                    print("(choice) Name Quantity")
                    # prints out full list of food choices
                    for idx, i in enumerate(food):
                        print("(", idx,")", FoodDict[idx], i)

                    # initialize order array
                    order = []
                    # take user input into an array
                    order = [int(item) for item in input("Enter the list items separated by spaces: ").split()]

                    # Sets the flag if bad order was detected
                    for i in order:
                        if 0 > i or i > 12:
                            order_flag = 1  # bad order
                        else:
                            pass

                    # if bad order was detected print statement
                    if order_flag == 1:
                        print ("\n**An order number was not between 0 and 12**")
                        print ("**Please try again**\n")

                # Orders the food, takes out what was ordered
                # displays what was empty
                for i in order:
                    if food[i] > 0:
                        # prints "name of food" and was ordered
                        print(FoodDict[i], "was ordered")
                        food[i] = food[i] - 1
                    else:
                        # prints there is no "name of food ordered"
                        print("There is no", FoodDict[i] )

            # Random Order
            elif iaction == 2 and len(food) > 1:
                # initialize order array
                order = []
                # randomly put some orders into array
                order = [random.randint(0, 12), random.randint(0, 12), random.randint(0, 12), random.randint(0, 12)]

                # Orders the food, takes out what was ordered
                # displays what was empty
                for i in order:
                    if food[i] > 0:
                        # prints "name of food" and was ordered
                        print(FoodDict[i], "was ordered")
                        food[i] = food[i] - 1
                    else:
                        # prints there is no "name of food ordered"
                        print("There is no", FoodDict[i] )
            else:
                # Display no food if no food
                print("\n***Store is closed, no food***")

        elif irole == 3:  # Manager options-------------------------------------------
            # if manager was chosen then display manager options
            print("(1)Close (2)Open (3)Exit")
            # collect user input
            action = input("Enter your choice:")
            # convert input to int
            iaction = int(action)

            # Resets the flag if correct choice was chosen
            # takes lowest number, highest number, input number, and action flag
            # resets flag if number is correct
            action_flag = flag_check(1, 3, iaction, action_flag)

            # Takes action based on choice
            if iaction == 1:  # Close
                # StoreFlag to 0 no random food
                StoreFlag = 0
                # empty the food array
                food = array('i', [])
                # display store closed
                print("\n***Store Closed***")
            elif iaction == 2:  # Open
                # StoreFlag to 1 for random food
                StoreFlag = 1
                print("\n***Store Opened***")
            elif iaction == 3:  # Exit
                # StoreFlag to 2 to Exit program
                StoreFlag = 2
        else:
            # this should never happen
            print ("Role out of bounds error, Program End")
            action_flag = 2


