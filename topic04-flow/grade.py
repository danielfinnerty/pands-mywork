# Lab 4.1.2 If, Elif, else
# Program to present students grade based off mark
# Author: Daniel Finnerty

'''
grade = int(input("Please enter student percentage mark: "))


if (grade < 40):
    print("Fail")
elif (grade >= 40 and grade < 49)
    print ("Pass")
'''

percentage = float(input("Please enter student percentage mark: "))

rounded = round(percentage, 0)

if rounded < 0 or rounded > 100:
    print ("Please enter a number between 0 and 100")
elif rounded < 40:
    print ("Fail")
elif rounded < 50:
    print ("Pass")
elif rounded < 60:
    print ("Merit 2")
elif rounded < 70:
    print ("Merit 1")
else:
    print ("Distinction")

# Still have to do number 4 adn 5 from the worksheet