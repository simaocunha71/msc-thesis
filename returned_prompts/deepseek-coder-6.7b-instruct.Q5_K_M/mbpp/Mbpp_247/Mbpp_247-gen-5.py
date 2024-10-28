
def lps(s): 
    X = s[::-1] 
    dp = [[0]*(len(X)+1) for _ in range(len(s)+1)] 
    for i in range(len(s)+1): 
        for j in range(len(X)+1): 
            if i == 0 or j == 0: 
                dp[i][j] = 0
            elif s[i-1] == X[j-1]: 
                dp[i][j] = dp[i-1][j-1]+1
            else: 
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) 
    return dp[-1][-1] 


