    fib4_cache = [0, 0, 2, 0]

    if n < 4:
        return fib4_cache[n]

    for i in range(4, n + 1):
        fib4_cache.append(fib4_cache[i-1] + fib4_cache[i-2] + fib4_cache[i-3] + fib4_cache[i-4])

    return fib4_cache[n]

