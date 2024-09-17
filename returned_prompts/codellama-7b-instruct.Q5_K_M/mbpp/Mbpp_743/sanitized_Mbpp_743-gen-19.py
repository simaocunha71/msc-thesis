def rotate_right(my_list, n):
    n = n % len(my_list)
    return my_list[-n:] + my_list[:-n]