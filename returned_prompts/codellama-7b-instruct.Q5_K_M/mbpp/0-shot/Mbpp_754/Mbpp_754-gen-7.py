def extract_index_list(l1, l2, l3):
    if len(l1) != len(l2) or len(l2) != len(l3):
        return []
    res = []
    for i in range(len(l1)):
        if l1[i] == l2[i] and l1[i] == l3[i]:
            res.append(l1[i])
    return res
