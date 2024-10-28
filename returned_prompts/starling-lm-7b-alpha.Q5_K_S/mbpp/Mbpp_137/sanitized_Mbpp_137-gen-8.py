from math import isclose
def zero_count(nums):
    zero_count = 0
    for num in nums:
        if num == 0:
            zero_count += 1
    return zero_count / len(nums)