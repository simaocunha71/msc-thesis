def extract_index_list(l1, l2, l3):
    result = []
    for i1, i2, i3 in zip(l1, l2, l3):
        if i1 == i2 == i3:
            result.append(i1)
    return result