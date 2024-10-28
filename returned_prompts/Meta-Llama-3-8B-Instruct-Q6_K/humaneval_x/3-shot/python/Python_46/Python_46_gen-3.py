    if n < 0:
        raise ValueError("n must be a positive integer")

    fib4_sequence = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_sequence.append(fib4_sequence[i - 1] + fib4_sequence[i - 2] + fib4_sequence[i - 3] + fib4_sequence[i - 4])

    return fib4_sequence[n]  # or fib4_sequence[-1] for Python 3.8+
    # Note: If you're using Python 3.8+, you can directly return fib4_sequence[-1] as the last element of the list. Otherwise, you need to return fib4_sequence[n].