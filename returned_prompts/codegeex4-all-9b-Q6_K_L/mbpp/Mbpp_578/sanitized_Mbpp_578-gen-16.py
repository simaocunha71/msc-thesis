def interleave_lists(list1:list,list2:list,list3:list) -> list:
    result = []
    for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
        result.append(list3[i])
    return result