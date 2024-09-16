def maximize_elements(tuple_list_1, tuple_list_2):
    tuple_list_3 = []
    for i in range(len(tuple_list_1)):
        tuple_list_3.append((max(tuple_list_1[i][0], tuple_list_2[i][0]), max(tuple_list_1[i][1], tuple_list_2[i][1])))
    return tuple_list_3
