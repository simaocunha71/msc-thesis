    fib = [0, 0, 2, 0]

    while len(fib) < n + 1:
        fib.append(sum(fib[-4:]))

    return fib[n]


