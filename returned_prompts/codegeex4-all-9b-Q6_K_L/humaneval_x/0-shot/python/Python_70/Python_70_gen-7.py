def strange_sort_list(lst):
    if len(lst) == 0: return []
    if len(lst) == 1: return lst
    sorted_lst = sorted(lst)
    new_lst = []
    i = 0
    while i < len(sorted_lst):
        new_lst.append(sorted_lst[i])
        i += 1
        if i < len(sorted_lst):
            new_lst.append(sorted_lst[-(i+1)])
            i += 1
    return new_lst
