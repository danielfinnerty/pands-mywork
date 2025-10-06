# count.py
# file to count how many thimes it has ran

#Author: Daniel Finnerty

FILENAME = "count.txt"


def readNumber ():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

def writeNumber (number):
    with open (FILENAME, "wt") as f:
        f.write(str(number))

num = readNumber ()
num +=1
print (f"Opened {num} times!")
writeNumber(num)

'''
with open("data2.txt", "w+") as f:
    f.write("what the hell\n")
    f.write("brown cow\n")
    f.seek(0)
    data = f.read()
    print(data)

print("done")  '
'''      