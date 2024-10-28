def replace_list(list1, list2):
    if not list2:
        return list1
    list1[-1:] = list2
    return list1