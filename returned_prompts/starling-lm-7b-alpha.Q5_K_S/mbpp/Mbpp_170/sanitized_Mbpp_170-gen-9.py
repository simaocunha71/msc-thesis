def sum_range_list(lst, start, end):
    # initialize sum
    sum = 0
    # loop through the list
    for i in range(start, end + 1):
        # add the value of each element to the sum
        sum += lst[i]
    # return the sum
    return sum