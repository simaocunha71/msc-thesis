def Find_Min_Length(L):
    # Initialize Min Length
    min_length = len(L[0])

    # Iterate through L
    for l in L:
        # If length of l is smaller than min_length
        if len(l) < min_length:
            # Update min_length
            min_length = len(l)

    # Return min_length
    return min_length