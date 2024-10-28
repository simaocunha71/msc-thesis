def merge_sorted_list(list1, list2, list3):
    result = []
    while list1 or list2 or list3:
        if not list1:
            result.append(list2.pop(0))
        elif not list2:
            result.append(list1.pop(0))
        elif not list3:
            result.append(list1.pop(0))
        elif list1[0] < list2[0]:
            result.append(list1.pop(0))
        elif list2[0] < list3[0]:
            result.append(list2.pop(0))
        else:
            result.append(list3.pop(0))
    return result

