def get_max_sum(n):
    memo = {1: 1}
    def f(k):
        if k in memo:
            return memo[k]
        if k < 2:
            return k
        max_sum = k
        for i in range(2, 6):
            if i * (i + 1) // 2 > k:
                break
            if i > 1 and k % i == 0:
                max_sum = max(max_sum, f(k // i) + k)
        memo[k] = max_sum
        return max_sum
    return f(n)