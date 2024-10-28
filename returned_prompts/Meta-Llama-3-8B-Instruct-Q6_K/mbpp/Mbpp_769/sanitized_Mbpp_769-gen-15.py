def Diff(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1 & set2
    diff1 = list(set1 - common)
    diff2 = list(set2 - common)
    return diff1 + diff2