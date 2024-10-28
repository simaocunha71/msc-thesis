    # find the longest length of the wells
    wells_length = len(grid[0])
    # find the number of wells
    number_of_wells = len(grid)

    # count the number of times we need to lower the bucket
    number_of_times = 0

    # get the index of the longest well
    longest_well_index = 0

    # get the length of the longest well
    longest_well_length = 0

    # get the largest length of the wells
    for i in range(number_of_wells):
        if len(grid[i]) > longest_well_length:
            longest_well_length = len(grid[i])
            longest_well_index = i

    # if we have a horizontal well we need to lower the bucket once
    if longest_well_length == wells_length:
        number_of_times += 1

    # otherwise we need to lower the bucket for the number of wells - 1
    else:
        number_of_times += number_of_wells - 1

    # return the number of times we need to lower the bucket
    return number_of_times


