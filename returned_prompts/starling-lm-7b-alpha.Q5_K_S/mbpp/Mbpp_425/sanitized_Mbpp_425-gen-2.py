def count_element_in_list(list, element):
    count = 0
    for sublist in list:
        if element in sublist:
            count += 1
    return count