    res = float("inf")
    start, end = 0, 0
    curr_sum = 0
    while end < len(nums):
        curr_sum += nums[end]
        while curr_sum > 0 and start < end:
            curr_sum -= nums[start]
            start += 1
        res = min(res, curr_sum)
        end += 1
    return res if res != float("inf") else 0


