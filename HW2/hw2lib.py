"""
Library file for ITIN 8000 HW 2, by kyle finley

This library defines:

1. def role_input():
#returns an input for the role (Waiter Customer Manager)

2. def flag_check(low_num, high_num, iaction, and action flag)
# resets action_flag if correct

"""

# -----prompt the user to input a role-----
# Loops until input is between 1 and 3
# returns user input "(1)Waiter (2)Customer (3)Manager"
def role_input():
    # set role flag to 1 to enter loop
    role_flag = 1
    while role_flag:
        print("\nWhat [role] do you want? (Type corresponding number)")
        print("(1)Waiter (2)Customer (3)Manager")
        role = input("Enter your choice:")

        irole = int(role)  # convert to int

        # checks the interger in irole
        # after the correct role is entered flag is turned off
        if 1 > irole or irole > 3:
            print("\n[Enter a number between 1 and 3]") # incorrect input
        else:
            role_flag = 0 # correct input

    return irole

# Resets the flag if correct choice was chosen
# takes lowest number, highest number, input number, and action flag
# resets flag if number is correct
def flag_check(low_num, high_num, iaction, action_flag):
    if low_num > iaction or iaction > high_num:
        print("\n[Enter a number between", low_num, "and", high_num, "]")
    else:
        action_flag = 0

    return action_flag