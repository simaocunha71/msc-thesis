def max_sum(nums: list) -> int:
    n = len(nums)
    if n == 0:
        return 0
    elif n == 1:
        return nums[0]
    else:
        inc = [0] * n
        dec = [0] * n
        inc[0] = nums[0]
        dec[n-1] = nums[n-1]
        for i in range(1, n):
            inc[i] = max(inc[i-1], nums[i])
        for i in range(n-2, -1, -1):
            dec[i] = max(dec[i+1], nums[i])
        max_sum = 0
        for i in range(n-1):
            max_sum = max(max_sum, inc[i] + dec[i+1])
        max_sum = max(max_sum, inc[n-1])
        return max_sum