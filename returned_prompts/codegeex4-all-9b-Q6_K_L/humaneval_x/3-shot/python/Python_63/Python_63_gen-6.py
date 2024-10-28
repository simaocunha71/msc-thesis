    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1

    for _ in range(n - 2):
        fibfib_n = fibfib_0 + fibfib_1 + fibfib_2
        fibfib_0 = fibfib_1
        fibfib_1 = fibfib_2
        fibfib_2 = fibfib_n

    return fibfib_n

