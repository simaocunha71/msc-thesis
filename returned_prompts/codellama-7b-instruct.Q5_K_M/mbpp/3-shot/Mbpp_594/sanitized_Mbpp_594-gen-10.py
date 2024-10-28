def diff_even_odd(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            first_even = my_list[i]
        else:
            first_odd = my_list[i]
    return first_even - first_odd