def is_sublist(lst, sub_lst):
    if len(sub_lst) > len(lst):
        return False
    else:
        for i in range(len(lst)-len(sub_lst)+1):
            if lst[i:i+len(sub_lst)] == sub_lst:
                return True
    return False