    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    i = 1
    while True:
        f = fib(i)
        if is_prime(f):
            n -= 1
            if n == 0:
                return f
        i += 1


