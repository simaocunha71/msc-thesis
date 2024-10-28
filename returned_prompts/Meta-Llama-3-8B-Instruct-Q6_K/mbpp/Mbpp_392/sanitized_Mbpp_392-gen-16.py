def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 4:
            memo[k] = k
            return memo[k]
        else:
            memo[k] = max(sum(f(i) for i in (k//2, k//3, k//4, k//5)) if i in memo else f(i) for i in (k//2, k//3, k//4, k//5)) + 1
            return memo[k]
    return f(n)