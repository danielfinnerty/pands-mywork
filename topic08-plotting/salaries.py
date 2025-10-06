# salaries.py
# program that creates 10 random salaries within a range
# Author: Daniel Finnerty

import numpy as np

minsalary = 20000
maxsalary = 80000
qty = 10

np.random.seed(1) # base salaries
salaries = np.random.randint(minsalary, maxsalary, qty)
print(salaries)

salaries_new = salaries + 5000 # salaries plus 5000 each
print(salaries_new)

salaries_increase = (salaries * 1.05) # salaries plus 5% each
print(salaries_increase)

salaries_inc_rounded = salaries_increase.astype(int) # salaries plus 5% each changed to inegers
print(salaries_inc_rounded)
