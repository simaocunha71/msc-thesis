def Diff(list1, list2):
    """
    Returns the difference between two lists, i.e. the elements in the first list that are not in the second.
    """
    return [i for i in list1 if i not in list2]