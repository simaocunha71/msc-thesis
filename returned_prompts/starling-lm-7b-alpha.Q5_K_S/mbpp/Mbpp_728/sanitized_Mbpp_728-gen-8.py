def sum_list(list1, list2):
    """
    Returns the sum of each pair of elements in two lists.

    >>> sum_list([10,20,30],[15,25,35])
    [25,45,65]
    """
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result