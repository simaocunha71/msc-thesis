    fib_cache = [0] * 5
    fib_cache[0] = 0
    fib_cache[1] = 0
    fib_cache[2] = 2
    fib_cache[3] = 0

    for i in range(4, n + 1):
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i - 2] + fib_cache[i - 3] + fib_cache[i - 4]

    return fib_cache[n]


