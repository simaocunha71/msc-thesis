def divisor(n):
    count = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            count *= 2
    if n > 1:
        count *= 2
    return count