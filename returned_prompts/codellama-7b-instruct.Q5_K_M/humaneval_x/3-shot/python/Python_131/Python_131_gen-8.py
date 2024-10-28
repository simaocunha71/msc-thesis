    if n < 0:
        raise ValueError('n should be positive')

    result = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            result *= digit

        n //= 10

    return result
