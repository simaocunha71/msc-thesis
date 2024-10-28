    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    fib_0 = 0
    fib_1 = 0
    fib_2 = 2
    fib_3 = 0

    for i in range(4, n + 1):
        fib_n = fib_0 + fib_1 + fib_2 + fib_3
        fib_0 = fib_1
        fib_1 = fib_2
        fib_2 = fib_3
        fib_3 = fib_n

    return fib_n

