def consecutive_duplicates(lst):
    """
    Remove consecutive duplicates of a given list
    """
    new_lst = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            new_lst.append(lst[i])
    return new_lst