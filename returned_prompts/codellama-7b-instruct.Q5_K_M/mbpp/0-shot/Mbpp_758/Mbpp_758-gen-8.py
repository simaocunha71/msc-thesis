def unique_sublists(my_list):
    return {frozenset(sublist): my_list.count(sublist) for sublist in set(map(tuple, my_list))}



