    int i,j,k;
    int grid_size=grid.size();
    int row_size=grid[0].size();
    int total_water=0;
    int total_fills=0;
    vector<vector<int>> used(grid_size,vector<int>(row_size,0));
    for (i=0;i<grid_size;i++)
    {
        for (j=0;j<row_size;j++)
        {
            if (used[i][j]==1)
                continue;
            total_fills+=1;
            int water_to_extract=(grid[i][j]/capacity)*capacity;
            for (k=0;k<water_to_extract/capacity;k++)
            {
                total_water+=capacity;
                grid[i][j]=grid[i][j]%capacity;
                used[i][j]=1;
                if (i+1<grid_size)
                {
                    if (grid[i+1][j]>0)
                    {
                        grid[i+1][j]-=capacity;
                        used[i+1][j]=1;
                    }
                }
                if (j+1<row_size)
                {
                    if (grid[i][j+1]>0)
                    {
                        grid[i][j+1]-=capacity;
                        used[i][j+1]=1;
                    }
                }
            }
            if (grid[i][j]>0)
                total_water+=grid[i][j];
        }
    }
    return total_fills;
}




