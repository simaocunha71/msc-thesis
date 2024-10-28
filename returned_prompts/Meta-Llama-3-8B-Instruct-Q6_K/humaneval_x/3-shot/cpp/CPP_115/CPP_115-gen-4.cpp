    int total=0;
    int max_fill=0;
    for (int i=0;i<grid.size();i++)
    {
        for (int j=0;j<grid[i].size();j++)
        {
            if (grid[i][j]==1)
            {
                total++;
            }
        }
    }
    int fill=total/capacity;
    total%=capacity;
    while (total>0)
    {
        fill++;
        total-=capacity;
    }
    return fill;
}