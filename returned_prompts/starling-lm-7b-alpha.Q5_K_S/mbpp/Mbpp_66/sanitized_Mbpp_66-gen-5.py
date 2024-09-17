def pos_count(lst):
    pos_list = []
    for i in lst:
        if i > 0:
            pos_list.append(i)
    return len(pos_list)