    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    fibfib_0 = 0
    fibfib_1 = 0
    fibfib_2 = 1

    for i in range(3, n + 1):
        fibfib_current = fibfib_0 + fibfib_1 + fibfib_2
        fibfib_0 = fibfib_1
        fibfib_1 = fibfib_2
        fibfib_2 = fibfib_current

    return fibfib_current

