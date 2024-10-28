def sum_Of_product(n):
    # Initialize result
    res = 0
    # Take n+1 consecutive terms
    # and multiply them
    for i in range(n + 1):
        res += (i * (n - i))
    return res