def div_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be the same length")
    return [i/j for i, j in zip(list1, list2)]