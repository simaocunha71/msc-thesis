def max_fill(grid, bucket_capacity):
    """
    :param grid: List[List[int]]
    :param bucket_capacity: int
    :return: int
    """
    # calculate the sum of the grid
    total = sum(sum(row) for row in grid)
    # calculate the maximum number of times