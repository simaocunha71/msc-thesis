def get_total_number_of_sequences(m: int, n: int) -> int:
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(1, m+1):
        for j in range(n, 0, -1):
            dp[j] += dp[j-1]
    return dp[n]