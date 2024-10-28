def heap_sort(my_list):
    """
    Sorts the list using heap sort.
    :param my_list: list to be sorted
    :return: sorted list
    """
    if len(my_list) <= 1:
        return my_list

    # heapify the list
    for i in range(len(my_list) // 2, -1, -1):
        heapify(my_list, i, len(my_list))

    # sort the list
    for i in range(len(my_list) - 1, 0, -1):
        my_list[0], my_list[i] = my_list[i], my_list[0]
        heapify(my_list, 0, i)

    return my_list