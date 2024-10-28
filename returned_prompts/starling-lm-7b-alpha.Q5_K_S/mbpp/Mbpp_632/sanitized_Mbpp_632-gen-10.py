def move_zero(lst):
    # create an empty list to store the zeroes
    zeroes = []
    # create an empty list to store the non-zeroes
    non_zeroes = []
    # loop through the list
    for elem in lst:
        # if the element is zero, append it to the zeroes list
        if elem == 0:
            zeroes.append(elem)
        # otherwise, append it to the non-zeroes list
        else:
            non_zeroes.append(elem)
    # concatenate the zeroes and non-zeroes lists
    return non_zeroes + zeroes