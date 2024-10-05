    fib_seq = [0, 0, 2]
    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2] + fib_seq[-3] + fib_seq[-4])

    return fib_seq[n]


