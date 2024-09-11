import math
def zero_count(lst):
    zeroes = sum(1 for x in lst if x == 0)
    non_zeroes = len(lst) - zeroes
    return math.isclose(zeroes / non_zeroes, 0) if non_zeroes > 0 else 0.0