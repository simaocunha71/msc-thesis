    int n=grid.size();
    vector<vector<int>> dp(n,vector<int>(n,0));
    vector<int> ans;
    for (int i=0;i<n;i++)
    dp[i][i]=grid[i][i];
    for (int d=1;d<k;d++)
    for (int i=0;i<n;i++)
    for (int j=0;j<n;j++)
    dp[i][j]=min(dp[i][j],dp[i][j-1]+grid[i][j]);
    for (int i=0;i<n;i++)
    for (int j=0;j<n;j++)
    for (int k=0;k<n;k++)
    ans.push_back(dp[i][j]);
    return ans;
}


