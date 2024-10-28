import math
def zero_count(lst):
    zero_count = lst.count(0)
    non_zero_count = len(lst) - zero_count
    return zero_count / non_zero_count if non_zero_count != 0 else 0