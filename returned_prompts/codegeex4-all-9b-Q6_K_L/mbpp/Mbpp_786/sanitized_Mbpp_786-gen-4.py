def right_insertion(lst, value):
    """
    Locate the right insertion point for a specified value in sorted order.
    """
    if not lst:
        return 0
    if value > lst[-1]:
        return len(lst)
    for i, x in enumerate(lst):
        if x > value:
            return i
    return len(lst)