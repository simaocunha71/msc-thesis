def add_pairwise(tup):
    new_list = []
    for i in range(len(tup)-1):
        new_list.append(tup[i] + tup[i+1])
    return tuple(new_list)