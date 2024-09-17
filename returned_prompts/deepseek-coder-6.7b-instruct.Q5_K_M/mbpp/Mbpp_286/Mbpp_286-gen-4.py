
from functools import reduce
from operator import mul

def max_product(lst):
    lst.sort()
    return max(reduce(mul, lst[-3:]), reduce(mul, lst[:2]+lst[-1:]))


