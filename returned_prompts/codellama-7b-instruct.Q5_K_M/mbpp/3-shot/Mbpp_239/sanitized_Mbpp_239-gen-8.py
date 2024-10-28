def get_total_number_of_sequences(m, n):
    dp = [1] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, i):
            if 2 * j <= m:
                dp[i] += dp[j - 1]
    return dp[n]