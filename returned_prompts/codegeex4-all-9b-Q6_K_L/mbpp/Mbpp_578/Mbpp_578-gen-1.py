def interleave_lists(list1, list2, list3):
    return [i for sublist in zip(list1, list2, list3) for i in sublist]

