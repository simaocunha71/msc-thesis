def bell_Number(n):
    ncr = [1, 1] + [0 for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            ncr[j] += ncr[j - 1]
    return ncr[n]