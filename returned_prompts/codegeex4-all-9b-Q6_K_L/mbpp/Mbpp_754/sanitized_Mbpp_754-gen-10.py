def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(min(len(l1), len(l2), len(l3))):
        if l1[i] == l2[i] == l3[i]:
            common_elements.append(l1[i])
    return common_elements