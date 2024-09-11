from math import log
from collections import Counter

def max_Product(arr):
    if len(arr) == 0:
        return None
    c = Counter(arr)
    max_p = max(c.items(), key=lambda x: x[1])
    if max_p[1] == 1:
        return (max(arr), max(arr))
    else:
        return (max_p[0], arr.index(max(c.items(), key=lambda x: x[1])[0]) if c[max_p[0]] > 2 else min(arr))

#def max_Product(arr):
#    if len(arr) == 0:
#        return None
#    max_p = max(arr)
#    min_p = min(arr)
#    if arr.count(max_p) == 1:
#        return (max(arr), min(arr))
#    elif arr.count(min_p) == 1:
#        return (min(arr), max(arr))
#    else:
#        return (max_p, arr.index(max_p))


# Alternative solution
def max_Product_alt(arr):
    if len(arr) == 0:
        return None
    max_p = max(arr)
    min_p = min(arr)
    if arr.count(max_p) == 1:
        return (max(arr), min(arr))
    elif arr.count(min_p) == 1:
        return (min(arr), max(arr))
    else:
        return (max_p, arr.index(max_p))

# Test
def test():
    import random
    import time
    seed = 123456789
    for _ in range(100000):
        arr = [random.randint(0, 100000000) for _ in range(random.randint(1, 100))]
        print(arr)
        res1 = max_Product(arr)
        res2 = max_Product_alt(arr)