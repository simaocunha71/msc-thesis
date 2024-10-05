    int total_water=0;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    total_water++;
    return total_water/capacity;
} //this is not correct, need to consider the bucket capacity, and also need to consider the case when the capacity is greater than the total water.
