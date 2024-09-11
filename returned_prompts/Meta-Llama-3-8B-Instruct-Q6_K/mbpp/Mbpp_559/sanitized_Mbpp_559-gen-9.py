def max_sub_array_sum(nums, k):
    max_sum = float('-inf')
    window_sum = 0
    window_start = 0
    for window_end in range(len(nums)):
        window_sum += nums[window_end]
        if window_end >= k-1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[window_start]
            window_start += 1
    return max_sum