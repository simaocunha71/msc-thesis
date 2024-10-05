    def fibfib(n):
        if n == 0 or n == 1 or n == 2:
            return 0
        else:
            return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)

    return fibfib(n)


