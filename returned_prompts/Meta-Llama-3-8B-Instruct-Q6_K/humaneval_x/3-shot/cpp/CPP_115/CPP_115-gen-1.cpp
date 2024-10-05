    int rows=grid.size();
    int cols=grid[0].size();
    int count=0;
    for (int i=0;i<rows;i++)
    {
        int water_in_well=0;
        for (int j=0;j<cols;j++)
        {
            if (grid[i][j]==1)
            {
                water_in_well+=1;
            }
        }
        int bucket_fill=water_in_well;
        while (bucket_fill>0)
        {
            bucket_fill=min(bucket_fill,capacity);
            water_in_well-=bucket_fill;
            count+=1;
            bucket_fill=0;
        }
    }
    return count;
}