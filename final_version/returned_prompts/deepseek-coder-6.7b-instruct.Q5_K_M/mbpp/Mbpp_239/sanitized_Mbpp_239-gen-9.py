def get_total_number_of_sequences(m, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if 2 * j <= m:
                dp[i] += dp[j]
    return sum(dp) - dp[0]