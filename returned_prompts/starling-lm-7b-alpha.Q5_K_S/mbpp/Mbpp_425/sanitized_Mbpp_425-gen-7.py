def count_element_in_list(input_list, element):
    """
    Count the number of sublists containing a particular element
    """
    return sum(1 for sublist in input_list for _ in sublist if _ == element)