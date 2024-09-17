from functools import reduce
def unique_product(lst):
    product = reduce(lambda x, y: x * y, sorted(set(lst)))
    return product