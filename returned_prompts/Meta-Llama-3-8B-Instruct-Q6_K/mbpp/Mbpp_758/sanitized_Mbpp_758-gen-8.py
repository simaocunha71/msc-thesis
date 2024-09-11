def unique_sublists(lists):
    result = {}
    for sublist in lists:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in result:
            result[tuple_sublist] += 1
        else:
            result[tuple_sublist] = 1
    return result