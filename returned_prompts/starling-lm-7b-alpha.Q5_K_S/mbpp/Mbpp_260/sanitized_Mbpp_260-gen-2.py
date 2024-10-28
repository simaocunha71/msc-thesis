def newman_prime(n):
    if n == 0:
        return 2
    elif n == 1:
        return 3
    else:
        a = 2
        b = 3
        while n > 1:
            a, b = (b**2 + a**2) % n, b
            n -= 1
        return b