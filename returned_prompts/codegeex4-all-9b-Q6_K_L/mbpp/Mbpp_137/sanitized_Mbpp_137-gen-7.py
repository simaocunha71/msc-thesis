import math
def zero_count(arr):
    zero_count = sum(1 for x in arr if x == 0)
    non_zero_count = len(arr) - zero_count
    return zero_count / non_zero_count if non_zero_count else 0