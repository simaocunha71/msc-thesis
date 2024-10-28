from collections import Counter
import math
def zero_count(arr):
    count = Counter(arr)
    zeroes = count[0]
    non_zeroes = len(arr) - zeroes
    return math.isclose(zeroes / non_zeroes, 0.181818, rel_tol=0.001)
    # return zeroes / non_zeroes
    # return round(zeroes / non_zeroes, 3) if non_zeroes > 0 else 0.0