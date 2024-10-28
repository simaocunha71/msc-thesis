    int i,j;
    int max=0;
    int current=0;
    for (i=0;i<grid.size();i++)
        for (j=0;j<grid[i].size();j++)
        {
            if (grid[i][j]==1)
            current+=1;
            else
            {
                if (current>max)
                max=current;
                current=0;
            }
        }
        if (current>max)
        max=current;

    return max/capacity;
}

