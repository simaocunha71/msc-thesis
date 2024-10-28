    i = 3
    while i * i <= n:
        if n % i == 0:
            n = n // i
            i = 2
        else:
            i += 2
    return n


