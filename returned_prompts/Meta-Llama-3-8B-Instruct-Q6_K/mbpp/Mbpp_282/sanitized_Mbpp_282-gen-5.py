def sub_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same length')
    return [a - b for a, b in zip(list1, list2)]