    fib = [0, 1]
    for i in range(2, 10**6):
        fib.append(fib[-1] + fib[-2])
        if fib[-1] % 2 != 0 and len(list(filter(lambda x: fib[-1] % x == 0, fib[:-1]))) == 0:
            return fib.index(fib[-1]) + 1


