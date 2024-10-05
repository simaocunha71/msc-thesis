    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4_minus_4 = 0
    fib4_minus_3 = 0
    fib4_minus_2 = 2
    fib4_minus_1 = 0

    for _ in range(4, n+1):
        current = fib4_minus_1 + fib4_minus_2 + fib4_minus_3 + fib4_minus_4

        fib4_minus_4 = fib4_minus_3
        fib4_minus_3 = fib4_minus_2
        fib4_minus_2 = fib4_minus_1
        fib4_minus_1 = current

    return fib4_minus_1


