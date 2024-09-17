def sub_list(list1, list2):
    if len(list1) != len(list2):
        return None
    else:
        return [list1[i] - list2[i] for i in range(len(list1))]