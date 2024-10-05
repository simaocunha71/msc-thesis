    fib4_cache = {0: 0, 1: 0, 2: 2}

    def fib4(n):
        if n not in fib4_cache:
            fib4_cache[n] = fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4)
        return fib4_cache[n]

    return fib4(n)


