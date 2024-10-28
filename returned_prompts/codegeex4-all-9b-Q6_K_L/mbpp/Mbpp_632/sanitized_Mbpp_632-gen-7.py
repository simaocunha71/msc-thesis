def move_zero(lst):
    # Count the number of zeroes
    count_zero = lst.count(0)
    # Remove all zeroes from the list
    lst = [x for x in lst if x != 0]
    # Add the zeroes at the end of the list
    lst.extend([0] * count_zero)
    return lst