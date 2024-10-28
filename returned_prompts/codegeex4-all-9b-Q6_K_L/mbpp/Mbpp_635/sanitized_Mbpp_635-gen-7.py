def heap_sort(lst):
    """
    Sorts a list using the heap sort algorithm.

    :param lst: List to be sorted.
    :return: Sorted list.
    """
    # Build a max heap from the input data.
    for i in range(len(lst) // 2 - 1, -1, -1):
        heapify(lst, i, len(lst))

    # One by one extract elements from heap
    for i in range(len(lst) - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]  # swap
        heapify(lst, 0, i)

    return lst