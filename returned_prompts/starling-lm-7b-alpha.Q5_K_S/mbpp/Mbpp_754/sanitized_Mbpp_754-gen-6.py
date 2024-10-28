def extract_index_list(l1, l2, l3):
    common_indices = []
    for index in range(len(l1)):
        if l1[index] in l2 and l1[index] in l3:
            common_indices.append(index)
    return common_indices