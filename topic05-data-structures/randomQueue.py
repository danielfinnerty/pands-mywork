# Lab 5.3.1 Random Queue
# Program to tell user summer months
# Author: Daniel Finnerty


import random
queue = []
numberOfNumbers = 10
rangeTo = 100

for i in range (0,numberOfNumbers):
    n = random.randint(0,rangeTo)
    queue.append(n)

print (f"queue is {queue}")

while len(queue) != 0:

    currentNumber = queue.pop(0)
    print ("current Number is {} and the queue is {} ".format(currentNumber, queue))

print("the queue is now empty")
