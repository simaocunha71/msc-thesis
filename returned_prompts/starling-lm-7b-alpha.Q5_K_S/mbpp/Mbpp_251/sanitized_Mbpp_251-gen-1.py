def insert_element(lst, elem):
    result = [elem]
    for i in range(len(lst)):
        result.append(lst[i])
        result.append(elem)
    return result