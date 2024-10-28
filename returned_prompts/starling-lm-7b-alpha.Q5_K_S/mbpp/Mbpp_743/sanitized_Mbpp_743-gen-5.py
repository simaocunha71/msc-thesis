def rotate_right(list1,n):
    new_list = list1[n:] + list1[:n]
    return new_list