    int n=grid.size();
    int m=grid[0].size();
    int dp[n][m][k+1];
    int i,j,l;
    for (i=0;i<n;i++)
    for (j=0;j<m;j++)
    for (l=0;l<=k;l++)
    dp[i][j][l]=0;
    for (l=0;l<=k;l++)
    dp[0][0][l]=grid[0][0];
    for (i=1;i<n;i++)
    for (j=1;j<m;j++)
    {
        for (l=1;l<=k;l++)
        {
            if (l==1)
            dp[i][j][l]=grid[i][j];
            else
            dp[i][j][l]=min(dp[i-1][j][l-1],dp[i-1][j-1][l-1]);
        }
    }
    vector<int> result;
    for (i=0;i<n;i++)
    for (j=0;j<m;j++)
    for (l=0;l<=k;l++)
    if (dp[i][j][l]==dp[i][j][k])
    {
        result.push_back(grid[i][j]);
    }
    return result;
}


