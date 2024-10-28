def count_element_in_list(lst, element):
    count = 0
    for sub_list in lst:
        if element in sub_list:
            count += 1
    return count