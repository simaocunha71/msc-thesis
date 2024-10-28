
from math import fsum

def prod_signs(arr):
    if not arr:
        return None
    sign = 1
    prod = 1
    for i in arr:
        sign *= 1 if i > 0 else -1 if i < 0 else 0
        prod *= sign
    return fsum(abs(i) for i in arr) - fsum(i * sign for i in arr) + prod
