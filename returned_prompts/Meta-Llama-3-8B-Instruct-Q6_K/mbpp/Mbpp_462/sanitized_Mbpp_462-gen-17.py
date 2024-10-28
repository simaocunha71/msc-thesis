def combinations_list(lst):
    result = [[]]
    for x in lst:
        result += [curr + [x] for curr in result]
    return result