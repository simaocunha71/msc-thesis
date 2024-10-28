    int i,j,k,l;
    int grid_size=grid.size();
    int grid_length=grid[0].size();
    int total_water=0;
    for (i=0;i<grid_size;i++)
    for (j=0;j<grid_length;j++)
    total_water+=grid[i][j];

    int times=total_water/capacity;
    int remain=total_water-capacity*times;
    for (k=0;k<times;k++)
    {
    for (i=0;i<grid_size;i++)
    for (j=0;j<grid_length;j++)
    {
        grid[i][j]=min(grid[i][j]-capacity,0);
    }
    }

    for (k=0;k<remain;k++)
    {
    for (l=0;l<grid_size;l++)
    for (i=0;i<grid_length;i++)
    {
        grid[l][i]=min(grid[l][i]-1,0);
    }
    }
    return times;
}


