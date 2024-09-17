def insert_element(lst, element):
    result = []
    for e in lst:
        result.append(element)
        result.append(e)
    return result