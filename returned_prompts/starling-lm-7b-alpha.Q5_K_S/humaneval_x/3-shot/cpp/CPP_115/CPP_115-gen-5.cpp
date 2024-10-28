    int i,j;
    int all_water=0;
    int water_left;
    int count_fill=0;
    int bucket_size;
    while (all_water<grid.size()*grid[0].size())
    {
        bucket_size=capacity;
        for (i=0;i<grid.size();i++)
        for (j=0;j<grid[i].size();j++)
        if (grid[i][j]==1)
        {
            water_left=bucket_size-grid[i][j];
            if (water_left>=0)
            {
                grid[i][j]=0;
                bucket_size-=water_left;
                all_water+=water_left;
            }
            else
            {
                grid[i][j]=grid[i][j]-water_left;
                all_water+=water_left;
            }
        }
        count_fill+=1;
    }
    return count_fill;
}








































































































































































































































































