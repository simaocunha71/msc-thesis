def interleave_lists(list1, list2, list3):
    """
    Interleave 3 lists of the same length into a single flat list.
    """
    result = []
    i = 0
    while i < len(list1):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
        i += 1
    return result