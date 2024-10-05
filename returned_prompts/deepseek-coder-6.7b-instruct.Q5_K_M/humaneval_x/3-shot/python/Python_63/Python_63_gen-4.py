    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1

    fibfib_n_minus_3 = 0
    fibfib_n_minus_2 = 0
    fibfib_n_minus_1 = 1

    for _ in range(3, n+1):
        fibfib_n = fibfib_n_minus_1 + fibfib_n_minus_2 + fibfib_n_minus_3
        fibfib_n_minus_3 = fibfib_n_minus_2
        fibfib_n_minus_2 = fibfib_n_minus_1
        fibfib_n_minus_1 = fibfib_n

    return fibfib_n


