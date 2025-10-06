# Lab 5.2.1 Tuple
# Program to tell user summer months
# Author: Daniel Finnerty


months = ("jan",
            "feb",
            "mar",
            "apr",
            "may",
            "jun",
            "jul", 
            "aug", 
            "sept", 
            "oct", 
            "nov", 
            "dec")

summer = months[4:7]

for month in summer:
    print(month)



# Below is how Andrew does it.
'''
months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "july",
          "August",
          "September",
          "October",
          "November",
          "December"
          )
summer = months[4:7]
for month in summer:
    print(month)
'''