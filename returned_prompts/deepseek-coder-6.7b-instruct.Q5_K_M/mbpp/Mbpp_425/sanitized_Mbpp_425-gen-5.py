def count_element_in_list(lst, x):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(x)
        else:
            if sublist == x:
                count += 1
    return count