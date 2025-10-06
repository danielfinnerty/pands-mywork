# Lab 4.2.2 Loops
# Program to prompt a user to guess a number until guessed correctly while providing hints
# Author: Daniel Finnerty

import random

guess = int(input("Please guess the number: "))
number = (random.randrange(0,1000))

while guess != number:
    if guess < number:
        print("Too low")

    else: # since it isn't equal to, or too low, it must be higher.
        print("Too High")
    
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was", guess)