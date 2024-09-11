def get_max_sum(n):
    memo = {1: 1}
    def f(x):
        if x not in memo:
            if x % 60 == 0:
                memo[x] = x
            else:
                memo[x] = max(f(x//2) + f(x//3) + f(x//4) + f(x//5), x)
        return memo[x]
    return f(n) - n