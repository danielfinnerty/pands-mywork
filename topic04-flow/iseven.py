# Lab 4.1.1 If, Elif, else
# Program to tell user if number inputted is odd or even
# Author: Daniel Finnerty

'''
number = int(input("Please enter your number: "))

if (number % 2) == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

'''

# Additional task (number 5) on worksheet

number = int(input("Please enter your number: "))

while number != -1:
    if (number % 2) == 0:
        number = int(input(f"{number} is an even number. Please enter another: "))

    else:
        number = int(input(f"{number} is an odd number. Please enter another: "))

print("end")