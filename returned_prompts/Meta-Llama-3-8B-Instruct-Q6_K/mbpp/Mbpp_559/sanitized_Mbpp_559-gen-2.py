def max_sub_array_sum(nums, k):
    if k > len(nums):
        return 0
    max_sum = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum = current_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum