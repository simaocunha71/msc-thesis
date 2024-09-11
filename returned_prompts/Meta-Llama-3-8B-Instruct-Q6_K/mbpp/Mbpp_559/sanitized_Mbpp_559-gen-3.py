def max_sub_array_sum(nums, k):
    if len(nums) < k:
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return max_sum