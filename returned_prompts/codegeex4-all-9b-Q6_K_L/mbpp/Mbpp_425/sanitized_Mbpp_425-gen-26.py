def count_element_in_list(test_list, element):
    count = 0
    for sublist in test_list:
        if element in sublist:
            count += 1
    return count