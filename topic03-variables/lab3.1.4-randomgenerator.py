# Lab 3.1 - Variables and states
# Program that prints out a random number between 1 and 10
# Author Daniel Finnerty

import random

numberlwr = int(input("Enter low end of range: "))
numberupr = int(input("Enter upper end of range: "))

number = random.randint(numberlwr,numberupr)
print("Here is a random number {}" .format(number))
