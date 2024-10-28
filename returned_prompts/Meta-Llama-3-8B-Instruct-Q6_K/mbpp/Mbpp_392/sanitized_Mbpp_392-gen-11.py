def get_max_sum(n):
    memo = {1: 1}
    def f(n):
        if n in memo:
            return memo[n]
        if n % 60 == 0:
            memo[n] = max(f(n//2) + f(n//3) + f(n//4) + f(n//5), n)
        else:
            memo[n] = max(f(n//2), f(n//3), f(n//4), f(n//5), n)
        return memo[n]
    return f(n)