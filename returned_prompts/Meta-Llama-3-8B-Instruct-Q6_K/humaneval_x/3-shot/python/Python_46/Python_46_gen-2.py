    if n < 1:
        return 0

    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])

    return fib4_sequence[n]


