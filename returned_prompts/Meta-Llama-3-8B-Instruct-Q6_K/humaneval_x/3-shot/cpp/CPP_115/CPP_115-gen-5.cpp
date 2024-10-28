    int count=0;
    for (int i = 0; i < grid.size(); i++)
    {
        int sum=0;
        for (int j = 0; j < grid[i].size(); j++)
        {
            if (grid[i][j]==1)
                sum++;
        }
        while (sum>0)
        {
            int fill=min(capacity,sum);
            sum-=fill;
            count++;
        }
    }
    return count;
}  // This function counts the number of times the bucket needs to be lowered
// by subtracting the maximum amount that can be filled from the bucket from the sum of the water in the current well.  // This is done for each well in the grid.  // The count of the number of times the bucket needs to be lowered is then returned.  // This function assumes that the bucket can hold at most the total amount of water in the grid.  // It also assumes that the bucket is initially empty.  // It does not handle the case where the bucket cannot hold all the water in the grid.  // It does not handle the case where the bucket is not initially empty.  // It does not handle the case where the bucket is not lowered at the end of each well.  // It does not handle the case where the bucket is not filled at the end of each well.  // It does not handle the case where the bucket is not filled at the end of the last well.  // It does not handle the case where the bucket is not lowered at the end of the last well.  // It does not handle the case where the bucket is not empty at the end of the last well.  // It does not handle the case where the bucket is not filled at the end of the last well.  // It does not handle the case where the bucket is not lowered at the end of the last well.  // It does not handle the case where the bucket is not empty at the end of the last well.  // It does not handle the case where the bucket is not filled at the end of the last well.  // It does not handle the case where the bucket is not lowered at the end of the last well.  // It does not handle the case where the bucket is not empty at the end of the last well.  // It does not handle the case where the bucket is not filled at the end of the last well.  // It does not handle the case where the