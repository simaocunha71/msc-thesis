def merge_sorted_list(l1, l2, l3):
    l1.extend(l2)
    l1.extend(l3)
    l1.sort()
    return l1

