def insert_element(my_list, elem):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(elem)
        new_list.append(my_list[i])
    return new_list