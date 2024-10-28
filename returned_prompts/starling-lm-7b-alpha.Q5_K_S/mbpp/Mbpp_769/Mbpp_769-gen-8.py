
def Diff(list1, list2):
    list_dif = []
    for i in list1:
        if i not in list2:
            list_dif.append(i)
    return list_dif


