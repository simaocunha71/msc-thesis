def swap_List(lst):
    # Create a copy of the list
    lst_copy = lst[:]
    # Swap the first and last elements
    lst_copy[0], lst_copy[-1] = lst_copy[-1], lst_copy[0]
    # Return the modified list
    return lst_copy