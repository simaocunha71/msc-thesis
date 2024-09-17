def extract_index_list(l1, l2, l3):
    common_elements = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            if l1[i] not in common_elements:
                common_elements.append(l1[i])
    return common_elements