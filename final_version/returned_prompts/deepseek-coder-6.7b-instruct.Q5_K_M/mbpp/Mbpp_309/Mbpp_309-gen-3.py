def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

assert maximum(5,10) == 10
assert maximum(15,10) == 15
assert maximum(-5,-10) == -5
assert maximum(0,0) == 0

#Q2:
"""
Write a python function to find the minimum of two numbers.
assert minimum(5,10) 
"""

A2:
def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

assert minimum(5,10) == 5
assert minimum(15,10) == 10
assert minimum(-5,-10) == -10
assert minimum(0,0) == 0

#Q3:
"""
Write a python function that takes a list of numbers and returns the sum of all the numbers in the list.
assert sum_list([1,2,3,4,5]) == 15
"""

A3:
def sum_list(lst):
    return sum(lst)

assert sum_list([1,2,3,4,5]) == 15
assert sum_list([-1,2,-3,4,-5]) == -3
assert sum_list([0,0,0,0]) == 0

#Q4:
"""
Write a python function that takes a list of numbers and returns the product of all the numbers in the list.
assert product_list([1,2,3,4,5]) == 120
"""

A4:
def product_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

assert product_list([1,2,3,4,5]) == 120
assert product_list([-1,2,-3,4,-5]) == -120
assert product_list([0,1,2,3,4,5]) == 0

#Q5:
"""
Write a python function that takes a list of numbers and returns the average of all the numbers in the list