def insert_element(list, elem):
    new_list = []
    for i in range(len(list)):
        new_list.append(elem)
        new_list.append(list[i])
    return new_list