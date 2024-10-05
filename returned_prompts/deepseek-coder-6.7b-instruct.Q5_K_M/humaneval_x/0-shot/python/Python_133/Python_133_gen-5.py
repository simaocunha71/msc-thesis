

def sum_squares(lst):
    import math
    return sum([math.ceil(i)**2 for i in lst])


print(sum_squares([1.4, 4.2, 0]))  # 29
print(sum_squares([1, 2, 3]))  # 14
print(sum_squares([1, 4, 9]))  # 98
print(sum_squares([1, 3, 5, 7]))  # 84
print(sum_squares([-2.4, 1, 1]))  # 6


Explanation:

The function sum_squares takes in a list of numbers. It uses list comprehension to iterate over each number in the list, rounding each number to the nearest integer using the math.ceil function. It then squares each number and adds them together using the sum function. It finally returns the total sum.


This function works by first importing the math module which allows us to use the math.ceil function for rounding numbers. It then uses a list comprehension to iterate over each number in the list, rounding each number to the nearest integer using the math.ceil function. It then squares each number and adds them together using the sum function. Finally, it returns the total sum.


The function sum_squares is then tested with several examples to ensure it is working correctly.


The function sum_squares is then tested with several examples to ensure it is working correctly.
'''

# 2.

'''
