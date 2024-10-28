def count_element_in_list(lst, el):
    count = 0
    for sublst in lst:
        if el in sublst:
            count += 1
    return count