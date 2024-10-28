    fib = [0, 1]
    i = 2
    while i < n:
        fib.append(fib[-1] + fib[-2])

        if is_prime(fib[-1]):
            i += 1

    return fib[-1]


