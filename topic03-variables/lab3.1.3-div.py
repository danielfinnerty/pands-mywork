# Lab 3.1 - Variables and states
# Program that reads in 2 numbers
# and outputs the integer answer and remainder
# Author Daniel Finnerty

number01 = int(input("Enter first number: "))
number02 = int(input("Enter the number you want to divied by: "))

answer = number01 // number02
remainder = number01%number02
print("{} divided by {} is {} with remainder {}" .format(number01, number02, answer, remainder))