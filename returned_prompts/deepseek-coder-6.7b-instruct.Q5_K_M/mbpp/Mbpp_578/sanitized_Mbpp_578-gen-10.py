def interleave_lists(lst1, lst2, lst3):
    result = []
    for i in range(len(lst1)):
        result.extend([lst1[i], lst2[i], lst3[i]])
    return result