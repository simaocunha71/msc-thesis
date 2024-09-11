def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k in [2,3,4,5]:
            memo[k] = k
        else:
            memo[k] = max(sum(f(k//i) for i in [2,3,4,5] if k%i==0), k)
        return memo[k]
    return f(n) if n > 1 else 0