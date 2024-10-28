
    s = float('inf')
    for i in range(len(nums)):
        cur = 0
        for j in range(i, len(nums)):
            cur += nums[j]
            if cur < s:
                s = cur
    return s
