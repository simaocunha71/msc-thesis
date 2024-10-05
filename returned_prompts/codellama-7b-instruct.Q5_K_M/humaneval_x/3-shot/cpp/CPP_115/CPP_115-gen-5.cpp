    int i,j,result;
    int max_row_water=0,max_col_water=0;
    int row_water=0,col_water=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    {
        row_water+=1;
        if (row_water>max_row_water)
        max_row_water=row_water;
    }
    else
    row_water=0;
    row_water=0;
    for (j=0;j<grid[0].size();j++)
    for (i=0;i<grid.size();i++)
    if (grid[i][j]==1)
    {
        col_water+=1;
        if (col_water>max_col_water)
        max_col_water=col_water;
    }
    else
    col_water=0;

    if (max_row_water>max_col_water)
    result=max_row_water;
    else
    result=max_col_water;

    if (result>capacity)
    result=capacity;
    else
    result=result;
    return result;
}


