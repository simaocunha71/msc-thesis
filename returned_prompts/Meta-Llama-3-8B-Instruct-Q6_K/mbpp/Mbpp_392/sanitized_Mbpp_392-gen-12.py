def get_max_sum(n):
    memo = {1: 1}
    def f(n):
        if n in memo:
            return memo[n]
        if n < 1:
            return 0
        max_sum = n
        for i in range(2, 6):
            if i * i <= n:
                max_sum = max(max_sum, f(n // i) + 1)
        memo[n] = max_sum
        return max_sum
    return f(n)