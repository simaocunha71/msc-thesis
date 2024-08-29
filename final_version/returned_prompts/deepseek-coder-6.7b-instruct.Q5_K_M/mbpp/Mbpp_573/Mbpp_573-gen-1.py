
def unique_product(lst):
    unique_nums = set(lst)
    product = 1
    for num in unique_nums:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# Alternate solution

def unique_product(lst):
    return eval('*'.join(str(set(lst))))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# Alternate solution

def unique_product(lst):
    return eval('*'.join(map(str, set(lst))))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# Alternate solution

from functools import reduce

def unique_product(lst):
    return reduce(lambda x, y: x*y, set(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# Alternate solution

from math import prod

def unique_product(lst):
    return prod(set(lst))

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))  # 720000000

# Alternate solution

def unique_product(lst):
    return eval('*'.join(map(str, {*lst})))

print(unique_product([10, 20, 30, 40, 20, 50