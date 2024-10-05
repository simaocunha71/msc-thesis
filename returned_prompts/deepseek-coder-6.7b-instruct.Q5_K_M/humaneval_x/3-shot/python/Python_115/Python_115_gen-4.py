    # flatten the grid to a list of wells
    wells = [well for sublist in grid for well in sublist]

    # sort the wells in descending order
    wells.sort(reverse=True)

    # initialize the number of times the buckets have to be lowered
    times = 0

    # keep lowering the buckets until all wells are emptied
    while wells:
        # lower the buckets
        times += 1

        # empty the wells until the bucket is full or all wells are emptied
        while wells and capacity:
            wells.pop()
            capacity -= 1

        # reset the bucket capacity
        capacity = len(wells)

    return times


