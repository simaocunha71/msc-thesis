    memo = {0: 0, 1: 0, 2: 1}

    def fibfib(n):
        if n not in memo:
            memo[n] = fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)
        return memo[n]

    return fibfib(n)


