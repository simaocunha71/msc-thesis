    int m=grid.size();
    int n=grid[0].size();
    int i,j,i_min,j_min;
    int min_val,val;
    vector<vector<int>> dp(m, vector<int>(n,-1));
    vector<vector<bool>> visited(m, vector<bool>(n,false));
    vector<int> ret;
    for (i=0;i<m;i++)
    for (j=0;j<n;j++)
    dp[i][j]=INT_MAX;
    dp[0][0]=0;
    visited[0][0]=true;
    ret.push_back(grid[0][0]);
    for (i=0;i<k;i++)
    {
        min_val=INT_MAX;
        i_min=-1;
        j_min=-1;
        for (i=0;i<m;i++)
        for (j=0;j<n;j++)
        if (visited[i][j]==false && dp[i][j]<min_val)
        {
            min_val=dp[i][j];
            i_min=i;
            j_min=j;
        }
        visited[i_min][j_min]=true;
        val=grid[i_min][j_min];
        ret.push_back(val);
        if (i_min>0)
        dp[i_min-1][j_min]=min(dp[i_min-1][j_min],dp[i_min][j_min]+val);
        if (i_min<m-1)
        dp[i_min+1][j_min]=min(dp[i_min+1][j_min],dp[i_min][j_min]+val);
        if (j_min>0)
        dp[i_min][j_min-1]=min(dp[i_min][j_min-1],dp[i_min][j_min]+val);
        if (j_min<n-1)
        dp[i_min