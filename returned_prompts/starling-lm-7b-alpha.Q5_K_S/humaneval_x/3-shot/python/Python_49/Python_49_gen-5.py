    if n == 0:
        return 1 % p
    if n % 2 == 0:
        return modp(n // 2, p) ** 2 % p
    return modp(n - 1, p) * modp(n, p) % p


