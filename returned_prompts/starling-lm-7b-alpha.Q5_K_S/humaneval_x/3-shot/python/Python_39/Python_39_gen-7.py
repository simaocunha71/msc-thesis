    fib_seq = [0, 1]
    while True:
        next_fib = fib_seq[-1] + fib_seq[-2]
        if is_prime(next_fib):
            if next_fib == fib_seq[n]:
                return next_fib
            else:
                fib_seq.append(next_fib)


