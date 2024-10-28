import math
def zero_count(arr):
    zero_count = sum(1 for x in arr if x == 0)
    non_zero_count = sum(1 for x in arr if x != 0)
    return zero_count / non_zero_count