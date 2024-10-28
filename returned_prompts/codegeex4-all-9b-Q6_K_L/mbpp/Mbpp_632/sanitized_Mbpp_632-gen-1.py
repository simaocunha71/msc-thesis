def move_zero(lst):
    # Filter out the zeroes and keep the order of non-zero elements
    non_zeroes = [x for x in lst if x != 0]
    # Count the number of zeroes
    num_zeroes = lst.count(0)
    # Create a new list with non-zero elements followed by the same number of zeroes
    result = non_zeroes + [0] * num_zeroes
    return result