def insert_element(lst, element):
    new_list = [element]
    for item in lst:
        new_list.extend([element, item])
    return new_list