def count_element_in_list(lst, element):
    count = 0
    for sublst in lst:
        if element in sublst:
            count += 1
    return count