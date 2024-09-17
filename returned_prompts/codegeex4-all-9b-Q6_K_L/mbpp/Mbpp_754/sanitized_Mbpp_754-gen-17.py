def extract_index_list(l1, l2, l3):
    return [x for x, y, z in zip(l1, l2, l3) if x == y == z]