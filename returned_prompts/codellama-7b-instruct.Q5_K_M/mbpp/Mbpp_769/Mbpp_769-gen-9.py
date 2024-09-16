def Diff(list1, list2):
    diff = []
    for i in list1:
        if i not in list2:
            diff.append(i)
    for j in list2:
        if j not in list1:
            diff.append(j)
    diff.sort()
    return diff
