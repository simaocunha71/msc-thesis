def is_polite(n):
    count = 0
    while n > 0:
        count += 1
        if n % 10 == 0:
            n //= 10
        else:
            n = n // 100 + n % 10
    return count == 4