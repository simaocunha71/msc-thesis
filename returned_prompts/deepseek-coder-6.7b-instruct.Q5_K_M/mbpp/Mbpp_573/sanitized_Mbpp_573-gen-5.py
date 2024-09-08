import numpy
def unique_product(lst):
    unique = set(lst)
    product = 1
    for num in unique:
        product *= num
    return product