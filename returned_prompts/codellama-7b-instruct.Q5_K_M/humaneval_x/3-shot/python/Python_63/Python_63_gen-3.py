    memo = {0: 0, 1: 0, 2: 1}

    def fibfib_helper(n):
        if n in memo:
            return memo[n]

        result = fibfib_helper(n - 1) + fibfib_helper(n - 2) + fibfib_helper(n - 3)
        memo[n] = result
        return result

    return fibfib_helper(n)


