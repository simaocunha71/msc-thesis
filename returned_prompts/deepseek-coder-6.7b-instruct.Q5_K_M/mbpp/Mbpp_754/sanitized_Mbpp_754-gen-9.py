def extract_index_list(l1, l2, l3):
    common = []
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            common.append(l1[i])
    return common