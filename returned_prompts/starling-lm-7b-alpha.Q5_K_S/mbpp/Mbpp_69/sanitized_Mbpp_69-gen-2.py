def is_sublist(list1,list2):
    if len(list1)<len(list2):
        return False
    for i in range(len(list2)):
        if list1[i]!=list2[i]:
            return False
    return True