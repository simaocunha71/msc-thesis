    min_sum = float('inf')
    running_sum = 0

    for num in nums:
        running_sum += num
        min_sum = min(min_sum, running_sum)
        if running_sum > 0:
            running_sum = 0

    return min_sum


