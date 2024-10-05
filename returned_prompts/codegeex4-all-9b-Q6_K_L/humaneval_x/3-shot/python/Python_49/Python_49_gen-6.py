    if n == 0:
        return 1
    if n == 1:
        return 2

    return modp(n - 1, p) * 2 % p

