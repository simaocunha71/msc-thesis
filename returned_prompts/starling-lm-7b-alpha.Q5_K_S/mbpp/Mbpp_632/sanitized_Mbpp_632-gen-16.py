def move_zero(list1):
    non_zero_list = [i for i in list1 if i != 0]
    return non_zero_list + [i for i in list1 if i == 0]