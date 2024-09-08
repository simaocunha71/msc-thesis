def swap_List(lst):
    """Swap the first and last elements in a list."""
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst