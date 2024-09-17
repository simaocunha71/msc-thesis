def count_integer(my_list):
    ct = 0
    for i in my_list:
        if isinstance(i, int):
            ct += 1
    return ct