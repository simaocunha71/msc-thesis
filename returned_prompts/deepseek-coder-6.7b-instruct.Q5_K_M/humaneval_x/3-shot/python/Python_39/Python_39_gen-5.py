    def is_prime(n):
        if n < 2: return False
        if n == 2 or n == 3: return True
        if n % 2 == 0 or n % 3 == 0: return False
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0: return False
            i += w
            w = 6 - w
        return True

    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    count = 0
    i = 1
    while count < n:
        if is_prime(fib(i)):
            count += 1
        i += 1
    return fib(i - 1)


