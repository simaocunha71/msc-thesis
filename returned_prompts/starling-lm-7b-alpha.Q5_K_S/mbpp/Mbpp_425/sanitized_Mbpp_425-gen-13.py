def count_element_in_list(list_of_lists, element):
    counter = 0
    for sublist in list_of_lists:
        if element in sublist:
            counter += 1
    return counter