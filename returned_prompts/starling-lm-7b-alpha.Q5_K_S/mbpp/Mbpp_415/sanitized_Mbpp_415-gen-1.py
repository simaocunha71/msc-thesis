from functools import reduce
def max_Product(arr):
    return reduce(lambda x,y: max(x,y) if x*y > 0 else min(x,y), arr)