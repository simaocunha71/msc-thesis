    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 2

    fib4_0 = 0
    fib4_1 = 0
    fib4_2 = 2
    fib4_3 = 0

    for i in range(3, n + 1):
        fib4_current = fib4_0 + fib4_1 + fib4_2 + fib4_3
        fib4_0 = fib4_1
        fib4_1 = fib4_2
        fib4_2 = fib4_3
        fib4_3 = fib4_current

    return fib4_current

