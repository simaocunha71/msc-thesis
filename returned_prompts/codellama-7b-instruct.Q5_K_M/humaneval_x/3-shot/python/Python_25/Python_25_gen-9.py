    factors = []
    while n > 1:
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                factors.append(p)
                n //= p
                break

    return factors


