def merge_sorted_list(list1, list2, list3):
    result = []
    list1 = list(list1)
    list2 = list(list2)
    list3 = list(list3)
    while list1 and list2 and list3:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        elif list1[0] > list2[0]:
            result.append(list2.pop(0))
        else:
            result.append(list3.pop(0))
    result += list1 + list2 + list3
    return sorted(result)
