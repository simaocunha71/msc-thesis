    int max_f=0,max_row=0,max_col=0;
    int i,j;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==1)
    {
        max_f++;
        max_row=i;
        max_col=j;
    }
    if (max_f<=capacity)
    return max_f;

    if (max_row==0)
    {
        if (grid[0][max_col]==1)
        return max_f+1;
        else
        return max_f;
    }
    if (grid[max_row][max_col-1]==1)
    return max_f+1;
    if (grid[max_row][max_col+1]==1)
    return max_f+1;
    if (grid[max_row-1][max_col]==1)
    return max_f+1;

    return max_f;
}

