    def _largest_prime_factor(n):
        if n % 2 == 0:
            return 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return i
            i += 2
        return n

    while n % 2 == 0:
        n >>= 1
    return _largest_prime_factor(n)


