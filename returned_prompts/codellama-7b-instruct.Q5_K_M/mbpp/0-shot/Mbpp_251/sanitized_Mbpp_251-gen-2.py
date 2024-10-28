def insert_element(my_list, element):
    new_list = []
    for i in range(len(my_list)):
        new_list.append(element)
        new_list.append(my_list[i])
    return new_list