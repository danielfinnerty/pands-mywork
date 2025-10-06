# es.py
# program that counts the number of
# e's from a text file
# Author: Daniel Finnerty

# Python program to demonstrate
# sys.argv


#source = https://www.geeksforgeeks.org/command-line-arguments-in-python/

import sys
import os.path

'''
print("This is the name of the program:", sys.argv[0])

print("Argument List:", str(sys.argv))
'''
if len(sys.argv) == 1:
    print("Filename not entered. Please try again")
'''
print(sys.argv[1])
'''
length = len(sys.argv)
print(length)
'''
FILENAME = (sys.argv[1])
print(FILENAME)


if not os.path.isfile(FILENAME):
    print ("File does not exist. Please check and try again.")
elif (FILENAME) == (""):
    print("Filename not entered. Please try again")
elif os.path.isfile(FILENAME):
    def readNumber ():
        with open (FILENAME) as f:
            number = f.read()
            return number
    num = readNumber()
    amount = num.count("e")
    print(amount)    
'''