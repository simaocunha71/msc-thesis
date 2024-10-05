    int i,j,k;
    vector<int> row_sums;
    for (i=0;i<grid.size();i++)
    {
        int sum=0;
        for (j=0;j<grid[i].size();j++)
        {
            sum+=grid[i][j];
        }
        row_sums.push_back(sum);
    }
    int total_water=0;
    for (i=0;i<row_sums.size();i++)
    {
        total_water+=row_sums[i];
    }
    int filled_wells=total_water/capacity;
    if (total_water%capacity!=0)
    filled_wells+=1;

    vector<vector<int>> temp_grid=grid;
    for (i=0;i<filled_wells;i++)
    {
        for (j=0;j<grid.size();j++)
        {
            for (k=0;k<grid[j].size();k++)
            {
                if (grid[j][k]>0)
                {
                    grid[j][k]-=1;
                    temp_grid[j][k]+=capacity;
                }
            }
        }
    }
    int total_water_again=0;
    for (i=0;i<row_sums.size();i++)
    {
        total_water_again+=row_sums[i];
    }
    int filled_wells_again=total_water_again/capacity;
    if (total_water_again%capacity!=0)
    filled_wells_again+=1;
    return filled_wells_again;
}



