
def common_in_nested_lists(nested_list):
    common_elements = []
    for sublist in nested_list:
        for element in sublist:
            if element not in common_elements:
                common_elements.append(element)
    return common_elements


