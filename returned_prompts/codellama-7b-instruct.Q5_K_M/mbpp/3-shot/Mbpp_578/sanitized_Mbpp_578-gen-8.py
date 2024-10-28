def interleave_lists(list_1, list_2, list_3):
    interleaved_list = []
    for i in range(len(list_1)):
        interleaved_list.append(list_1[i])
        interleaved_list.append(list_2[i])
        interleaved_list.append(list_3[i])
    return interleaved_list