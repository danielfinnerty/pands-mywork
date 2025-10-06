# plotting.py
# program to practice plots
# Author: Daniel Finnerty

import numpy as np
import matplotlib.pyplot as plt


# Question 5
np.random.seed(1)
x_points = np.array(range(0, 101))
y_points = x_points ** 2

plt.plot(x_points, y_points)
'''
plt.show()
'''

# Question 6

minsalary = 20000
maxsalary = 80000
qty = 100

np.random.seed(1) # base salaries
salaries = np.random.randint(minsalary, maxsalary, qty)

plt.hist(salaries)
'''
plt.show()
'''

# Question 7

np.random.seed(1)
ages = np.random.randint(21, 66, qty)
print(salaries)
print(ages)

plt.scatter(ages, salaries, color = 'r')
plt.plot(x_points, y_points, color = 'b')
plt.legend()
plt.xlabel ("age")
plt.ylabel ("salaries")
plt.title ("random")
plt.xlim(20, 100)
'''
plt.show()
'''
plt.savefig("prettier-plot.png")