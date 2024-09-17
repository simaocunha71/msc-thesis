def max_occurrences(nums):
    return max(set(nums), key = nums.count)