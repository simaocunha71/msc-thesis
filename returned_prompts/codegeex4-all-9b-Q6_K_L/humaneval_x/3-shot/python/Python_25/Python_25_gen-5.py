    factors = []
    while n > 1:
        factor = 2
        while n % factor != 0:
            factor += 1
        factors.append(factor)
        n //= factor

    return factors


