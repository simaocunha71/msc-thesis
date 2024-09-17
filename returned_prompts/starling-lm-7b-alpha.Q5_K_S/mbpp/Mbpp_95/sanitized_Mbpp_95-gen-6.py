def Find_Min_Length(L):
    """Returns the length of the smallest list in a list of lists."""
    # Initialize the length of the smallest list
    min_length = len(L[0])
    # Iterate through all the lists in the list of lists
    for l in L:
        # If the length of the current list is smaller than min_length
        if len(l) < min_length:
            # Assign the length of the current list to min_length
            min_length = len(l)
    # Return the length of the smallest list
    return min_length