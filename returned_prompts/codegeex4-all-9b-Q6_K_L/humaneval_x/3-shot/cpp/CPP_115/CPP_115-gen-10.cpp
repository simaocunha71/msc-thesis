    int i,j;
    int level=0;
    int bucket=0;
    int max_level=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    level+=1;
    max_level=level;
    while (max_level>0){
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    {
        bucket+=1;
        grid[i][j]=0;
        max_level-=1;
    }
    if (bucket==capacity)
    {
    bucket=0;
    continue;
    }
    else
    {
    return bucket;
    }
    }
    return bucket;
}

