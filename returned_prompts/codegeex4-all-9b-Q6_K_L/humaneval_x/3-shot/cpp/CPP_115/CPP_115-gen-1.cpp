    int rows=grid.size();
    int cols=grid[0].size();
    int count=0;
    int i,j;
    for (i=0;i<rows;i++)
    {
        for (j=0;j<cols;j++)
        {
            if (grid[i][j]==1)
            {
                if (capacity>0)
                {
                    grid[i][j]=0;
                    capacity-=1;
                }
                else
                {
                    count+=1;
                    capacity=grid[i][j];
                    grid[i][j]=0;
                }
            }
        }
    }
    return count;
}

