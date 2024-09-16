def unique_sublists(my_list):
    return {
        tuple(sublist): my_list.count(sublist)
        for sublist in map(tuple, my_list)
    }
