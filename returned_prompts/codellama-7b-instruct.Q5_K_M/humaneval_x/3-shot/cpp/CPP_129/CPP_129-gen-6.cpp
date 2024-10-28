    vector<int> res;
    res.clear();
    int n=grid.size();
    int m=grid[0].size();
    int dp[n][m];
    for (int i=0;i<n;i++)
    for (int j=0;j<m;j++)
    dp[i][j]=grid[i][j];
    
    for (int i=0;i<n;i++)
    for (int j=0;j<m;j++)
    {
        if (i>0)
        dp[i][j]=min(dp[i][j],dp[i-1][j]+dp[i][j]);
        
        if (j>0)
        dp[i][j]=min(dp[i][j],dp[i][j-1]+dp[i][j]);
        
        if (i<n-1)
        dp[i][j]=min(dp[i][j],dp[i+1][j]+dp[i][j]);
        
        if (j<m-1)
        dp[i][j]=min(dp[i][j],dp[i][j+1]+dp[i][j]);
    }
    
    for (int i=0;i<n;i++)
    for (int j=0;j<m;j++)
    {
        if (dp[i][j]<=k)
        res.push_back(grid[i][j]);
    }
    
    return res;
}

