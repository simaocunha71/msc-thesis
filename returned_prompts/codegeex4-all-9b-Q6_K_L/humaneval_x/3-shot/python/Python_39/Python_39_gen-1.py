    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    count, i = 0, 0
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1

    return fib(i - 1)


