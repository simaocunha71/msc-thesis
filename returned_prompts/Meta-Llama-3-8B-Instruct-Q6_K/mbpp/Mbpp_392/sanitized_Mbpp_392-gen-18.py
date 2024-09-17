def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            memo[k] = k
        else:
            memo[k] = max(k, sum(f(k//i) for i in range(2, 6)) if k % 60 == 0 else float('-inf'))
        return memo[k]
    return f(n)