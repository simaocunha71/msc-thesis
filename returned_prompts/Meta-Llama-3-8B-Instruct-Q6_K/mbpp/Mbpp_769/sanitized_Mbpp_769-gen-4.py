def Diff(list1, list2):
    list1 = list(set(list1) - set(list2))
    list2 = list(set(list2) - set(list1))
    return list1 + list2