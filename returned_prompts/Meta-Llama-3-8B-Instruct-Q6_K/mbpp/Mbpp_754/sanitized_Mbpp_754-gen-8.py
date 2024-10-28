def extract_index_list(l1, l2, l3):
    return [x for x in set(l1) & set(l2) & set(l3) if l1.index(x) == l2.index(x) == l3.index(x)]