def sub_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    return [list1[i] - list2[i] for i in range(len(list1))]
