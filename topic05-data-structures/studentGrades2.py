# Lab 5.4.1 Student Grades 2
# Program that students name and grades are entered.
# this is then stored and lists the details when requested.

# Author: Daniel Finnerty
'''
courseNames = []
grades = []

nameInput = input("Students name? ")

courseName = input("Enter course: ")
while courseName != "":
    courseNames.append(courseName)

grade = input("Enter grade: ")
while grade != "":
    grades.append(grade)

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

'''
'''
student = {
    "name" : nameInput,
    "modules" : [
        {
            "courseName" : "Programming",
            "grade" : 45
        },
        {
            "courseName" : "History",
            "grade" : 99
        },
    ]
}

print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))

'''
    
'''
numbers = []

# first number then we check if it is 0 in the while loop
number = int(input("enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print (f"The average is {average}")

'''