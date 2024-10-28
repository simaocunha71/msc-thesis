    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= 2
            result %= p
        n //= 2
        p *= p
        p %= 1000000007
    return result


