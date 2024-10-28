def remove_elements(lst1, lst2):
    for i in lst2:
        if i in lst1:
            lst1.remove(i)
    return lst1