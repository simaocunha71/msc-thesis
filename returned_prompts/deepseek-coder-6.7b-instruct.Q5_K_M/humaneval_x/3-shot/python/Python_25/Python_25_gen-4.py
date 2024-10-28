    factors = []
    def add_factor(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
    add_factor(n)
    if n > 1:
        factors.append(n)
    return factors


