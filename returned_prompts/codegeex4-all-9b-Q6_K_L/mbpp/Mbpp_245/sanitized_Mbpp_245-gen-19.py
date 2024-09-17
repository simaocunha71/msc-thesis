def max_sum(nums: list) -> int:
    n = len(nums)
    incl = [0]*n
    excl = [0]*n

    incl[0] = nums[0]
    for i in range(1, n):
        incl[i] = nums[i] + (excl[i-1] if i-2 < 0 else max(excl[i-1], incl[i-2]))
        excl[i] = max(incl[i-1], excl[i-1])
    return max(incl[-1], excl[-1])