    product = 1
    while n:
        d = n % 10
        if d % 2 != 0:
            product *= d
        n //= 10
    return product


