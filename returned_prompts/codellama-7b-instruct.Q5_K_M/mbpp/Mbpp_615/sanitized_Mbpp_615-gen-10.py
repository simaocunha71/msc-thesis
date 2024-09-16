def average_tuple(my_tuple):
    my_list = []
    for t in my_tuple:
        my_list.append(sum(t) / len(t))
    return my_list