"""
def get_lucid(n):
    res = []
    for i in range(1, n + 1):
        temp = i
        while temp <= n:
            if temp in res:
                break
            res.append(temp)
            temp *= 2
    return res
"""

import math

def get_lucid(n):
    sq = int(math.sqrt(n))
    res = []
    for i in range(1, sq + 1):
        if i in res:
            continue
        temp = i
        while temp <= n:
            if temp in res:
                break
            res.append(temp)
            temp *= 2
    return res

print(get_lucid(10))


"""
