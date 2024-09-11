def Diff(list1, list2):
    return list(set([i for i in list1 if i not in list2]) + [i for i in list2 if i not in list1])