from collections import Counter
from math import isclose
def zero_count(nums):
    count = Counter(nums)
    return count[0] / len(nums)