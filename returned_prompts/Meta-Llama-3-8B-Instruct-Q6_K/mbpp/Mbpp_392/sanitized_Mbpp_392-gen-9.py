def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        else:
            if k % 2 == 0:
                memo[k] = max(f(k//2), f(k//3), f(k//4), f(k//5)) + k
            else:
                memo[k] = f(k-1) + k
            return memo[k]
    return f(n) - n