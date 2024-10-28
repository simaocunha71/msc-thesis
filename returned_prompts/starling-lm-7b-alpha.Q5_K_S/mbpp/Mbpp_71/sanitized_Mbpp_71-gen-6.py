def comb_sort(lst):
    """
    Implementation of comb_sort algorithm.

    Parameters:
        lst (list): A list of elements to be sorted.

    Returns:
        list: The sorted list of elements.
    """
    # Set the initial gap and the sorting flag
    gap = len(lst)
    sorting = True

    # Combine sort algorithm
    while sorting:
        sorting = False
        gap = gap * 10 // 13
        for i in range(len(lst) - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                sorting = True

    return lst