def extract_index_list(l1, l2, l3):
    return list(set([x for x in l1 if x in l2 and x in l3]))