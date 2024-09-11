def extract_index_list(l1, l2, l3):
    l1 = list(enumerate(l1))
    l2 = list(enumerate(l2))
    l3 = list(enumerate(l3))
    common = set([i for i in l1 if i in l2 and i in l3])
    return [i[1] for i in common]