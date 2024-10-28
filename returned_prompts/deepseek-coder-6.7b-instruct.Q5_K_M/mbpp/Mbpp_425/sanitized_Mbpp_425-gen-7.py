def count_element_in_list(lst, n):
    count = 0
    for sublist in lst:
        if isinstance(sublist, list):
            count += sublist.count(n)
        else:
            if sublist == n:
                count += 1
    return count