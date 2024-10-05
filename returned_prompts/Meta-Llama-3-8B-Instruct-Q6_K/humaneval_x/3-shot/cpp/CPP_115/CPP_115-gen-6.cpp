    int rows = grid.size();
    int cols = grid[0].size();
    int bucket_fill = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                bucket_fill += 1;
            }
        }
    }
    return bucket_fill / capacity;
} 
//bucket fill is the total water in all the wells
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//because if there are 15 units of water in all the wells and we can hold 3 units per bucket
//we need to lower the buckets 5 times. 
//bucket_fill/capacity is the number of times we need to lower the buckets. 
//bucket_fill is the total amount of water in all the wells. 
//capacity is the amount of water each bucket can hold.  # noqa: E501
//it is not necessary to use a loop to calculate the total water in all the wells
//because we can directly calculate it by summing all the elements in the grid
//because we can directly calculate it by summing all the elements in the grid
//we are dividing bucket fill by capacity because bucket fill is the total water in all the wells
//and bucket capacity is the amount of water each bucket can hold
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the buckets
//bucket fill / bucket capacity is the number of times we need to lower the