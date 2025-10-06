
import json
FILENAME = "testdict.txt"
sample = dict (name = "fred", age = 31, grades = [1, 34, 55])

def writeDict (obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

writeDict(sample)

def readDict ():
    with open (FILENAME) as f:
        return json.load(f)
    
somedict = readDict()
print(somedict)