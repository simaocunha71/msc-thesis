def insert_element(lst, element):
    result = []
    for item in lst:
        result.extend([element, item])
    return result