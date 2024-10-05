    int min_val=min_fill(grid,capacity),max_val=max_fill(grid,capacity),i,j,max_wells=0,min_wells=0,curr_wells=0;
    for (i=0;i<grid.size();i++)
    for (j=0;j<grid[i].size();j++)
    if (grid[i][j]==min_val)
    min_wells+=1;
    else if (grid[i][j]==max_val)
    max_wells+=1;
    if (min_wells>0)
    curr_wells=min_wells;
    else
    curr_wells=max_wells;
    if (curr_wells<=capacity)
    return curr_wells;
    if (max_wells>0)
    return max_wells;
    return max_wells;
}


