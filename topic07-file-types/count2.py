# count.py
# file to count how many thimes it has ran

#Author: Daniel Finnerty

FILENAME = "count.txt"

def readNumber ():
    with open (FILENAME) as f:
        number = int(f.read())
        return number


def writeNumber (number):
    with open (FILENAME, "wt") as f:
        f.write(str(number))
        
num = readNumber()
num +=1
writeNumber(num)
print(num)