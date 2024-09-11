def is_octagonal(n):
    octagonal_nums = [(8*k**3 - 13*k**2 + 7*k) for k in range(1, n+1)]
    return octagonal_nums[n-1]