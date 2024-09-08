def max_sub_array_sum(nums, k):
    if not nums or k <= 0:
        return 0

    max_sum = float('-inf')
    current_sum = 0
    start = 0

    for end in range(len(nums)):
        current_sum += nums[end]

        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[start]
            start += 1

    return max_sum