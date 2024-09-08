def zero_count(lst):
    zero_num = lst.count(0)
    non_zero_num = len(lst) - zero_num
    return zero_num / non_zero_num

assert math.isclose(zero_count([0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]), 0.181818, rel_tol=0.001)
"""

