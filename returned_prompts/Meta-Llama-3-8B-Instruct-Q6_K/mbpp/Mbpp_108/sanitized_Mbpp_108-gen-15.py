def merge_sorted_list(list1, list2, list3):
    result = []
    for lst in [list1, list2, list3]:
        result.extend(sorted(lst))
    return sorted(result)