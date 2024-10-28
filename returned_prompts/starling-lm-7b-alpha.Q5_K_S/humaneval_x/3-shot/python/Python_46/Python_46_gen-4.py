    fib_sequence = [0, 0, 2] + [None] * (n - 3)

    for i in range(3, n + 1):
        fib_sequence[i] = fib_sequence[i - 1] + fib_sequence[i - 2] + fib_sequence[i - 3] + fib_sequence[i - 4]

    return fib_sequence[n]


