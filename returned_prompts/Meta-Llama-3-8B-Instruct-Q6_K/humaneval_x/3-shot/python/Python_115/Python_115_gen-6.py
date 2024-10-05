    # Get the total number of buckets needed
    total_buckets = math.ceil(sum(sum(row) for row in grid) / capacity)

    # Initialize the result
    result = 0

    # Iterate over the grid
    for row in grid:
        # Calculate the remaining water in the current row
        remaining_water = sum(row)

        # Calculate how many buckets are needed to empty the current row
        buckets_needed = math.ceil(remaining_water / capacity)

        # Add the buckets needed to the result
        result += buckets_needed

    # Return the result
    return int(result)


