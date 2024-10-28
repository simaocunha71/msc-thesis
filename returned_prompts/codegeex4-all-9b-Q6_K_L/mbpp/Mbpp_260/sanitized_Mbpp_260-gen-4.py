def newman_prime(n):
    def newman_sequence():
        a, b, c = 1, 1, 1
        while True:
            yield a
            a, b, c = b, c, a + b + c

    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

    return next(x for i, x in enumerate(newman_sequence()) if is_prime(x) and i == n)