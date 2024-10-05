    int max_water=0;
    int row=0;
    int col=0;
    int i;
    int j;
    int level=0;
    int size=grid.size();
    vector<vector<int>>visited(size,vector<int>(size,0));
    for (i=0;i<size;i++)
    for (j=0;j<size;j++)
    if (grid[i][j]==1 && visited[i][j]==0)
    {
        row=i;
        col=j;
        break;
    }
    if (row==0 && col==0)
    return max_water;
    level=1;
    while (level>0)
    {
        for (i=row-1;i>=0;i--)
        if (grid[i][col]==1 && visited[i][col]==0)
        {
            visited[i][col]=1;
            grid[i][col]=0;
            level+=1;
            row=i;
            break;
        }
        for (j=col-1;j>=0;j--)
        if (grid[row][j]==1 && visited[row][j]==0)
        {
            visited[row][j]=1;
            grid[row][j]=0;
            level+=1;
            col=j;
            break;
        }
        for (i=row+1;i<size;i++)
        if (grid[i][col]==1 && visited[i][col]==0)
        {
            visited[i][col]=1;
            grid[i][col]=0;
            level+=1;
            row=i;
            break;
        }
        for (j=col+1;j<size;j++)
        if (grid[row][j]==1 && visited[row][j]==0)
        {
            visited[row][j]=1;
            grid[row][j]=0;
            level+=1;
            col=j;
            break;
        }
    }
    for (i=0;i<