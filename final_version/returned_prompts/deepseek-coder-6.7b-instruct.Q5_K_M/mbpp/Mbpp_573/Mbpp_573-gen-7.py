def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


# Alternatively, using python's built-in reduce function:
from functools import reduce

def unique_product(lst):
    return reduce(lambda x, y: x*y, set(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


# Alternatively, using python's built-in math library's prod function:
from math import prod

def unique_product(lst):
    return prod(set(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


# Alternatively, using numpy:
import numpy as np

def unique_product(lst):
    return np.prod(np.unique(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


# Alternatively, using pandas:
import pandas as pd

def unique_product(lst):
    return pd.Series(lst).unique().prod()

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


# Alternatively, using python's built-in reduce function with numpy:
from functools import reduce
import numpy as np

def unique_product(lst):
    return reduce(lambda x, y: x*y, np.unique(lst))

print(unique_product([10, 20, 30, 40, 2