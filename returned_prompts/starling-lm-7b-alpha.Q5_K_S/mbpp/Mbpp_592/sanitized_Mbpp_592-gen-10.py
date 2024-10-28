def sum_Of_product(n):
    # Initialize result
    res = 0
    # Take the first two terms of the series
    res = res + 1
    # Consider remaining terms one by one
    for i in range(2,n+1):
        res = res + (i*(i-1))
    return res