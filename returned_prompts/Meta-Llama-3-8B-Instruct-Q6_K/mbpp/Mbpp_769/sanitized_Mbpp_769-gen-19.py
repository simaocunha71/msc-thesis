def Diff(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    for i in list2:
        if i not in list1:
            result.append(i)
    return result