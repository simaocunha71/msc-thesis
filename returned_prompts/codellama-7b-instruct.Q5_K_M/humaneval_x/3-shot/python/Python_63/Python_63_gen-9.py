    memo = {0: 0, 1: 0, 2: 1}

    def fibfib(n, memo):
        if n in memo:
            return memo[n]

        memo[n] = fibfib(n - 1, memo) + fibfib(n - 2, memo) + fibfib(n - 3, memo)
        return memo[n]

    return fibfib(n, memo)


