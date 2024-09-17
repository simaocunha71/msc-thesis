def catalan_number(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    catalan = 0
    for i in range(n):
        catalan += (catalan + 1) * (i + 1)
    return catalan