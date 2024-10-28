    result = 0
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        result = min(result, current_sum)
        if current_sum < 0:
            current_sum = 0
        for j in range(i+1, len(nums)):
            current_sum += nums[j]
            result = min(result, current_sum)
            if current_sum < 0:
                current_sum = 0
    return result


