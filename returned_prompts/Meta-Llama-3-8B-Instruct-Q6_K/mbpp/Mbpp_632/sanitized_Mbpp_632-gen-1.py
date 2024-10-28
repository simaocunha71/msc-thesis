def move_zero(nums):
    return [i for i in nums if i != 0] + [i for i in nums if i == 0]  # O(n) time complexity