def remove_elements(lst1, lst2):
    lst1[:] = [i for i in lst1 if i not in lst2]
    return lst1