    int i,j;
    int bucket=0;

    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    bucket+=1;

    return bucket/capacity;
}

