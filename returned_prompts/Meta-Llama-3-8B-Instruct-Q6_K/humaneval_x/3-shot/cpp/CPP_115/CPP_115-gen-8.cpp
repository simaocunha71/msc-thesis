    int total=0;
    int i,j;
    for (i=0;i<grid.size();i++)
    {
        for (j=0;j<grid[i].size();j++)
        {
            if (grid[i][j]==1)
                total++;
        }
    }
    return total/capacity;
}