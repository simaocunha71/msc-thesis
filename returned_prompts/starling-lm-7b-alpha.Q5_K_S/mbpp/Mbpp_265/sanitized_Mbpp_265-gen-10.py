def list_split(lst, n):
    new_list = []
    while len(lst) > 0:
        new_list.append(lst[:n])
        lst = lst[n:]
    return new_list