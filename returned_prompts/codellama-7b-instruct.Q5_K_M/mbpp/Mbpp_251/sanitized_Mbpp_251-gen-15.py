def insert_element(my_list, elem):
    new_list = []
    for i in my_list:
        new_list.append(elem)
        new_list.append(i)
    return new_list