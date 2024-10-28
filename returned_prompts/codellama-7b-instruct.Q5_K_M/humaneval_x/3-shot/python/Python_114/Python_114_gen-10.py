    min_sum = sum(nums)
    current_sum = 0
    start = 0
    end = 0

    while end < len(nums):
        current_sum += nums[end]
        end += 1

        while current_sum > 0:
            min_sum = min(min_sum, current_sum)
            current_sum -= nums[start]
            start += 1

    return min_sum


