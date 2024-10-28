def extract_index_list(l1, l2, l3):
    return [i for i in set(l1) if l1.count(i) == 3 and i in l2 and i in l3]