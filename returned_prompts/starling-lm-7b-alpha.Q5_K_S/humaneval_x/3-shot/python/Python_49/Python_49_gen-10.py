    if n == 0:
        return 1
    elif n % 2 == 0:
        return modp(n // 2, p) ** 2 % p
    else:
        return modp(n - 1, p) * modp(n, p) % p


