    curr_sum = nums[0]
    min_sum = curr_sum
    start = 0
    end = 0

    while end < len(nums):
        curr_sum += nums[end]
        while curr_sum > 0 and curr_sum > min_sum:
            curr_sum -= nums[start]
            start += 1
        min_sum = min(min_sum, curr_sum)
        end += 1

    return min_sum


