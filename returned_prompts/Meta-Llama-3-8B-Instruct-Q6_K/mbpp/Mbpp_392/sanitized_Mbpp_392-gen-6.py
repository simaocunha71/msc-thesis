def get_max_sum(n):
    memo = {}
    def f(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        res = max((f(n//2) + f(n//3) + f(n//4) + f(n//5)) for r in range(2, 6) if n//r >= 1)
        memo[n] = res + n
        return res + n
    return f(n) - n