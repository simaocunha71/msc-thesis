def merge_sorted_list(list_a, list_b, list_c):
    list_a.extend(list_b)
    list_a.extend(list_c)
    list_a.sort()
    return list_a