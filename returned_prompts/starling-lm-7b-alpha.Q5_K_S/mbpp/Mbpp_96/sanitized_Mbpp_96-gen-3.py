def divisor(n):
    i = 1
    while i * i <= n:
        if (n % i == 0):
            if (n / i == i):
                return 1 + 1
            else:
                return 2 + 1
        i += 1
    return 1