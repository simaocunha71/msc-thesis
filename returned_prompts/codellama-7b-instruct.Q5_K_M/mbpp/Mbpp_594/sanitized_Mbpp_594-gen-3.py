def diff_even_odd(my_list):
    return my_list[next(i for i, x in enumerate(my_list) if x % 2 == 0)] - my_list[next(i for i, x in enumerate(my_list) if x % 2 == 1)]