from operator import mul
from itertools import product, starmap
from functools import reduce
def large_product(list1, list2, num):
    """
    Find the largest products from two given lists, selecting one factor from each list
    """
    return list(reduce(max, starmap(mul, product(list1, list2)))[:num])