    if n == 0:
        return 1
    if p == 1:
        return 0
    if n % 2 == 0:
        half = Modp(n/2, p)
        return (half * half) % p
    else:
        return (n * Modp(n-1, p)) % p

