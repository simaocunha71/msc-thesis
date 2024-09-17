def lps(s): 
    X = s[::-1] 
    n = len(s) 
    dp = [[0 for x in range(n+1)] for x in range(n+1)] 
    for i in range(n+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                dp[i][j] = 0
            elif s[i-1] == X[j-1]: 
                dp[i][j] = dp[i-1][j-1]+1
            else: 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    return dp[n][n]