def interleave_lists(list1, list2, list3):
    return [num for sublist in zip(list1, list2, list3) for num in sublist]