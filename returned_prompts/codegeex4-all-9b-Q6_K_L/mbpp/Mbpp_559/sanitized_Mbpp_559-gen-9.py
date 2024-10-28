def max_sub_array_sum(nums, k):
    max_sum = float('-inf')
    current_sum = 0
    for i in range(len(nums)):
        if i >= k:
            current_sum -= nums[i - k]
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)
    return max_sum