def insert_element(lst, elem):
    new_list = [elem]
    for item in lst:
        new_list.append(elem)
        new_list.append(item)
    return new_list