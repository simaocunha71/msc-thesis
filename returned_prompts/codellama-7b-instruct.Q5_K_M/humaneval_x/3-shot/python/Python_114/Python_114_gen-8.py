    # O(n) time, O(1) space
    curr_sum = 0
    min_sum = float('inf')
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        elif curr_sum > min_sum:
            curr_sum = 0

    return min_sum
