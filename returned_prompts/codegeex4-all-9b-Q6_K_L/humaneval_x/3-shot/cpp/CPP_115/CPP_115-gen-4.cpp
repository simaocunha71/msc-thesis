    int i,j;
    int count=0;
    int max=0;
    int maxj=0;
    for (i=0;i<grid.size();i++)
    {
        for (j=0;j<grid[i].size();j++)
        {
            if (grid[i][j]==1)
            {
                max+=1;
                maxj=j;
            }
        }
        if (max>=capacity)
        {
            max=0;
            count+=1;
        }
    }
    return count;
}

