def count_element_in_list(input_list, element):
    count = 0
    for sublist in input_list:
        if element in sublist:
            count += 1
    return count