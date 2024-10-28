from functools import reduce
from operator import mul
def unique_product(lst):
    return reduce(mul, set(lst))