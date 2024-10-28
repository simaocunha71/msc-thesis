def sort_sublists(lists):
    """
    Arguments:
        lists -- a list of lists
    Returns:
        a list of sorted sublists
    """
    for sublist in lists:
        sublist.sort()
    return lists