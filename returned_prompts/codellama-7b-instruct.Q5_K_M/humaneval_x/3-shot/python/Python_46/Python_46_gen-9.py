    fib4_memo = [0, 0, 2, 0]

    def fib4(n):
        if n < 4:
            return fib4_memo[n]

        fib4_memo.append(fib4(n - 1) + fib4(n - 2) + fib4(n - 3) + fib4(n - 4))

        return fib4_memo[n]
