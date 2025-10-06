# Lab 4.2.2 Loops
# Program to prompt a user to guess a number until guessed correctly
# Author: Daniel Finnerty

guess = int(input("Please guess the number: "))
number = 30

while guess != number:
    print("Wrong")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", guess)