def multiply_num(my_list):
    my_list_product = 1
    for num in my_list:
        my_list_product *= num
    return my_list_product / len(my_list)


