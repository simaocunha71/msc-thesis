def Diff(list1, list2): 
    return [x for x in list1 if x not in list2] + [x for x in list2 if x not in list1]