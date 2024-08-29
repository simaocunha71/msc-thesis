from functools import reduce
from operator import mul
from functools import reduce
def unique_product(lst):
    unique_set = set(lst)
    product = 1
    for num in unique_set:
        product *= num
    return product