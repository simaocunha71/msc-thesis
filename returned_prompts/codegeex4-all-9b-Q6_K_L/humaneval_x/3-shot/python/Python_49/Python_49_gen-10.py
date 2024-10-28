    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        p = (p * p) % p
    return result

