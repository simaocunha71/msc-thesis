from typing import List
from math import isclose
def zero_count(nums: List[int]) -> float:
    zero_count = 0
    non_zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            non_zero_count += 1
    return zero_count / non_zero_count if non_zero_count != 0 else 0