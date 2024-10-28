def interleave_lists(list1, list2, list3):
    if len(list1) != len(list2) != len(list3):
        raise ValueError("lists must be of the same length")
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result