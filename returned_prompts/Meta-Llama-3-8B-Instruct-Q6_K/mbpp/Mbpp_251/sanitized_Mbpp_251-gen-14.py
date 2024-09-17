def insert_element(lst, element):
    result = []
    for i in lst:
        result.append(element)
        result.append(i)
    return result