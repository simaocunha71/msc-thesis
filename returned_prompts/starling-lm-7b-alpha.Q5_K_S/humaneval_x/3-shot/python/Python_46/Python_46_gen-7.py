    fib_seq = [0, 0, 2] + [None] * (n - 3)

    for i in range(3, n + 1):
        fib_seq[i] = fib_seq[i - 1] + fib_seq[i - 2] + fib_seq[i - 3] + fib_seq[i - 4]

    return fib_seq[n]


