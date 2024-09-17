def merge_sorted_list(list1, list2, list3):
    """Merge three sorted lists into a single sorted list."""
    merged_list = []
    i = 0
    j = 0
    k = 0
    while i < len(list1) and j < len(list2) and k < len(list3):
        if list1[i] < list2[j] < list3[k]:
            merged_list.append(list2[j])
            j += 1
        elif list3[k] < list1[i] < list2[j]:
            merged_list.append(list3[k])
            k += 1
        else:
            merged_list.append(list1[i])
            i += 1
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    while k < len(list3):
        merged_list.append(list3[k])
        k += 1
    return merged_list