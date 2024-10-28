    int i,j,k,min_f,max_f;
    min_f=min_fill(grid,capacity);
    max_f=max_fill(grid,capacity);
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    for (k=min_f;k<=max_f;k++)
    if (k==grid[i][j])
    return 1+wells(grid,capacity-k);
    return 0;
}


