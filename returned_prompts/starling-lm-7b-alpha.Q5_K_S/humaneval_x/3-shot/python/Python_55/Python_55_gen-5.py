    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        fib_n_minus_2, fib_n_minus_1 = 1, 2
        for _ in range(2, n):
            fib_n_minus_2, fib_n_minus_1 = fib_n_minus_1, fib_n_minus_2 + fib_n_minus_1
        return fib_n_minus_2


