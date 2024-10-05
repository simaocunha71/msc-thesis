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

    count = 0
    i = 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1

    return fib(i - 1)

