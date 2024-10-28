def get_max_sum(n):
    memo = {1: 1}
    for i in range(2, n + 1):
        memo[i] = max((memo.get(i // 2, 0) + memo.get(i // 3, 0) + memo.get(i // 4, 0) + memo.get(i // 5, 0)), i)
    return memo[n]