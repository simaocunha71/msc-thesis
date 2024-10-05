    fib_cache = [0, 0, 2] + [None] * (n + 1)

    for i in range(3, n + 1):
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2] + fib_cache[i - 3] + fib_cache[i - 4]

    return fib_cache[n]


