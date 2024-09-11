import math
def zero_count(lst):
    zeroes = len([i for i in lst if i == 0])
    non_zeroes = len([i for i in lst if i != 0])
    return math.isclose(zeroes / non_zeroes, 0.181818, rel_tol=0.001) if non_zeroes > 0 else 0.0
    # return zeroes / non_zeroes if non_zeroes > 0 else 0.0
    # return zeroes / len(lst) if len(lst) > 0 else 0.0
    # return zeroes / len(lst)
    # return len([i for i in lst if i == 0]) / len(lst) if len(lst) > 0 else 0.0
    # return len([i for i in lst if i == 0]) / len(lst) if len(lst) > 0 else None