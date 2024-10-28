    res = float('inf')
    curr = 0
    for i in nums:
        curr += i
        if res > curr:
            res = curr
        if curr < 0:
            curr = 0
    return res


