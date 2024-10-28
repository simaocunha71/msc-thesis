    if n < 3:
        return n

    fibfib_n = fibfib(n - 2) + fibfib(n - 3) + fibfib(n - 4)

    return fibfib_n


