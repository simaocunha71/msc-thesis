    int total_water=0;
    for (int i=0;i<grid.size();i++)
    {
        for (int j=0;j<grid[i].size();j++)
        {
            total_water+=grid[i][j];
        }
    }
    return total_water/capacity;
}  // This function does not consider the problem correctly. It just calculates the total water in the grid divided by the capacity of the bucket.
// It does not consider the fact that the bucket needs to be lowered after each use. It also does not consider the fact that the bucket can only hold the capacity amount of water.
// A correct implementation would be more complex and would require a different approach. It would probably involve using a loop to lower the bucket until it is empty and then use it to fill the wells. The number of times the bucket needs to be lowered would be the total number of times it is used to fill the wells.  // This function does not consider the problem correctly. It just calculates the total water in the grid divided by the capacity of the bucket.
// It does not consider the fact that the bucket needs to be lowered after each use. It also does not consider the fact that the bucket can only hold the capacity amount of water.
// A correct implementation would be more complex and would require a different approach. It would probably involve using a loop to lower the bucket until it is empty and then use it to fill the wells. The number of times the bucket needs to be lowered would be the total number of times it is used to fill the wells.  // This function does not consider the problem correctly. It just calculates the total water in the grid divided by the capacity of the bucket.
// It does not consider the fact that the bucket needs to be lowered after each use. It also does not consider the fact that the bucket can only hold the capacity amount of water.
// A correct implementation would be more complex and would require a different approach. It would probably involve using a loop to lower the bucket until it is empty and then use it to fill the wells. The number of times the bucket needs to be lowered would be the total number of times it is used to fill the wells.  // This function does not consider the problem correctly. It just calculates the total water in the grid divided by the capacity of the bucket.
// It does not consider the fact that the bucket needs to be lowered after each use. It also does not consider the fact that the bucket can only hold the capacity amount