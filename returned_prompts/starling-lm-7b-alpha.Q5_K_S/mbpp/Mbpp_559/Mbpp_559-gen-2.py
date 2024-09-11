"""
def max_sub_array_sum(nums, k):
    if not nums:
        return 0
    max_sum = 0
    cur_sum = 0
    for i in range(len(nums)):
        if i + k > len(nums):
            break
        cur_sum += nums[i]
        if i + k == len(nums):
            max_sum = max(cur_sum, max_sum)
        elif i + k < len(nums):
            if cur_sum < 0:
                cur_sum = 0
            max_sum = max(max_sum, cur_sum)
    return max_sum

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7
"""

def max_sub_array_sum(nums, k):
    if not nums:
        return 0
    max_sum = 0
    cur_sum = 0
    for i in range(len(nums)):
        if i + k > len(nums):
            break
        cur_sum += nums[i]
        if i + k == len(nums):
            max_sum = max(cur_sum, max_sum)
        elif i + k < len(nums):
            if cur_sum < 0:
                cur_sum = 0
            max_sum = max(max_sum, cur_sum)
    return max_sum

assert max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8) == 7

def max_sub_array_sum(nums, k):
    if not nums:
        return 0
    max_sum = 0
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if i + 1 == k:
            max_sum = max(cur_sum, max_sum)
            cur_sum = 0
