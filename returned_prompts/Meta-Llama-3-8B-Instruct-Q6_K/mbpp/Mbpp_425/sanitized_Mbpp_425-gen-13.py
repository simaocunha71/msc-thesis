def count_element_in_list(list_of_lists, element):
    count = 0
    for sublist in list_of_lists:
        if element in sublist:
            count += 1
    return count