
from math import floor, log10
def zero_count(arr):
    non_zeroes = 0
    for i in arr:
        if i != 0:
            non_zeroes += 1

    zeroes = len(arr) - non_zeroes
    return zeroes / non_zeroes


