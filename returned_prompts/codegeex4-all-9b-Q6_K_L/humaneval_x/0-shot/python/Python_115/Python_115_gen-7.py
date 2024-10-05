def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """

    # Initialize the number of times we need to lower the buckets
    num_buckets = 0

    # Loop through each well in the grid
    for well in grid:
        # Initialize the number of times we need to lower the bucket for this well
        num_buckets_for_well = 0

        # Loop through each unit of water in the well
        for water in well:
            # If the water is present (represented by 1), we need to lower the bucket
            if water == 1:
                num_buckets_for_well += 1

        # Update the total number of times we need to lower the buckets
        num_buckets += math.ceil(num_buckets_for_well / capacity)

    return num_buckets