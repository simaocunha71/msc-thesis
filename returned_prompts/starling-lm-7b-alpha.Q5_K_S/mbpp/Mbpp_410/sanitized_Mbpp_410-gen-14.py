def min_val(nums):
    return min(nums, key=lambda x: (type(x), x))