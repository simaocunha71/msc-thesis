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