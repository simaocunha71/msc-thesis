    product = 1
    while n > 0:
        d = n % 10
        if d % 2 == 1:
            product *= d
        n = n // 10
    return product


