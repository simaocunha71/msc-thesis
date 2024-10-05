    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        if fib_sequence[-1] > 10 ** 6:
            break
        if all(fib_sequence[-1] % i != 0 for i in fib_sequence[:-1]):
            fib_sequence.pop()
    else:
        return fib_sequence[-1]

    return fib_sequence[-2]


