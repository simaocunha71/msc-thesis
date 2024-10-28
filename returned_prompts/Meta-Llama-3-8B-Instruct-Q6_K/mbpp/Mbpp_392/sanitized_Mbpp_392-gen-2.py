def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k <= 5:
            memo[k] = k
        else:
            memo[k] = max(f(k//2) + f(k//3) + f(k//4) + f(k//5), k)
        return memo[k]
    return f(n)  # get_max_sum(60) == 106