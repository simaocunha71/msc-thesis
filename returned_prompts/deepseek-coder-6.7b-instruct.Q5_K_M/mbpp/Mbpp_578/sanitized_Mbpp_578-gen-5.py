def interleave_lists(lst1, lst2, lst3):
    interleaved = []
    for i in range(len(lst1)):
        interleaved.append(lst1[i])
        interleaved.append(lst2[i])
        interleaved.append(lst3[i])
    return interleaved