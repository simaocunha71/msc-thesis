def count_element_in_list(list_of_lists, target_element):
    target_element = target_element.lower()
    count = 0
    for sublist in list_of_lists:
        for element in sublist:
            if element.lower() == target_element:
                count += 1
                break
    return count