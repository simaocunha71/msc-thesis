def consecutive_duplicates(lst):
    new_lst = []
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            new_lst.append(lst[i])
    new_lst.append(lst[-1])
    return new_lst