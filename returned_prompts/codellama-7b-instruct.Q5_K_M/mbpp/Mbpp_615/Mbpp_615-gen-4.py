def average_tuple(my_tuple):
    my_list = []
    for i in my_tuple:
        my_list.append(sum(i) / len(i))
    return my_list


