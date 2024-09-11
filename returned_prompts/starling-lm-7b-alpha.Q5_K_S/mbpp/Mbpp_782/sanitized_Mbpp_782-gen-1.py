def odd_length_sum(nums):
    n = len(nums)
    res = 0
    for mask in range(1<<n):
        curr = 0
        for j in range(n):
            if (mask & (1 << j)) != 0:
                curr += nums[j]
        res += curr if curr%2 else -curr
    return res