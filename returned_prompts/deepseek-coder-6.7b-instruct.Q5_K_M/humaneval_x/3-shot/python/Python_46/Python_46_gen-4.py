    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0

    fib4_n_minus_1 = 0
    fib4_n_minus_2 = 0
    fib4_n_minus_3 = 2
    fib4_n_minus_4 = 0

    for _ in range(4, n+1):
        fib4_n = fib4_n_minus_1 + fib4_n_minus_2 + fib4_n_minus_3 + fib4_n_minus_4

        fib4_n_minus_4 = fib4_n_minus_3
        fib4_n_minus_3 = fib4_n_minus_2
        fib4_n_minus_2 = fib4_n_minus_1
        fib4_n_minus_1 = fib4_n

    return fib4_n



