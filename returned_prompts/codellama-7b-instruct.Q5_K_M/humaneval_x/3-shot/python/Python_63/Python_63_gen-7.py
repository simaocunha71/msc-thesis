    memo = {0: 0, 1: 0, 2: 1}

    def fib(n):
        if n in memo:
            return memo[n]
        else:
            result = fib(n - 1) + fib(n - 2) + fib(n - 3)
            memo[n] = result
            return result

    return fib(n)


