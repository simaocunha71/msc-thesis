
def maxAverageOfPath(arr):
    n = len(arr)
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = arr[i][i]
    for i in range(n-1):
        for j in range(i+1, n):
            dp[i][j] = max(arr[i][j], dp[i+1][j], dp[i][j-1])
    return sum(dp[0][-1])/float(n)


