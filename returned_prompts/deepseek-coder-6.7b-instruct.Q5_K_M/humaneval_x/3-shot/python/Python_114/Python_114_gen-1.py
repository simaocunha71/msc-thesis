    current_sum = 0
    min_sum = float('inf')

    for num in nums:
        current_sum += num
        min_sum = min(min_sum, current_sum)
        if current_sum > 0:
            current_sum = 0

    return min_sum


