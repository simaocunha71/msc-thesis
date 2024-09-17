def unique_sublists(list_of_sublists):
    result = {}
    for i in list_of_sublists:
        if i not in result:
            result[tuple(i)] = 1
        else:
            result[tuple(i)] += 1
    return result