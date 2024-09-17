def merge_sorted_list(list1, list2, list3):
    list1.extend(list2)
    list1.extend(list3)
    return sorted(list1)