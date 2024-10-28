def extract_index_list(l1, l2, l3):
    l = []
    for i in range(len(l1)):
        if l1[i] in l2 and l1[i] in l3:
            l.append(l1[i])
    return l