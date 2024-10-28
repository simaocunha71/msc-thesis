def insert_element(lst, elem):
    new_list = [elem]
    for i in lst:
        new_list.append(elem)
        new_list.append(i)
    return new_list