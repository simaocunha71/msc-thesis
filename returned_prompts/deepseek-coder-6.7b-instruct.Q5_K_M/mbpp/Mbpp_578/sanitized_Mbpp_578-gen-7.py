def interleave_lists(list1, list2, list3):
    interleaved_list = []
    for i in range(len(list1)):
        interleaved_list.append(list1[i])
        interleaved_list.append(list2[i])
        interleaved_list.append(list3[i])
    return interleaved_list