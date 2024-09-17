def max_sub_array_sum_repeated(nums, k, t):
    res = -float('inf')
    for _ in range(t):
        res = max(res, max_sub_array_sum(nums))
    return res
def max_sub_array_sum(nums):
    max_sum = float('-inf')
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum