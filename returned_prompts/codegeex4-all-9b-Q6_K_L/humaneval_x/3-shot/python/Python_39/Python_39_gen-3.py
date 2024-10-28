    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    for i in range(2, n + 1):
        if is_prime(fib[i]):
            return fib[i]

