    if n < 0:
        raise ValueError("n must be a non-negative integer")

    fib4_values = [0, 0, 2, 0]
    for i in range(4, n + 1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])

    return fib4_values[n]  # fib4_values[n] is the nth element of the sequence


