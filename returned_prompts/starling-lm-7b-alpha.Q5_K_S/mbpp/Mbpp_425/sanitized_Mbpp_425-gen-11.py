def count_element_in_list(list1, element):
    count = 0
    for sublist in list1:
        if element in sublist:
            count += 1
    return count