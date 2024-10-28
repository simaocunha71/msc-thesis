def unique_sublists(my_list):
    res = {}
    for sublist in my_list:
        tup = tuple(sublist)
        res[tup] = res.get(tup, 0) + 1
    return res
