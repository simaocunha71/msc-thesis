def Diff(list1, list2):
    return list(set(list1) - set(list2))
    # or return [i for i in list1 if i not in list2]
    # or return [i for i in list1 + list2 if (i in list1 and i not in list2) or (i in list2 and i not in list1)]