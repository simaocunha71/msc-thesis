def zero_count(lst):
    count = lst.count(0)
    return count / len(lst)

assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""


# 3.

