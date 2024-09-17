def max_sum(arr):
    n = len(arr)
    
    # Initialize a table to store the maximum sum of bitonic subsequences ending at each position
    dp = [[0] * n for _ in range(n)]
    
    # Fill the table in a bottom-up manner
    for i in range(n):
        dp[i][i] = arr[i]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i][k] + arr[k + 1] - arr[k] for k in range(i, j))
    
    # The maximum sum of a bitonic subsequence is the maximum sum of a bitonic subsequence ending at any position
    return max(max(row) for row in dp)