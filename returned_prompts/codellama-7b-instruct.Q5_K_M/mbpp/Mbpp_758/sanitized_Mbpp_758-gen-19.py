def unique_sublists(my_list):
    uniques = {}
    for sublist in map(tuple, my_list):
        if sublist not in uniques:
            uniques[sublist] = 0
        uniques[sublist] += 1
    return uniques