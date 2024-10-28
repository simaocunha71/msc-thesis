def extract_even(nested_tuple):
    even_elements = []
    for element in nested_tuple:
        if isinstance(element, tuple):
            even_elements.append(extract_even(element))
        else:
            if element % 2 == 0:
                even_elements.append(element)
    return tuple(even_elements)