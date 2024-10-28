import math
def unique_product(lst):
    return prod(set(lst))
def prod(iterable):
    result = 1
    for value in iterable:
        result *= value
    return result