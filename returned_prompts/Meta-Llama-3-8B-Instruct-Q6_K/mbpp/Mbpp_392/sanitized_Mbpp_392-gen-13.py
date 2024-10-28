def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 1:
            return 0
        max_sum = 0
        for i in range(2, 6):
            if k % i == 0:
                max_sum = max(max_sum, f(k // i) + k)
        memo[k] = max_sum
        return max_sum
    return f(n)