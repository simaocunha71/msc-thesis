def Diff(list1, list2):
    list1_set = set(list1)
    list2_set = set(list2)
    difference = list1_set.difference(list2_set)
    return list(difference)