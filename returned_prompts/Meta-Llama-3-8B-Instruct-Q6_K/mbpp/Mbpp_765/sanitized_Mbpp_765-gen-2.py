def is_polite(n):
    polite_nums = [i*(i+1)//2 for i in range(1, n)]
    return polite_nums[n-1] + n - 1