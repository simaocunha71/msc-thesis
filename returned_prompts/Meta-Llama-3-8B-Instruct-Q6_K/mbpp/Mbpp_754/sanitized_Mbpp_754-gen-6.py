def extract_index_list(l1, l2, l3):
    result = [i for i in zip(l1, l2, l3) if i[0] == i[1] == i[2]]
    return [i for i in result for i in i]