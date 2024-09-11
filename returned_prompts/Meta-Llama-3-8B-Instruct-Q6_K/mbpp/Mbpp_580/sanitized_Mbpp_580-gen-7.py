def extract_even(tup):
    even_elements = []
    for element in tup:
        if isinstance(element, tuple):
            even_elements.append(extract_even(element))
        elif element % 2 == 0:
            even_elements.append(element)
    return tuple(even_elements) if even_elements else ()