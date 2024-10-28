from collections import Counter
def zero_count(nums):
    zero_count = Counter(nums).get(0, 0)
    non_zero_count = len(nums) - zero_count
    return zero_count / non_zero_count if non_zero_count else 1