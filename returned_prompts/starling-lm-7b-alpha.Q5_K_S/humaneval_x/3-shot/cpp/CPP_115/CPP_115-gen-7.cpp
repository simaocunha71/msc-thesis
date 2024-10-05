    int i,j,k,l;
    int n=grid.size();
    int m=grid[0].size();
    int filled_times=0;
    int water_left=0;

    while(1)
    {
        water_left=0;
        for (i=0;i<n;i++)
        for (j=0;j<m;j++)
        if (grid[i][j]==1)
        water_left+=1;

        if (water_left==0)
        return filled_times;

        for (i=0;i<n;i++)
        for (j=0;j<m;j++)
        if (grid[i][j]==1)
        {
            grid[i][j]=0;
            water_left-=1;
        }

        if (water_left>capacity)
        {
            filled_times+=1;
            water_left=capacity;
        }
        else
        filled_times+=water_left/capacity;
    }
}


