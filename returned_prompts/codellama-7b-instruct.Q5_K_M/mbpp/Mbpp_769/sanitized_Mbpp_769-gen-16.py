def Diff(list1, list2):
    return (list(list(set(list1) - set(list2))) + list(list(set(list2) - set(list1))))