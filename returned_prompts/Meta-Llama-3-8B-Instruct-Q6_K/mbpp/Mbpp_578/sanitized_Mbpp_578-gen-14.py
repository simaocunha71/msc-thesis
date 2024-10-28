def interleave_lists(list1, list2, list3):
    result = []
    for i in range(max(len(list1), len(list2), len(list3))):
        if i < len(list1):
            result.append(list1[i])
        if i < len(list2):
            result.append(list2[i])
        if i < len(list3):
            result.append(list3[i])
    return result