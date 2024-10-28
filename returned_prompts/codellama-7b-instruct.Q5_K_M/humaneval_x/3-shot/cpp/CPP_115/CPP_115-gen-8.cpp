    int max_fill_value=0;
    int current_fill_value=0;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[0].size();j++)
    if (grid[i][j]==1)
    {
        if (current_fill_value==0)
        max_fill_value++;
        current_fill_value++;
        if (current_fill_value==capacity)
        current_fill_value=0;
    }

    return max_fill_value;
}


