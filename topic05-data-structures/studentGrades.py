# Lab 5.4.1 Student Grades
# Program that stores a student name and lists her courses.
# Program then prints out her data.

# Author: Daniel Finnerty

'''
student = {
    "First" : {
        "Student" : "Mary",
        "Programming" : 45,
        "History" : 99
    }
}

for x, obj in student.items():
    print(x)


    for y in obj:
        print(y + ':', obj[y])
'''

# The above method is my own and not correct. See below from Andrew.

student = {
    "name" : "Mary",
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
