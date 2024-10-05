    int i,j;
    int rows=grid.size();
    int cols=grid[0].size();
    int max_water=0;
    int water_in_row=0;
    int water_in_col=0;
    for (i=0;i<rows;i++)
    for (j=0;j<cols;j++)
    if (grid[i][j]==1){
        water_in_row++;
        water_in_col++;
    }
    for (i=0;i<rows;i++)
    for (j=0;j<cols;j++)
    if (grid[i][j]==1){
        if (i>0 && grid[i-1][j]==1)
        water_in_row--;
        if (j>0 && grid[i][j-1]==1)
        water_in_col--;
        if (i<rows-1 && grid[i+1][j]==1)
        water_in_row--;
        if (j<cols-1 && grid[i][j+1]==1)
        water_in_col--;
        max_water=max(max_water,water_in_row*capacity+water_in_col*capacity);
        water_in_row=0;
        water_in_col=0;
    }
    return max_water;
}



