def search(lst):
    """
    Find the element that appears only once in a sorted array.
    """
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        return lst[1]
    if len(lst) == 3:
        if lst[0] == lst[1]:
            return lst[2]
        elif lst[1] == lst[2]:
            return lst[0]
    for i in range(len(lst) - 2):
        if lst[i] != lst[i + 1]:
            if lst[i + 1] == lst[i + 2]:
                return lst[i + 1]
    return lst[-1]