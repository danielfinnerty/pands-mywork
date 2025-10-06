'''
aBook = {"title":"the order of phoenix", "author":"JK", "what":"well"}
for key, value in aBook.items():
    print ( key, "has a value of", value)
'''

'''
x , y, z = (1, 2, 3)
print (x, y, z, sep="\n")
print (x, y, z)
'''

'''
def topower(number, power=3):
        return (number ** power)

pwr = (2)
num = (9)
ans = topower(num) # long winded way
print (f"with we got {ans}")
print (f"Second check {topower(10)}")
print (f"Number {num} is {topower(num, pwr)}")
'''

'''
def yo(a):
    return a * 2

var = yo(4)
print (f"Lets see {yo(3)}")
print (var)'

'''

'''
def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
    
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # I am not doing error handling
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        # now read the next module name
        moduleName = input("\tEnter next module name (blank to quit) :").strip()

    return modules
def displayModules(modules):
    print ("\tName   \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

print (f"well {readModules()}")'
'''

with open("test-d.txt", "w") as f:
    data = f.write("test d\n") # returns the number of chars written
    print (data)

with open("test-d.txt", "a") as f2: # open file again
    data = f2.write("another line") # returns the number of chars written
    print (data)

