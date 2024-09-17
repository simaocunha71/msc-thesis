
def get_total_number_of_sequences(m: int, n: int) -> int:
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        dp[1][i] = 1
    for i in range(2, n+1):
        for j in range(1, m+1):
            for k in range(1, j):
                dp[i][j] += dp[i-1][k]
    return sum(dp[n])

