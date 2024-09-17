def max_sub_array_sum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums or k <= 0:
        return 0

    # Sliding window solution
    window_sum, max_sum, start = 0, 0, 0
    for i in range(len(nums)):
        window_sum += nums[i]
        while window_sum > k:
            window_sum -= nums[start]
            start += 1
        max_sum = max(max_sum, window_sum)
    return max_sum