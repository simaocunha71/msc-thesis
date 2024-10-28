    if n < 3:
        return [0, 0, 1][n]

    fib = [0, 0, 1]
    for _ in range(3, n+1):
        fib.append(fib[-1] + fib[-2] + fib[-3])

    return fib[-1]


