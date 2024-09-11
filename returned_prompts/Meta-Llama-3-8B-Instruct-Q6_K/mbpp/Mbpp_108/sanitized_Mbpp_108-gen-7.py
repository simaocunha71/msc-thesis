def merge_sorted_list(list1, list2, list3):
    result = []
    i, j, k = 0, 0, 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] < list2[j] and list1[i] < list3[k]:
            result.append(list1[i])
            i += 1
        elif list2[j] < list1[i] and list2[j] < list3[k]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list3[k])
            k += 1
    while i < len(list1):
        result.append(list1[i])
        i += 1
    while j < len(list2):
        result.append(list2[j])
        j += 1
    while k < len(list3):
        result.append(list3[k])
        k += 1
    return result