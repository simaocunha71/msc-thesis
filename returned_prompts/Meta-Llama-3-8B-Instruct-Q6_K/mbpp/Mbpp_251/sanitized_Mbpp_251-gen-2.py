def insert_element(lst, element):
    result = [element]
    for i in lst:
        result.append(element)
        result.append(i)
    return result