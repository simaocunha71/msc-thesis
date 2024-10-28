import math
def zero_count(lst):
    zeros = sum(1 for x in lst if x == 0)
    non_zeros = len(lst) - zeros
    return zeros / non_zeros if non_zeros > 0 else 0