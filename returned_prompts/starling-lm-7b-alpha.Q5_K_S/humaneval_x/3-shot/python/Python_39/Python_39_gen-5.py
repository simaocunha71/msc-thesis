    fib = [2, 3]  # First two Fibonacci numbers are prime
    while len(fib) < n:
        fib_next = fib[-1] + fib[-2]
        if all(fib_next % i != 0 for i in fib):
            fib.append(fib_next)
    return fib[-1]


