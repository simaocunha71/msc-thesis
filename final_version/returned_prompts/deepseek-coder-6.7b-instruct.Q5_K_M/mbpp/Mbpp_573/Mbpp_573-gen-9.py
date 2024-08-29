def unique_product(lst):
    unique_set = set(lst)
    product = 1
    for num in unique_set:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

"""
The set data structure in Python is an unordered collection of unique elements. 
We use set() function to convert the list to a set, which automatically removes any duplicate values.
"""

# Using Python's built-in function reduce() and lambda functions

from functools import reduce

def unique_product(lst):
    unique_set = set(lst)
    return reduce(lambda x, y: x * y, unique_set)

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

"""
The reduce() function applies a binary function (in this case, a lambda function that multiplies two numbers) 
to all items of an iterable in a cumulative way. The binary function takes two arguments. 
It is a function of two arguments that takes two values at a time and returns one value.
"""

# Using list comprehension

def unique_product(lst):
    return eval('*'.join(str(x) for x in set(lst)))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

"""
Here, we're converting the set back to a list, joining the elements of the list with '*' 
and then evaluating the expression to find the product.
"""

# Using operator module

from operator import mul
from functools import reduce

def unique_product(lst):
    return reduce(mul, set(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

"""
The operator module in Python provides functions