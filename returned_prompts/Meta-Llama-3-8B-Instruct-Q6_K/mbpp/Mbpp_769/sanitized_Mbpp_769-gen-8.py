def Diff(list1, list2):
    return list(set(list1) - set(list2)) + [i for i in list1 if i not in list2]