def remove_elements(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result