def check_element(input_list, element):
    # Returns True if all items in the list
    # are equal to the given element
    return all(x == element for x in input_list)