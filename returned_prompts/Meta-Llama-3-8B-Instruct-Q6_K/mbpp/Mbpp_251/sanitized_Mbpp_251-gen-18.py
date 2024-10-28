def insert_element(lst, element):
    result = [element]
    for i in lst:
        result.extend([element, i])
    return result