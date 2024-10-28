
def recursive_list_sum(list_tuple):
    sum_list = 0
    for elem in list_tuple:
        if type(elem) == list:
            sum_list += recursive_list_sum(elem)
        else:
            sum_list += elem
    return sum_list


