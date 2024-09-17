def insert_element(lst, element):
    result = [element]
    for item in lst:
        result.extend([element, item])
    return result