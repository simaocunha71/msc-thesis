def move_zero(lst):
    # Create two lists, one for non-zero values and one for zero values
    non_zero = [i for i in lst if i != 0]
    zero = [i for i in lst if i == 0]
    # Combine the two lists and return the result
    return non_zero + zero