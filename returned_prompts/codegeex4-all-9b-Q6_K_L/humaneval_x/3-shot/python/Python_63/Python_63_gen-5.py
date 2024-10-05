    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    fibfib_n_minus_1 = 0
    fibfib_n_minus_2 = 0
    fibfib_n_minus_3 = 1

    for i in range(3, n + 1):
        current_fibfib = fibfib_n_minus_1 + fibfib_n_minus_2 + fibfib_n_minus_3
        fibfib_n_minus_3 = fibfib_n_minus_2
        fibfib_n_minus_2 = fibfib_n_minus_1
        fibfib_n_minus_1 = current_fibfib

    return fibfib_n_minus_1

