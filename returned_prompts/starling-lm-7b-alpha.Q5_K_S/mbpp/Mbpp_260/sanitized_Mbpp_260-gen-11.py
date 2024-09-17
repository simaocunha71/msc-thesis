def newman_prime(n):
    mod = 2 ** n - 1
    mod += 1

    def f(x, c):
        return pow(x, c, mod)

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = 2
    c = 2
    while not is_prime(f(x, c)):
        c += 1

    return f(x, c)