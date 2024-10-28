def merge_sorted_list(list1, list2, list3):
    result = []
    while len(list1) > 0 and len(list2) > 0 and len(list3) > 0:
        if list1[0] <= list2[0] and list1[0] <= list3[0]:
            result.append(list1.pop(0))
        elif list2[0] <= list3[0]:
            result.append(list2.pop(0))
        else:
            result.append(list3.pop(0))
    result.extend(list1)
    result.extend(list2)
    result.extend(list3)
    return result