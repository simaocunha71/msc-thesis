def extract_index_list(l1, l2, l3):
    temp_list = []
    for i in range(len(l1)):
        if l1[i] == l2[i] and l1[i] == l3[i]:
            temp_list.append(l1[i])
    return temp_list
l1 = [1, 1, 3, 4, 5, 6, 7]
l2 = [0, 1, 2, 3, 4, 5, 7]
l3 = [0, 1, 2, 3, 4, 5, 7]