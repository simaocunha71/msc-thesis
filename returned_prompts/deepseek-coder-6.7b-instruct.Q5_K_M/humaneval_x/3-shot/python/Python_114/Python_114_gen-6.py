    current_min = nums[0]
    min_sum = nums[0]

    for num in nums[1:]:
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    return min_sum


