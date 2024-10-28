    int i,j,k;
    int rows=grid.size();
    int cols=grid[0].size();
    int total_water=0;
    int total_times=0;
    while (true)
    {
        int water_in_current_bucket=0;
        for (i=0;i<rows;i++)
        for (j=0;j<cols;j++)
        {
            if (grid[i][j]!=0){
                water_in_current_bucket+=grid[i][j];
            }
        }
        if (water_in_current_bucket==0)
        {
        return total_times;
        }
        for (i=0;i<rows;i++)
        for (j=0;j<cols;j++)
        {
            if (grid[i][j]!=0){
            grid[i][j]=0;
            }
        }
        total_water+=water_in_current_bucket;
        total_times+=water_in_current_bucket/capacity;
        water_in_current_bucket=water_in_current_bucket%capacity;
        if (water_in_current_bucket==0)
        {
        return total_times;
        }
    }
}


