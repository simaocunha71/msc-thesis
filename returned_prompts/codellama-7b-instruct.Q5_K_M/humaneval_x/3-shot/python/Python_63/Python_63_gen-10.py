    if n < 3:
        return 0

    memo = [0] * (n + 1)
    memo[0] = 0
    memo[1] = 0
    memo[2] = 1

    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

    return memo[n]


