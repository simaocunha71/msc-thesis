    def fib4(n):
        if n < 0:
            raise ValueError("n must be nonnegative")
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 2
        if n == 3:
            return 0
        prev_prev = 0
        prev = 0
        current = 2
        for _ in range(4, n + 1):
            current = prev_prev + prev + current
            prev_prev = prev
            prev = current
        return current


