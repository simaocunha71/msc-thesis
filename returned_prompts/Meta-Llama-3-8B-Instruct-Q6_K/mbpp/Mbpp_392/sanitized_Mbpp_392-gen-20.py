def get_max_sum(n):
    memo = {1: 1}
    for i in range(2, n+1):
        if i in memo:
            continue
        max_sum = float('-inf')
        for j in [2, 3, 4, 5]:
            if i % j == 0:
                max_sum = max(max_sum, get_max_sum(i//j) + i)
        memo[i] = max_sum
    return memo[n]