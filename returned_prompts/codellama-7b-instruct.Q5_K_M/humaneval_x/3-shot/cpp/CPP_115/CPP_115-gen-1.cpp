    int m=grid.size();
    int n=grid[0].size();
    int i,j;
    int max_level=0;
    vector<vector<int>> level(m,vector<int>(n));
    for (i=0;i<m;i++)
    for (j=0;j<n;j++)
    if (grid[i][j]==1)
    {
        level[i][j]=1;
        max_level=1;
    }
    for (i=0;i<m;i++)
    for (j=0;j<n;j++)
    if (level[i][j]==1)
    {
        if (i>0&&grid[i-1][j]==1)
        {
            level[i-1][j]+=1;
            max_level=max(max_level,level[i-1][j]);
        }
        if (j>0&&grid[i][j-1]==1)
        {
            level[i][j-1]+=1;
            max_level=max(max_level,level[i][j-1]);
        }
        if (i<m-1&&grid[i+1][j]==1)
        {
            level[i+1][j]+=1;
            max_level=max(max_level,level[i+1][j]);
        }
        if (j<n-1&&grid[i][j+1]==1)
        {
            level[i][j+1]+=1;
            max_level=max(max_level,level[i][j+1]);
        }
    }
    int current_level=max_level;
    int count=0;
    while (current_level>capacity)
    {
        count+=1;
        for (i=0;i<m;i++)
        for (j=0;j<n;j++)
        if (level[i][j]==current_level)
        {
            level[i][j]=0;
            if (i>0&&grid[i-1][j]==