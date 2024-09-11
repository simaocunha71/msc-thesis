def odd_num_sum(n):
    # Initialize result
    res = 0
    # Add squares of first n odd numbers
    for i in range(1, 2*n+1, 2):
        res += i**4
    return res