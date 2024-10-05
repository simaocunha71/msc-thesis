    int i,j;
    int sum=0;
    for (i=0;i<grid.size();i++)
    {
        for (j=0;j<grid[i].size();j++)
        {
            sum+=grid[i][j];
        }
    }
    if (sum>capacity)
    return sum/capacity;

    return 0;
}

